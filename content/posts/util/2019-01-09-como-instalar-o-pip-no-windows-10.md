title: [Resolvido] 'pip' não é reconhecido como um comando interno
date: 2019-01-09
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: pip, instalação, windows
image: /images/logo-python.png

O PIP é um gerenciador e instalador de pacotes do python.

Muitas vezes acontece de você tentar executar o comando pip no seu Windows 10 e receber a mensagem abaixo:

> 'pip' não é reconhecido como um comando interno
ou externo, um programa operável ou um arquivo em lotes.

Mas isso não significa necessariamente que você não tem o PIP no seu computador.

## Pode ser que você já tenha o PIP no seu computador

Se você tem o **python nas versões acima de 2.7.9 para python 2 ou 3.4 para python 3**, você já tem o pip no seu computador, então provavelmente você não precisará instalar o Pip.

Neste caso o que está faltando é configurar a variável de ambiente PATH com o caminho do executável do pip.

Nós já vimos como fazer isso para corrigir o comando do `python`.

[**>> [Resolvido] 'python' não é reconhecido como um comando interno**](https://dicasdepython.com.br/resolvido-python-nao-e-reconhecido-como-um-comando-interno/){:target=\_blank}

Siga os passos do post acima para adicionar na variável de ambiente PATH também a pasta onde está o executável do PIP, que é o mesmo caminho do python, porém na subpasta `Script`.

No meu caso a pasta é essa:

![Adicionando caminho da pasta do executável PIP à variável de ambiente PATH](/images/como-instalar-o-pip-no-windows-10/pasta-com-executavel-pip.png){:style="width:100%; padding:10px;"}

Ou seja, você deve adicionar no seu PATH o valor:

```
C:\...<pasta onde o python está instalado>...\Scripts
```

No meu caso ficou desse jeito.

![Adicionando caminho da pasta do executável PIP à variável de ambiente PATH](/images/como-instalar-o-pip-no-windows-10/variavel-de-ambiente-path-com-pip.png){:style="width:100%; padding:10px;"}

[**>> Veja também: Como instalar o python no Windows 10**](https://dicasdepython.com.br/como-instalar-o-python-no-windows-10/){:target=\_blank}

## Se o seu python não tiver o pip

Se você não estiver utilizando uma versão que já vem com o pip, ou seja, se você tiver o **python em uma das versões abaixo de 2.7.9 para python 2 ou 3.4 para python 3**.
Você precisará executar um procedimento a mais para instalar o pip no seu computador.

Primeiro você deve baixar o arquivo [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py){:target=\_blank} para o seu computador
e em seguida executar ele com o comando python. Assim:

```
python get-pip.py
```

Este script irá instalar o pip no seu computador, bem como o setuptools e o wheel.

Qualquer dúvida, poste aí nos comentários!

## Referências

[1. PYPA installing](https://pip.pypa.io/en/stable/installing/){:target=\_blank}

