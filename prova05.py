numero_de_alunos = int(input("Inisira o número de alunos da sua sala: "))
alunos = {}


for i in range (numero_de_alunos):
    
    opcao = int(input("Deseja adicionar um aluno: "))

    if opcao == 1:
        
        nome = input("Nome do aluno: ")
        nota_1 = float(input("Insira a primeira nota do aluno: "))
        nota_2 = float(input("Insira a primeira nota do aluno: "))
        nota_3 = float(input("Insira a primeira nota do aluno: "))
        nota_lista = [nota_1, nota_2, nota_3]
        alunos[nome] = nota_lista

    elif opcao == 2:
        break

print(alunos)



