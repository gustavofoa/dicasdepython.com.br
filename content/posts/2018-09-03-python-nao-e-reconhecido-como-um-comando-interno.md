---
title: '[Resolvido] 'python' não é reconhecido como um comando interno'
date: '2018-09-03'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: python, linha de comando, variável de ambiente, erro
image: /images/logo-python.png
---

Pode acontecer de depois que você instalar o python no seu computador,
você tente executar o comando `python` na linha de comando e apareça o seguinte erro no Windows:

>'python' não é reconhecido como um comando interno
ou externo, um programa operável ou um arquivo em lotes.

!['python' não é reconhecido como um comando interno ou externo, um programa operável ou um arquivo em lotes.](/images/variavel-de-ambiente/python-nao-e-reconhecido.png){:width=100%}

Não se apavore, a solução para isso é fácil!

## A solução

Basta você colocar o caminho da instalação do python na variável de ambiente `PATH` e **reiniciar o prompt de comando**.

Veja passo a passo como fazer essa configuração:

### 1. Clique com o botão direito do mouse no ícone do seu computador e clique em **Propriedades**.

![menu: propriedades do computador](/images/variavel-de-ambiente/meu-computador-propriedades.png){:width=100%}

### 2. Clique em **Configurações avançadas do sistema**.

![Configurações avançadas do sistema](/images/variavel-de-ambiente/configuracoes-avancadas-do-sistema.png){:width=100%}

### 3. Clique no botão **Variáveis de ambiente** dentro da aba **Avançado**.

![Configurações avançadas do sistema](/images/variavel-de-ambiente/botao-variaveis-de-ambiente.png){:width=100%}

### 4. Selecione a variável de ambiente **PATH** na lista e clique em **Editar**.

![Editar variável de ambiente PATH](/images/variavel-de-ambiente/edicao-variavel-de-ambiente-PATH.png){:width=100%}

### 5. Clique no botão **Novo** e adicione o caminho da pasta de instalação do python.

![Adicionando a pasta do python na variável de ambiente PATH](/images/variavel-de-ambiente/adiciona-python-no-PATH.png){:width=100%}

> **Importante**: Pode ser que na sua versão do Windows esta janela seja diferente, apresentando apenas um campo de texto com vários caminhos de pastas separadas por **ponto-e-vírgula (;)**. Neste caso, o que você precisa fazer é justamente **adicionar outro ponto-e-vírgula (;) e o caminho da nova pasta** que você deseja incluir no PATH.

### 6. REINICIE o prompt de comando!

Um passo muito importante que muitos esquecem.
Você precisa reiniciar o prompt de comandos para que as alterações de variáveis de ambiente sejam aplicadas.

### 7. Comando 'python' funcionando normalmente

![Comando 'python' funcionando normalmente no prompt de comandos](/images/variavel-de-ambiente/python-funcionando.png){:width=100%}

Se você tiver alguma dúvida, poste aí nos comentários.