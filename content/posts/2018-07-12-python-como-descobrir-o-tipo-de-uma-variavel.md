---
title: 'Python: Como descobrir o tipo de uma variável ou objeto'
date: '2018-07-12'
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: Básico, operadores
image: /images/logo-python.png
---

Para saber o tipo de um objeto ou variável, você pode usar a função `type()`do python,
passando o objeto ou variável como parâmetro.

O código mostra a utilização desta função para a descoberta do tipo da variável.

```python
lista = []

print( type(lista) )

dicionario = {}

print( type(dicionario) )

texto = 'a'

print( type(texto) )

numero = 23

print( type(numero) )

logico = False

print( type(logico) )

class Classe1 (object):
    pass

objeto = Classe1()

print( type(objeto) )
```

Saída:

```
<class 'list'>
<class 'dict'>
<class 'str'>
<class 'int'>
<class 'bool'>
<class '__main__.Classe1'>
```

Além disso, para testar se uma variável ou objeto é de um determinado tipo, você deve utilizar o perador `is`.
Veja

```python
lista = []

print( type(lista) is list )

dicionario = {}

print( type(dicionario) is dict )

texto = 'a'

print( type(texto) is str )

numero = 23

print( type(numero) is int )

logico = False

print( type(logico) is bool )

class Classe1 (object):
    pass

objeto = Classe1()

print( type(objeto) is Classe1 )
```

Saída:

```
True
True
True
True
True
True
```

Referências:

1. [Documentação: type](https://docs.python.org/3/library/stdtypes.html){:target=\_blank}
