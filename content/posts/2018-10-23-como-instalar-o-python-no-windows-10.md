---
title: Como instalar o python no Windows 10
date: '2018-10-23'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: python, instalação, windows
image: /images/logo-python.png
---

A instalação do python no Windows 10 é uma das mais simples que já vi.

Para instalar o python 3.7 no Windows,
primeiro você precisa acessar a [página de download do python](https://www.python.org/downloads/){:target=\_blank},
clicar no botão **Download Python 3.7.1** para baixar o instalador.

![Página de download do instalador do Python](/images/como-instalar-python-no-windows-10/pagina-de-download-do-python.png){:width=100%}

Em seguida, você precisa executar o instalador baixado.

A primeira tela do instalador, nos oferece a opção de adicionar o python 3.7 na variável de ambiente **PATH**.

Marcar essa opção significa que o comando `python` poderá ser
executado pela linha de comandos.
Eu já marco essa caixa de seleção para eu não precisar configurar
a variável de ambiente manualmente depois.

Após marcar (ou não) essa opção você pode escolher entre
a instalação personalizada, onde você poderá escolher
quais ferramentas você deseja instalar, ou a opção **Install Now**,
que instala todas as ferramentas, incluindo a IDE **IDLE** e o **pip**, uma ferramenta de instalação de dependências do python.

Indico a opção **Install Now**.

![Instalador do Python - seleção do tipo de instalação](/images/como-instalar-python-no-windows-10/instalador-python-01-selecao-do-tipo-de-instalacao.png){:width=100%}

Pronto! Após clicar em **Install Now** o python será instalado no seu computador.
O instalador pedirá privilégios de administrador para realizar a instalação..

Após a instalação concluir, basta clicar no botão **Close** e acabou!
O python 3.7 já estará instalado no seu Windows.

![Instalador do Python - tela de conclusão da instalação](/images/como-instalar-python-no-windows-10/instalador-python-02-conclusao-da-instalacao.png){:width=100%}

Mais fácil impossível!

Agora vamos verificar se tudo correu bem e o seu python foi instalado corretamente.

Abra o **menu iniciar** e digite `cmd` e execute o **Prompt de comando**.

![Menu iniciar - cmd](/images/como-instalar-python-no-windows-10/menu-iniciar-cmd.png){:width=100%}

No prompt de comando digite `python` e tecle **ENTER**.

Se a sua instalação do python deu certo e você marcou a opção de adicionar o python no **PATH** como eu sugeri,
o prompt do python será aberto apresentando tres caracteres `>>>` indicando que você já pode executar comandos python.

![Prompt do python](/images/como-instalar-python-no-windows-10/prompt-python.png){:width=100%}

Obs: para sair do prompt do python, basta digitar o comando `exit()`.

Qualquer dúvida, poste aí nos comentários!