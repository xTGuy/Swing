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
# Swing Packages          #
# ----------------------- #

# Put a URL or Directory tree here to add a swing package.
# e.g \/
# if exec == '<PKGNAME>':
#    os.system('cd <DIR> && <PKGNAME>.swi')

# SUR ARG Tree
    # No ARGs
if exec == 'sur':
    surpkg = input('Run Which PKG? | >> ')
    os.system('cd SUR && python3 ' + surpkg + '.swi')
    # ARG - Get
if exec == 'sur -S':
    surget = input('Get Which PKG? | >> ')
    os.system('cd SUR && wget https://raw.githubusercontent.com/xTguy/Swing/main/SUR/' + surget + '.swi && cd .. && python3 shell.py')
# End -------------

# Linux ARG Tree
    # No ARGs
if exec == 'linux':
    print('To go back, type ./swing in the /~ Directory.')
    quit()
    # Temp ARG
if exec == 'linux -t':
    lexec = input('Linux | >> ')
    if lexec == '05n82c785n2045987n304n958c709850v987n05983':
        os.system('echo HOW?????? | lolcat')
    else:
        os.system(lexec + ' && python3 shell.py')
        os.system('cd ~/.swing && python3 shell.py && echo Invalid Linux Command. | lolcat')
# End -------------
