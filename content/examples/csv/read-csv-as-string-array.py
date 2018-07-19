import csv

arquivo = open('pessoas.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    print(linha)