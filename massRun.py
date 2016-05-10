import os
from textPlayer import TextPlayer


game_num = 0
for game in os.listdir(os.getcwd() + '/games'):
	print game, game_num
	t = TextPlayer(game, False)
	start_info = t.run()
	#print start_info
	t.parse_and_execute_command_file('commands.txt')
	#command_output = t.execute_command('go south')
	#print command_output
	#command_output = t.execute_command('go east')
	#print command_output
	#command_output = t.execute_command('go east')
	#print command_output
	#command_output = t.execute_command('go east')
	#print command_output
	#command_output = t.execute_command('look')
	#print command_output
	t.quit()
	game_num += 1


'''
t = TextPlayer('zork1.z5', False)
start_info = t.run()
print start_info
#t.parse_and_execute_command_file('commands.txt')
command_output = t.execute_command('open mailbox')
print command_output
command_output = t.execute_command('read leaflet')
print command_output
command_output = t.execute_command('go south')
print command_output
command_output = t.execute_command('go east')
print command_output
command_output = t.execute_command('open window')
print command_output
command_output = t.execute_command('enter window')
print command_output
command_output = t.execute_command('take bottle')
print command_output
command_output = t.execute_command('open bottle')
print command_output
command_output = t.execute_command('drink water')
print command_output
command_output = t.execute_command('take sack')
print command_output
command_output = t.execute_command('open sack')
print command_output
command_output = t.execute_command('eat lunch')
print command_output
command_output = t.execute_command('eat garlic')
print command_output
command_output = t.execute_command('go west')
print command_output
command_output = t.execute_command('take lantern')
print command_output
command_output = t.execute_command('take sword')
print command_output
command_output = t.execute_command('go east')
print command_output
command_output = t.execute_command('go east')
print command_output
command_output = t.execute_command('look')
print command_output
command_output = t.execute_command('inventory')
print command_output
t.quit()
'''
