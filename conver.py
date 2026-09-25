#Exibir a mensagem de entrada
print("Olá, esse é o conversor de moedas! Escolha a moeda que deseja converter"
" Essas são as opções:\n1 - Dólar\n2 - Euro\n3 - Kwanza\n4 - Afegâni\n5 - Yuan\n6 - Real")
entrada = input("Digite a moeda inicial: ").lower()
moe = input("Para qual moeda você deseja converter?: ").lower()
dinheiro = float(input("Digite o valor que deseja converter: "))

#Valores de cada moeda
dolareu = 0.87
dolarkw = 916.63
dolaraf = 63,53
dolaryuan = 6.71
dolarreal = 5.20


#o valor do euro em relação as outras moedas
eurodolar = 1.13
eurokw = 1044,27
euroaf = 73.
euroyuan = 7.66
euroreal = 592


#o valor do kwanza em relação as outras moedas
kwdolar = 0.0011
kweuro = 0.00095
kwaf = 0.070
kwyuan = 0.0073
kwreal = 0.0056


#o valor do afegâni em relação as outras moedas
afdolar = 0.016
afeuro = 0.01
afkw = 14.43
afyuan = 0.10
afreal = 0.08


#o valor do yuan em relação as outras moedas
yuandolar = 0.14
yuaneuro = 0.13
yuankw = 136.23
yuanaf = 10
yuanreal = 0.77

#o valor do real em relação as outras moedas


realdolar = 0.19
realeuro = 0.16
realkw = 176.02
realaf = 12
realyuan = 1.29

if entrada == "euro" and moe == "dólar":
    resultado = dinheiro * eurodolar
    print(f"O valor convertido é: {resultado:.2f} USD")
elif entrada == "euro" and moe == "kwanza":
    resultado = dinheiro * eurokw
    print(f"O valor convertido é: {resultado:.2f} Kz")
elif entrada == "euro" and moe == "afegâni":
    resultado = dinheiro * euroaf
    print(f"O valor convertido é: {resultado:.2f} AFN")
elif entrada == "euro" and moe == "yuan":
    resultado = dinheiro * euroyuan
    print(f"O valor convertido é: {resultado:.2f} CNY")
elif entrada == "euro" and moe == "real":
    resultado = dinheiro * euroreal
    print(f"O valor convertido é: {resultado:.2f} BRL")
#parte do dólar
elif entrada == "dólar" and moe == "euro":
    resultado = dinheiro * dolareu
    print(f"O valor convertido é: {resultado:.2f} EUR")
elif entrada == "dólar" and moe == "kwanza":
    resultado = dinheiro * dolarkw
    print(f"O valor convertido é: {resultado:.2f} Kz")
elif entrada == "dólar" and moe == "afegâni":
    resultado = dinheiro * dolaraf
    print(f"O valor convertido é: {resultado:.2f} AFN")
elif entrada == "dólar" and moe == "yuan":
    resultado = dinheiro * dolaryuan
    print(f"O valor convertido é: {resultado:.2f} CNY")
elif entrada == "dólar" and moe == "real":
    resultado = dinheiro * dolarreal
    print(f"O valor convertido é: {resultado:.2f} BRL")
#parte do kwanza
elif entrada == "kwanza" and moe == "euro":
    resultado = dinheiro * kweuro
    print(f"O valor convertido é: {resultado:.2f} EUR")
elif entrada == "kwanza" and moe == "dólar":
    resultado = dinheiro * kwdolar
    print(f"O valor convertido é: {resultado:.2f} USD")
elif entrada == "kwanza" and moe == "afegâni":
    resultado = dinheiro * kwaf
    print(f"O valor convertido é: {resultado:.2f} AFN")
elif entrada == "kwanza" and moe == "yuan":
    resultado = dinheiro * kwyuan
    print(f"O valor convertido é: {resultado:.2f} CNY")
elif entrada == "kwanza" and moe == "real":
    resultado = dinheiro * kwreal
    print(f"O valor convertido é: {resultado:.2f} BRL")
#parte do afegâni
elif entrada == "afegâni" and moe == "euro":
    resultado = dinheiro * afeuro
    print(f"O valor convertido é: {resultado:.2f} EUR")
elif entrada == "afegâni" and moe == "dólar":
    resultado = dinheiro * afdolar
    print(f"O valor convertido é: {resultado:.2f} USD")
elif entrada == "afegâni" and moe == "kwanza":
    resultado = dinheiro * afkw
    print(f"O valor convertido é: {resultado:.2f} Kz")
elif entrada == "afegâni" and moe == "yuan":
    resultado = dinheiro * afyuan
    print(f"O valor convertido é: {resultado:.2f} CNY")
elif entrada == "afegâni" and moe == "real":
    resultado = dinheiro * afreal
    print(f"O valor convertido é: {resultado:.2f} BRL")
    print(f"O valor convertido é: {resultado:.2f} BRL")
#parte do yuan
elif entrada == "yuan" and moe == "euro":
    resultado = dinheiro * yuaneuro
    print(f"O valor convertido é: {resultado:.2f} EUR")
elif entrada == "yuan" and moe == "dólar":
    resultado = dinheiro * yuandolar
    print(f"O valor convertido é: {resultado:.2f} USD")
elif entrada == "yuan" and moe == "kwanza":
    resultado = dinheiro * yuankw
    print(f"O valor convertido é: {resultado:.2f} Kz")
elif entrada == "yuan" and moe == "afegâni":
    resultado = dinheiro * yuanaf
    print(f"O valor convertido é: {resultado:.2f} AFN")
elif entrada == "yuan" and moe == "real":
    resultado = dinheiro * yuanreal
    print(f"O valor convertido é: {resultado:.2f} BRL")
#parte do real
elif entrada == "real" and moe == "euro":
    resultado = dinheiro * realeuro
    print(f"O valor convertido é: {resultado:.2f} EUR")
elif entrada == "real" and moe == "dólar":
    resultado = dinheiro * realdolar
    print(f"O valor convertido é: {resultado:.2f} USD")
elif entrada == "real" and moe == "kwanza":
    resultado = dinheiro * realkw
    print(f"O valor convertido é: {resultado:.2f} Kz")
elif entrada == "real" and moe == "afegâni":
    resultado = dinheiro * realaf
    print(f"O valor convertido é: {resultado:.2f} AFN")
elif entrada == "real" and moe == "yuan":
    resultado = dinheiro * realyuan
    print(f"O valor convertido é: {resultado:.2f} CNY")
else:
    print("Opção inválida. Por favor, escolha uma moeda válida para conversão.")
