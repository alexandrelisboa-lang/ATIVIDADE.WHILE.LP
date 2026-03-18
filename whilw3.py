import os 
os.system("cls")


login = "xandinhometedor"
sen = "xandinhobambambam"
tentativa=3

while True:
    for i in range (tentativa):
     log=str(input("digite seu login: "))
    senha=input("digite sua senha: ")
    if sen== senha and log == login:
        print("acesso permitido")
        break
    else:
        print ("acesso negado \ tente novamente -------- ")
        
        print("acesso negado,numero de tentativa superado ")
        break
        