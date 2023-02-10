#def big_mac():
#  print("sanduiche big mac")

#print("Inicio")
#big_mac()
#big_mac()
#print("Fim")  

def fazer_big_mac(nome):
  print(f"Sanduiche big mac {nome}")

#fazer_big_mac("Josi")
#fazer_big_mac("Leandro")
#fazer_big_mac("Clara")  

def Fazer_batata(tamanho):
  print(f"batata {tamanho}")

def preparar_refrigerante(tipo, tamanho):
  print(f"{tipo} {tamanho}")

#fazer_big_mac("Josi")
#Fazer_batata("Grande")
#preparar_refrigerante("Coca","Media")

#def fazer_combo_big_mac(nome,tamanho_batata,tipo_refri,tamanho_refri):

def soma_num(num1,num2):
  return num1 + num2

#resultado = soma_num(15,20)
#print(resultado)  

def maior_num(lista_num):
  lista_num.sort()
  lista_num.reverse()
  maior_num = lista_num[0]
  return maior_num

resultado = maior_num([300,25,30,500,2])
print(resultado)








