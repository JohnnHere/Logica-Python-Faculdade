print("Bem vindo ao supermercado Orlando Produções - João Orlando Ferreira Junior")

while True: #Condicional para avaliar se o valor do produto não é inválido
    valor = float(input("Insira o valor do produto: ")) #Aqui é possível inserir o valor do produto do aplicativo.
    if valor > 0:
        break
    print("O valor do produto não pode ser zero ou negativo.")

while True: #Condicional para avaliar se a quantidade do produto não é inválida
    quantidade = int(input("Insira a quantidade do produto: ")) #Aqui é possível inserir a quantidade do produto
    if quantidade > 0:
        break
    print("A quantidade do produto não pode ser zero ou negativa.")

#A seguir, irei adequar o aplicativo à regra de negócio estipulada pelo exercício
if quantidade < 11: #Laço condicional para a hipótese da quantidade de produtos ser 11
    valor_total = valor * quantidade #Fórmula matemática simples para conseguir o valor total da compra
    valor_embalagem = 30.00 #Valor da embalagem para frete estipulado pelo exercício
    valor_total_com_embalagem = valor_total + valor_embalagem #Fórmula de soma simples para trazer o valor total da compra com o valor do frete
    print("O valor total sem a embalagem para frete é: R$", valor_total)
    print("O valor total com embalagem para frete é: R$", valor_total_com_embalagem)

elif quantidade >= 11 and quantidade < 101: #Mesma lógica do primeiro laço, porém com uma nova hipótese
    valor_total = valor * quantidade
    valor_embalagem = 60.00
    valor_total_com_embalagem = valor_total + valor_embalagem
    print("O valor total sem a embalagem para frete é: R$", valor_total)
    print("O valor total com embalagem para frete é: R$", valor_total_com_embalagem)

elif quantidade >= 101 and quantidade < 1001: #Mesma lógica do primeiro laço, porém com uma nova hipótese
    valor_total = valor * quantidade
    valor_embalagem = 120.00
    valor_total_com_embalagem = valor_total + valor_embalagem
    print("O valor total sem a embalagem para frete é: R$", valor_total)
    print("O valor total com embalagem para frete é: R$", valor_total_com_embalagem)

else: #Mesma lógica do primeiro laço, porém com uma nova hipótese
   valor_total = valor * quantidade
   valor_embalagem = 240.00
   valor_total_com_embalagem = valor_total + valor_embalagem
   print("O valor total sem a embalagem para frete é: R$", valor_total)
   print("O valor total com embalagem para frete é: R$", valor_total_com_embalagem)