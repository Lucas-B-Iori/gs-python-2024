import json

# Lista para armazenar questões sobre o oceano
problemas = []

# Função para salvar dados em um arquivo JSON
def salva_arquivo():
    with open('ocean_issues.json', 'w') as file:
        json.dump(problemas, file)


# Função para carregar dados de um arquivo JSON
def carrega_do_arquivo():
    global problemas
    try:
        with open('ocean_issues.json', 'r') as file:
            problemas = json.load(file)
    except FileNotFoundError:
        problemas = []


#Função para validar dados de entrada
def valida_entrada(msg, msg_erro):
    while True:
        entrada = input(msg).strip()
        if entrada:
            break
        print(msg_erro)
    return entrada


#Função para garantir que o index acessado é valido
def garante_index_valido(msg):
    while True:
        try:
            index = int(input(msg)) - 1
            if 0 <= index < len(problemas):
                break
            else:
                print("Número do problema inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")
    return index


#Função para pedir dados ao usuario
def pega_dados():
    campos = ['titulo', 'descricao', 'categoria']
    dados = {}

    for campo in campos:
        entrada = valida_entrada(f"Digite o {campo} do problema: ", f"O {campo} não pode estar vazio.")
        dados[campo] = entrada
    return dados

# Função para criar uma nova questão
def cria_problema():

    dados = pega_dados()
    problema = {"titulo": dados['titulo'], "descricao": dados['descricao'], "categoria": dados['categoria']}
    problemas.append(problema)
    print("Questão criada com sucesso!")
    salva_arquivo()


# Função para ler todas as questões
def le_problemas():
    if not problemas:
        print("Nenhuma questão encontrada.")
    else:
        for index in range(len(problemas)):
            problema = problemas[index]
            print(f"{index + 1}. {problema['titulo']} (Categoria: {problema['categoria']})\n   {problema['descricao']}")


# Função para atualizar uma questão existente
def atualiza_problema():
    le_problemas()
    index = garante_index_valido("Digite o número da questão que deseja atualizar: ")
    if 0 <= index < len(problemas):
        dados = pega_dados()
        problemas[index] = {"titulo": dados['titulo'], "descricao": dados['descricao'], "categoria": dados['categoria']}
        print("Questão atualizada com sucesso!")
        salva_arquivo()
    else:
        print("Número da questão inválido.")


# Função para deletar uma questão
def deleta_problema():
    le_problemas()
    if not problemas:
        return

    index = garante_index_valido("Digite o número da questão que deseja deletar: ")

    del problemas[index]
    print("Questão deletada com sucesso!")
    salva_arquivo()


# Função para exibir o menu
def menu():
    carrega_do_arquivo()
    while True:
        print("\nMenu:")
        print("1. Criar nova questão")
        print("2. Ler todas as questões")
        print("3. Atualizar uma questão")
        print("4. Deletar uma questão")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cria_problema()
        elif escolha == '2':
            le_problemas()
        elif escolha == '3':
            atualiza_problema()
        elif escolha == '4':
            deleta_problema()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o menu
menu()
