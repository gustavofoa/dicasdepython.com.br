title: Como ler arquivos CSV em python
date: 2018-07-19
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: CSV, IO
image: /images/logo-python.png

Existem várias formas de ler arquivos CSV em Python. Por padrão o python já oferece um pacote para trabalharmos com arquivos CSV.

Neste post vamos ver como ler arquivos CSV usando o pacote `csv` do python.

[>> Como ler arquivos CSV em java](https://dicasdejava.com.br/como-ler-arquivos-csv-em-java/){:target=\_blank}

##CSV de exemplo

Para os exemplos destes post, vamos usar um CSV simples.
Considere que o arquivo `pessoas.csv` esteja em algum lugar acessível para o seu programa python e tenha este conteúdo:

```
nome,idade,email
Gustavo,28,gustavo@dicasdeprogramcao.com.br
Joao,35,joao@dicasdepython.com.br
Maria,23,maria@dicasdeprogramacao.com.br
Ana,25,ana@dicasdepython.com.br
```

### Lendo CSV como array de Strings em python

O código abaixo mostrar como ler o arquivo CSV como um array de Strings e imprime na tela os valores de cada linha separadamente

```python
import csv

arquivo = open('pessoas.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    print(linha)
```

Saída:

```
['nome', 'idade', 'email']
['Gustavo', '28', 'gustavo@dicasdeprogramcao.com.br']
['Joao', '35', 'joao@dicasdepython.com.br']
['Maria', '23', 'maria@dicasdeprogramacao.com.br']
['Ana', '25', 'ana@dicasdepython.com.br']
```

Repare que este algoritmo considera o cabeçalho como uma linha normal.

### Lendo CSV como um dicionário em python

Uma interessante forma de se obter os dados de um CSV é na forma de um dicionário. O código abaixo mostra como fazer isso.

```python
import csv

arquivo = open('pessoas.csv')

pessoas = csv.DictReader(arquivo)

for pessoa in pessoas:
    print("Nome:", pessoa["nome"], " - Idade:", pessoa["idade"], " - Email:", pessoa["email"])
```

Saída:

```
Nome: Gustavo  - Idade: 28  - Email: gustavo@dicasdeprogramcao.com.br
Nome: Joao  - Idade: 35  - Email: joao@dicasdepython.com.br
Nome: Maria  - Idade: 23  - Email: maria@dicasdeprogramacao.com.br
Nome: Ana  - Idade: 25  - Email: ana@dicasdepython.com.br
```

Repare que neste exemplo o cabeçalho não foi considerado como uma linha normal, ele foi usado para dar nome às chaves do dicionário.

## Referências:

1. [pacote csv do python](https://docs.python.org/3/library/csv.html){:target=\_blank}
2. [Códigos-fonte deste post](https://github.com/gustavofoa/dicasdepython.com.br/tree/master/content/examples/csv){:target=\_blank}