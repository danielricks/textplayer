import subprocess
import time
import os
from logParser import LogParser

# Class Summary: TextPlayer([name of the game file], [boolean for debug flag])
# Methods:	run()
# 			parse_and_execute_command_file([text file containing a list of commands])
# 			execute_command([command string])
#			quit()

# Known issue: when you send the same command more than 15 times in a row, you stop receiving output for that command until a different command is sent.

class TextPlayer:

	def __init__(self, game_filename, debug_flag):
		self.assign_variables(game_filename, debug_flag)
		self.output_filename = 'frotz_output.txt'

	# Verifies the specified game file and assigns class variables
	def assign_variables(self, game_filename, debug_flag):

		self.running = True

		# Verify that specified game file exists, else limit functionality
		if game_filename == None or not os.path.exists('games/' + game_filename):
			self.running = False
			print "Use -h for help"
			return

		# Create variables used by the game (game log filenames, etc.)
		self.current_game = game_filename
		current_game_title = self.current_game.split('.')[0]
		self.game_log = 'log/' + current_game_title + '_log.txt'				# Ex. 'zork1_log.txt'
		self.old_game_log = 'log/' + current_game_title + '_log_old.txt'		# Ex. 'zork1_log_old.txt', clean
		self.game_log_clean = 'log/' + current_game_title + '_log_clean.txt'	# Ex. 'zork1_log_clean.txt'
		self.debug = debug_flag

	# Run game, returns the start game information
	def run(self):

		# Verify game is running
		if self.running == False:
			return

		# Refuse to run non-"Z-Machine" games
		if not self.current_game.endswith('z5'):
			return

		print "Running a copy of " + self.current_game

		# Attempt to remove all files used to log game info
		self.remove_old_files()

		# Create in_fifo pipe
		self.run_bash('mkfifo in_fifo')

		# Create log folder if it doesn't already exist
		if not os.path.isdir('log'):
			os.makedirs('log')

		# Run game
		self.run_bash_game('frotz games/' + self.current_game + ' < in_fifo > ' + self.game_log)

		# Prep the game for use (Frotz doesn't appear to load until it receives at least one command)
		self.run_bash('echo \" \" > in_fifo')

		# Clean initial game log
		self.run_bash('strings ' + self.game_log + ' > ' + self.game_log_clean)

		# Prep history comparisons
		self.run_bash('cp ' + self.game_log_clean + ' ' + self.old_game_log)

		# Get game start information
		p = LogParser()
		start_info = p.get_all_output(self.game_log_clean)

		# Write game start information to a file
		if self.debug:
			self.write_output_to_file(start_info)

		return start_info

	# Write text to the output file
	def write_output_to_file(self, text):
		if self.debug:
			output = open(self.output_filename, 'a')
			output.write(text + "\n\n\n")
		else:
			output = open(self.output_filename, 'w')
			output.write(text)
		output.close()

	# Parses through a text list of commands (or a single command) and executes them
	def parse_and_execute_command_file(self, filename):

		# Parse command file
		if (os.path.exists(filename)):
			f = open(filename, 'r')
			commands = f.read()
			f.close()
			if '\n' in commands:
				for command in commands.split('\n'):
					self.execute_command(command)
			else:
				self.execute_command(command)

	# Executes a single command on the current game
	def execute_command(self, command):

		# Verify game is running
		if self.running == False:
			return

		# Execute command
		if len(command) > 1:
			print "Command: " + command

			# Send command to game
			self.run_bash('echo \"' + command + '\" > in_fifo')

			# Send game output to log file
			self.run_bash('strings ' + self.game_log + ' > ' + self.game_log_clean)

			# Grabs most recent output in log file and sends it to the output file
			p = LogParser()
			command_output = p.get_last_output(self.game_log_clean, command, self.old_game_log, self.debug)

			# Write command output to a file
			if self.debug:
				self.write_output_to_file(command_output)

			return command_output

	# Runs a bash command
	def run_bash_game(self, command):
		process = subprocess.Popen(command, shell=True)

	# Run a bash command and wait until it finishes
	def run_bash(self, command):
		process = subprocess.Popen(command, shell=True)
		while process.poll() is None:
			time.sleep(0.00001)

	# Removes a file if it exists
	def remove_file_if_exists(self, filename):
		if os.path.exists(filename):
			self.run_bash('rm ' + filename)

	# Deletes old game logs
	def remove_old_files(self):
		self.remove_file_if_exists(self.game_log)
		self.remove_file_if_exists(self.old_game_log)
		self.remove_file_if_exists(self.old_game_log)
		self.remove_file_if_exists(self.output_filename)
		self.remove_file_if_exists('in_fifo')

	# Prints text if debug flag is set to True
	def print_if_debug(self, text):
		if self.debug:
			print text

	# Kills game process
	def kill(self):
		self.run_bash('pkill frotz')

	# Sends the game a general sequence of quitting commands
	def quit(self):
		if self.running == False:
			return
		print "Closing " + self.current_game
		self.run_bash('echo \"quit\" > in_fifo')
		self.run_bash('echo \"y\" > in_fifo')
		self.run_bash('echo \" \" > in_fifo')
		self.kill()

