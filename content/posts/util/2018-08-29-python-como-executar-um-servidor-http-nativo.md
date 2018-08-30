title: Python: Como executar um servidor HTTP nativo para servir arquivos de uma pasta local
date: 2018-08-29
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: servidor, http
image: /images/logo-python.png

Se você tem vários arquivos de um site em uma pasta e quer servir estes arquivos em um browser com o protocolo `http://` ao invés do protocolo `file:///`, neste post você vai descobrir **como executar um servidor http básico nativo do python**.

O python tem um servidor http nativo que pode ser executado em qualquer pasta do seu sistema operacional.

Mas os comandos são diferente para as duas principais versões do Python, a versão 2.\* e a versão 3.\*.

## Servidor HTTP no Python 3.\*

Para executar um servidor HTTP no python 3.\*, você deve executar o módulo nativo `http.server` passando a porta que você quer usar como argumento.

Veja abaixo o comando para executar o servidor http com o python 3.\*.

```
python -m http.server 8080
```

No exemplo, estamos criando um servidor HTTP na porta 8080.

> O argumento `-m` do python é usado para executar pela linha de comando um módulo que não está localizado na pasta atual.. No nosso caso o módulo `http.server` não está na pasta onde estamos executando o comando.

No gif abaixo você pode ver na prática a execução de um servidor HTTP em uma pasta com o Python 3.

![Exemplo de execução de um servidor HTTP nativo em Python 3](/images/python-http-server.gif){:width=100%}

Também podemos ver no gif que o servidor serve o arquivo `index.html` por padrão, se ele existir na pasta.

## Servidor HTTP no Python 2.*

Na versão 2 você consegue o mesmo servidor executando o módulo nativo `SimpleHTTPServer` passando a porta que você quer usar como argumento.

Veja abaixo o comando para executar o servidor http com o python 2.*.

```
python -m SimpleHTTPServer 8000
```

No exemplo, estamos criando um servidor HTTP na porta 8000.

## Referências

1. [Doc: http.server](https://docs.python.org/3/library/http.server.html#module-http.server){:target=\_blank}
2. [Doc: SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html){:target=\_blank}
3. [Doc: Arg -m](https://docs.python.org/2/using/cmdline.html#cmdoption-m){:target=\_blank}
