title: Python: Como converter inteiro em string e vice-versa
date: 2018-07-10
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: String, inteiro
image: /images/logo-python.png

Para converter uma variável do tipo inteiro para um texto (string), basta usar a função `str`

```python
variavel_texto = str(28)
```

E para converter uma variável do tipo texto para uma variável do tipo inteiro, basta usar a função `int`.

```python
variavel_inteiro = int('10')
```

O código abaixo mostra como converter um valor do tipo inteiro para um valor do tipo string (texto) e vice-versa.

```python
variavel_texto = str(28)

print(variavel_texto + '1')

variavel_inteiro = int('10')

print(variavel_inteiro + 1)
```

Saída:

```
281
11
```

Referências:

1. [Documentação: função str](https://docs.python.org/3/library/functions.html#func-str){:target=\_blank}
2. [Documentação: função int](https://docs.python.org/3/library/functions.html#int){:target=\_blank}
