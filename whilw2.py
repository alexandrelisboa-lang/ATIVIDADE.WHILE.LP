import os
os.system("cls")

login = "xandinhometedor"
sen = "xandinhobambambam"
while True:
    log=str(input("digite seu login: "))
    senha=input("digite sua senha: ")
    if sen== senha and log == login:
        print("acesso permitido")
        break
    else:
        print ("acesso negado \ tente novamente -------- ")