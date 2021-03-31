##############################
#     © SÍLVIO SILVA         #                    
#     Whatsapp/Telegram:     #
#       +244940989200        #
#                            #
#        10/02/2021          #
##############################
import os
import platform

if "Windows" in platform.system().lower():
    c = 'cls'
else:
    c = 'clear'
os.system(c)
g = '\033[1;32m'
r = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;36m'


def verifica_NIF(nif):
    NC = []
    try:
        if nif[0:4].isnumeric():
            NC.append(nif[0:4])
        if nif[4:8].isnumeric():
            NC.append(nif[4:8])

        if nif[8:9].isnumeric():
            NC.append(nif[8:9])

        if not nif[9:11].isnumeric():
            NC.append(nif[9:11])

        if nif[11:14].isnumeric():
            NC.append(nif[11:14])

        nif_valido = ''.join(NC)

        if nif[0:4].isnumeric() is False or nif[4:8].isnumeric() is False or nif[8:9] is False or nif[9:11].isnumeric() is True or nif[11:14].isnumeric() is False or len(nif) > 14 or len(nif) < 14:
            print(f'\n{r}O N.I.F. INTRODUZIDO NÃO É VÁLIDO!\033[m')
        else:
            print(f'\n{g}O N.I.F. INTRODUZIDO É VÁLIDO\033[m')
    except Exception as erro:
        print(f'{r}[!] ACONTECEU UM ERRO NÃO PROGRÁMAVEL\033[m')
        print('[!] ACESSE -> https://github.com/silviooosilva')
