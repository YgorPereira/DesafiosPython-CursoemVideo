# lendo dados de um aluno, guardando num dicionário e exibindo para o usúario.
alunos = {}
alunos['nome'] = str(input('Nome do aluno: '))
alunos['media'] = float(input('Média do aluno: '))
if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'
elif alunos['media'] < 5:
    alunos['situacao'] = 'Reprovado'
else:
    alunos['situacao'] = 'Em recuperação'

print (20 * '-=')
print(f'Nome: {alunos["nome"]}')
print(f'Média: {alunos["media"]:.2f}')
print(f'Situação: {alunos["situacao"]}')
