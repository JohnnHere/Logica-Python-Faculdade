print("Bem vindo à sorveteria da Orlando Produções - João Orlando Ferreira Junior")

# Define preços de acordo com sabor e tamanho
sabores = {
    "TR": {"P": 6, "M": 10, "G": 18},
    "ES": {"P": 7, "M": 12, "G": 21},
    "PR": {"P": 8, "M": 14, "G": 24},
}

# Instanciando o total como 0, para que ele possa ser declarado sem nenhuma alteração indesejada no valor
total = 0

# Laço condicional para saber o pedido do cliente
while True:
    # Perguntando ao cliente o tamanho e o sabor do sorvete
    tamanho = input("Qual o tamanho do pote de sorvete desejado (P, M, G)? ")
    sabor = input("Qual o sabor do sorvete desejado (TR, ES, PR)? ")

    # Laço condicional para saber se os valores escolhidos são válidos
    if tamanho not in ["P", "M", "G"] or sabor not in sabores:
        print("Tamanho ou sabor inválido(s).")
        continue

    # Adiciona o preço do sorvete ao valor total
    total += sabores[sabor][tamanho]

    # Perguntar ao cliente se ele deseja mais alguma coisa
    mais = input("Deseja pedir mais alguma coisa (s/n) ? ")
    if mais != "s":
        break

# Mostre o valor total
print("Valor da compra:", total)