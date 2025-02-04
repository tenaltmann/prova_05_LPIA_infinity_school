numero_de_alunos = int(input("Inisira o número de alunos que voc~e quer cadatrar: "))
alunos = {}
soma_total = 0
quantidade_de_notas = 0

for i in range (numero_de_alunos):

    nome = input("Nome do aluno: ")
    notas = [
        float(input("Insira a primeira nota do aluno: ")),
        float(input("Insira a segunda nota do aluno: ")),
        float(input("Insira a terceira nota do aluno: "))]
    
    alunos[nome] = notas


for nome, notas in alunos.items():    
    soma_notas = sum(notas)
    soma_total += soma_notas
    quantidade_de_notas += len(notas)

    media = soma_notas / 3

    if media >= 7:
        mencao = "APROVADO"
    else:
        mencao = "REPROVADO"
    print(f"o aluno(a) {nome} tirou as seguintes {notas} e sua média foi {media:.2f}, portanto ele está {mencao}")


media_sala = soma_total / quantidade_de_notas

print(f" A MEDIA DA TURMA FOI DE {media_sala} PONTOS")





















