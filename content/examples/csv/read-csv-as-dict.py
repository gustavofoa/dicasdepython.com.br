import csv

arquivo = open('pessoas.csv')

pessoas = csv.DictReader(arquivo)

for pessoa in pessoas:
    print("Nome:", pessoa["nome"], " - Idade:", pessoa["idade"], " - Email:", pessoa["email"])