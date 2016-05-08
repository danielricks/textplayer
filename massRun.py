import os
from textPlayer import TextPlayer


'''
for game in os.listdir(os.getcwd() + '/games'):
	print game
	t = TextPlayer()
	t.assign_variables(game, True)
	t.run()
	t.parse_and_execute_command_file('commands.txt')
	t.quit()
'''


t = TextPlayer()
t.assign_variables('zork1.z5', False)
t.run()
t.parse_and_execute_command_file('commands.txt')
t.execute_command('look')
t.quit()

