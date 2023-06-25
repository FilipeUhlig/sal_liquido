"""
Programa: sal_liquido
Descrição: Este programa calcula o salário líquido de um trabalhador em uma empresa que remunera R$20,00 por hora.
Data : 24/06/2023
Versão: 0.0.1
"""

#Atribuição de variáveis



w = 0
h = 0

#Entrada de dados

h = float(input("Quantas horas são trabalhadas? "))

#Processamento de dados
w = (h*20)
if w <= 1000:
    wl = w
    print(f"Seu salário líquido é de {wl}.")
    
elif 1000 < w <= 2500:
    wl = w * 0.9
    print(f"Seu salário líquido é de {wl}.")
    
elif 2500 < w <= 5000:
    wl = w * 0.8
    print(f"Seu salário líquido é de {wl}.")
    
else:
    wl = w * 0.65
    print(f"Seu salário líquido é de {wl}.")
    
#Saida de dadaos