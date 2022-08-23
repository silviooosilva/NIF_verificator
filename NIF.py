##############################
#     © SÍLVIO SILVA         #                    
#     Whatsapp/Telegram:     #
#       +244940989200        #
#                            #
#        10/02/2021          #
##############################

from nif_main import *


def banner():
    print(f'{C}-\033[m' * 30)
    print(f'{C}|IDENTIFICADOR DE N.I.F. 2.0|\033[m')
    print(f'{C}-\033[m' * 30)

banner()

NIF = str(input(f'DIGITE O SEU N.I.F.:\n>'))
print('-' * 30)
print(validarNIF(NIF))
print('\033[1;33m\n\tBy: SÍLVIO SILVA\033[m')
