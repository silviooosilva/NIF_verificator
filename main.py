##############################
#     © SÍLVIO SILVA         #                    
#     Whatsapp/Telegram:     #
#       +244940989200        #
#                            #
#        10/02/2021          #
##############################
g = '\033[1;32m'
r = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;36m'
import platform, os
if "Windows" in platform.system().lower():
    c = 'cls'
else:
    c = 'clear' 
os.system(c) 
def verifica_NIF(NIF):
    NC = [] 
    try:
        if NIF[0:4].isnumeric() == True:
            NC.append(NIF[0:4])
        if NIF[4:8].isnumeric() == True:
            NC.append(NIF[4:8])
  
        if NIF[8:9].isnumeric() == True:
            NC.append(NIF[8:9])
        
        if NIF[9:11].isnumeric() == False:
            NC.append(NIF[9:11]) 
        
        if NIF[11:14].isnumeric() == True:
            
            NC.append(NIF[11:14])
     
        nif_valido = ''.join(NC) 
        
        if NIF[0:4].isnumeric() == False or NIF[4:8].isnumeric() == False or NIF[8:9] == False or NIF[9:11].isnumeric() == True or NIF[11:14].isnumeric() == False or len(NIF) > 14 or len(NIF) < 14:
            print(f'\n{r}O N.I.F. INTRODUZIDO NÃO É VÁLIDO!\033[m')
        else:
            print(f'\n{g}O N.I.F. INTRODUZIDO É VÁLIDO\033[m') 
            
            
    except:
        print(f'{r}[!]ACONTECEU UM ERRO NÃO PROGRÁMAVEL\033[m')
        print('[!] ACESSE -> https://github.com/silviooosilva') 