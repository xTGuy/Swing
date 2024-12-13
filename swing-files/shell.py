import os
# For more information, go to https://github.com/xTGuy/Swing/

# ----------------------- #
# Config                  #
# ----------------------- #



# ----------------------- #
# Shell                   #
# ----------------------- #

exec = input('>> ')

# ----------------------- #
# SUR Package Manager     #
# ----------------------- #

if exec == 'sur':
    surget = input('Get Which Package? / SUR | >> ')
    os.system('cd SUR && wget https://raw.githubusercontent.com/xTguy/Swing/repo/SUR/' + surget + '.swi && cd .. && python3 shell.py')
elif exec == 'help':
    print('Help:')
    print('>> sur / Get Which Package? / SUR | >> <PKGNAME> || >> exit / <TERMINAL> || >> load / Load Which Package? | SUR >> <PKGNAME>')
    os.system('python3 shell.py')
elif exec == 'exit':
    quit()
elif exec == 'load':
    load = input('Load Which Package? / SUR | >> ')
    os.system('cd SUR && python3 '+ load + '.sur')
else:
    print('Swing: Illegal Input.')
    os.system('python3 shell.py')

# ----------------------- #
# Credits                 #
# ----------------------- #


