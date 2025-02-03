numero_de_alunos = int(input("Inisira o número de alunos da sua sala: "))
alunos = {}


while True:
    print("Opções: ")
    print("1 - Adicionar Aluno")
    print("2 - Sair")

    opcao = input("Digite o Número da opção: ")

    if opcao == 1:
        nome = input("Nome do aluno: ")
        
        nota_1 = float(input("Insira a primeira nota do aluno: "))
        nota_2 = float(input("Insira a primeira nota do aluno: "))
        nota_3 = float(input("Insira a primeira nota do aluno: "))

        nota_lista = [nota_1, nota_2, nota_3]

        alunos[nome] = nota_lista
