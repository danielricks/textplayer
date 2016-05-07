import argparse
import re

class LogParser:
	def __init__(self):
		self.args = None

	# Cleans text according to regex, removes new lines/excessive spaces, returns cleaned text
	def clean_text(self, line):
		line = re.sub(r'\[[?0-9a-z][;]*[0-9]*[;]*[a-z][0-9]*', ' ', line)
		line = re.sub(r'\[m', ' ', line)
		line = re.sub(r'\[131G[0-9]*', ' ', line)
		line = re.sub(r'\[[0-9]*;[0-9H]*[a-z]*', ' ', line)
		line = re.sub(r'\[[0-9]*[A-Z]*[0-9]*', ' ', line)
		line = self.tidy_text(line)
		while '  ' in line:
				line = line.replace('  ', ' ')
		return line

	# Opens and clean text, returns cleaned text
	def open_file_and_clean(self, filename):
		f = open(filename, 'r')
		f_text = f.read()
		f.close()
		f_text = self.clean_text(f_text)
		return f_text

	# Tidies up text
	def tidy_text(self, text):
		return text.replace('\n', '').replace('>', '')

	# Print debug statement
	def print_if_debug(self, debug, text):
		if (debug):
			print text

	# Prints the output from the entire log file to a file
	# Used at the beginning of a game, when we need the entire printout, not just what follows a specific command
	def get_all_output(self, input_filename, output_filename, debug):

		# Open and clean the text from game logs
		f_text = self.open_file_and_clean(input_filename)

		# Write new output to a file
		if debug:
			o = open(output_filename, 'a')
			o.write(self.tidy_text(f_text) + "\n\n\n")
		else:
			o = open(output_filename, 'w')
			o.write(self.tidy_text(f_text))
		o.close()

	# Prints the output for the input bash command to a file
	def get_last_output(self, input_filename, command, output_filename, old_output_filename, debug):

		# Open and clean the text from game logs
		f_text = self.open_file_and_clean(input_filename)
		r_text = self.open_file_and_clean(old_output_filename)

		# Compare old history to current history to see if anything has changed
		f_words = f_text.split(' ')
		r_words = r_text.split(' ')
		self.print_if_debug(debug, "Word diff: " + str(len(r_words)) + " vs " + str(len(f_words)))
		new_text = ''
		if (len(f_words) > len(r_words)):
			new_words = f_words[len(r_words):]
			new_text = " ".join(new_words)
		else:
			new_text = " ".join(f_words)

		# Write new output to a file
		if debug:
			o = open(output_filename, 'a')
			o.write(self.tidy_text(new_text) + "\n\n\n")
		else:
			o = open(output_filename, 'w')
			o.write(self.tidy_text(new_text))
		o.close()

		# Write current history for comparison in the future
		f = open(input_filename, 'r')
		f_text_orig = f.read()
		f.close()
		old = open(old_output_filename, 'w')
		old.write(f_text_orig)
		old.close()

