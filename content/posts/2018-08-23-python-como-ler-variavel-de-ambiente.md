---
title: 'Python: Como ler variavel de ambiente'
date: '2018-08-23'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: system
image: /images/logo-python.png
---

As variáveis de ambiente do sistema operacional são acessíveis através do dicionário `os.environ` do pacote `os`.

Portanto, para acessar o valor de uma variável de ambiente em Python,
basta passar o nome da variável de ambiente entre colchetes no `os.environ['NOME-DA-VARIÁVEL-DE-AMBIENTE']`.

O código abaixo mostra um exemplo de como acessar a variável de ambiente chamada `OS` no meu sistema operacional.

```python
import os
print(os.environ['OS'])
```

Saída:

```
Windows_NT
```

**Importante!** A variável de ambiente `OS` já estava configurada na minha máquina no momento da execução.

Você pode consultar o valor de qualquer variável de ambiente do seu sistema operacional.

## Exemplo de execução

![Como ler variável de ambiente com Python](/images/ler-variavel-de-ambiente.gif){:width=100%}

## Referência

1. [Doc: os.environ](https://docs.python.org/3/library/os.html#os.environ){:target=\_blank}