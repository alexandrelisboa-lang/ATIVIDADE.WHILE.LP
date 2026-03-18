import os 
os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 3
for i in range(QUANTIDADE_NOTAS):
 while True:
   nota = float(input(f"DIGITE SUA NOTA: "))
   if nota >= 0 and nota <= 10:
        soma +=nota
        break
    
print("acesso negado")
print(f"nota{nota}")
        
media = soma / QUANTIDADE_NOTAS
print(f"media{media}")
print("acesso permitido")   
    
print("FIM!")
        