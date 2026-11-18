name = ''
while name != 'your name':
    print('please type your name.')
    name = input('>')
    print ('Thank you!')
# The code inside this clause asks the user to type their name, which is
# assigned to the name variable. Since this is the last line of the block, the exe-
# cution moves back to the start of the while loop and reevaluates the condi-
# tion. If the value in name is not equal to the string 'your name', the condition
# is True, and the execution enters the while clause again.