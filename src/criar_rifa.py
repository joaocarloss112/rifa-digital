from datetime import datetime

def Criar_rifa():
    nome_rifa = str(input("Informe o nome da rifa a ser criada: "))
    descricao = str(input("Informe uma breve descrição da rifa: "))
    qtd = int(input("Informe a quantidade de números da rifa: "))
    preco = int(input("Informe o preço da rifa: "))
    data = input("Digite a data do sorteio (DD/MM/AAAA): ")
    try:
        data_objeto = datetime.strptime(data, "%d/%m/%Y")
        print(f"Data validada com sucesso: {data_objeto}")
        rifa = {
            "nome": nome_rifa,
            "descricao": descricao,
            "quantidade": qtd,
            "preco": preco,
            "data": data_objeto,
            "numeros_disponiveis": list(range(1, qtd + 1)),
            "compradores": {} 
        }
    except ValueError:
        print("Formato inválido! Use o padrão DD/MM/AAAA.")

def verificar_criacao(nome, descricao, qtd, preco, data):
    return {
            "nome": nome,
            "descricao": descricao,
            "quantidade": int(qtd),
            "preco": int(preco),
            "data": data
        }

