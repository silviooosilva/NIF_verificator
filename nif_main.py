##############################
#     © SÍLVIO SILVA         #
#     Whatsapp/Telegram:     #
#       +244940989200        #
#                            #
#        10/02/2021          #
##############################

from re import compile

# definindo o padrao para um NIF
padraoNIF = compile(r'(\d+)([A-Z]+)(\d+)')
g = '\033[1;32m'
r = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;36m'


def validarNIF(nif: str):
    resultado = padraoNIF.search(nif)
    if resultado:
        return f"{g}[i] - SIM É UM NIF VÁLIDO..\033[m"
    else:
        return f"{r}[x] - NÃO É UM NIF VÁLIDO..\033[m"


if __name__ == '__main__':
    exemploNIF1 = '123456AB7890'  # um NIF aparentemente valido
    exemploNIF2 = '09876cd54321'  # um NIF com letras minusculas
    exemploNIF3 = 'EF1234567890'  # um NIF com letras no inicio do padrao
    exemploNIF4 = '1234567890GH'  # um NIF com letras no final do padrao
    print(f"{exemploNIF1} é um NIF válido?: {validarNIF(exemploNIF1)}")
    print(f"{exemploNIF2} é um NIF válido?: {validarNIF(exemploNIF2)}")
    print(f"{exemploNIF3} é um NIF válido?: {validarNIF(exemploNIF3)}")
    print(f"{exemploNIF4} é um NIF válido?: {validarNIF(exemploNIF4)}")
    print('\033[1;33m\n\tBy: SÍLVIO SILVA\033[m')
