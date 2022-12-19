print("Bem vindo à empresa de limpeza da Orlando Produções - João Orlando Ferreira Junior")

#Declarando a função referente à metragem
def metragem_limpeza():
    metragem = input("Informe a quantidade de metros que irá ser limpa ")

#Uma estrutura de try/except que me permite tratar erros dentro do código. Nete caso, é para lidar com possíveis erros no momento
# em que a variável metragem é convertida para inteiro. Neste código eu passo a regra de negócio solicitada no exercício para
# que a função tenha o retorno desejado. As execeções são tratadas de modo que o programa impeça que valores indesejados sejam
# aceitos. Caso o usuário tente, ele continuará dentro de um loop que lhe perguntará a quantidade de metros.
    try:
        metragem = int(metragem)

        if not 30 <= metragem < 700:
            metragem_limpeza()

        else:
            metragem = int(metragem)

            if 30 <= metragem < 300:
                metragem_final = 60 + 0.3 * metragem

            else:
                metragem_final = 120 + 0.5 * metragem

            return metragem_final

    except:
        metragem_limpeza()

#Nesta função do tipo da limpeza, eu defino duas possibilidades para meu tipo de limpeza. Eu preciso que ela seja Básica OU Completa.
#O loop só sera interrompido caso o usuário digite as opções corretas. Aqui também é passada a regra de negócio solicitada pelo
#exercício.
def tipo_limpeza():

    tipo = ""
    multiplicador = 0

    while tipo != "Básica" and tipo != "Completa":
        tipo = input("A limpeza é Básica ou Completa ? ")

    if tipo == "Básica":
        multiplicador = 1.00

    elif tipo == "Completa":
        multiplicador = 1.30

    else:
        tipo_limpeza()

    return multiplicador

#Nesta função eu estou instanciando a limpeza adicional como 0 para que ela tenha um valor que não interfira no resultado esperado.
#dentro de servicos_adicionais eu crio um objeto para instanciar meus serviços e declará-los no início da função. O while me permite
# manter o loop enquanto o usuário não escolher recusar o serviço com a opção 0. Condições adequadas à regra de negócio.
def adicional_limpeza():
    limpeza_adicional = 0

    print(servicos_adicionais)

    while True:
        adicional = input("Deseja algum serviço adicional ?")

        if int(adicional) == 0:
            break

        elif int(adicional) in servicos_adicionais:
            limpeza_adicional = limpeza_adicional + preco_adicional[int(adicional)]

        else:
            continue

    return limpeza_adicional

servicos_adicionais = {0: "Não gostaria de nenhum serviço adicional",
                       1: "Gostaria de passar 10 peças de roupa",
                       2: "Gostaria de limpar Forno/Microondas",
                       3: "Gostaria de limparFreezer/Geladeira"}

preco_adicional = [0, 10.00, 12.00, 20.00]

#Aqui estou instanciando minhas funções dentro de variáveis para que eu possa montar uma fórmula dentro da variável total que receba
# os valores solicitados no enunciado.
valor = metragem_limpeza()

preco_limpeza = tipo_limpeza()

preco_adicionais = adicional_limpeza()

preco_total = (valor * preco_limpeza) + preco_adicionais

#O print é dessa maneira para que se possa printar os centavos.
print(f"O valor total do serviço ofertado é R$ {preco_total:,.2f}")