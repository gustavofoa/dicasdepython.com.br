---
title: Como criar uma Virtual Env e um arquivo de requirements.txt no Python
date: '2021-11-08'
author: Marcelo Santos de Oliveira
category: Util
tags: 'pip, linha de comando, virtualenv , requirements.txt'
image: /images/logo-python.png
---

Quando começamos a programar em Python, logo percebemos a grande quantidade de bibliotecas que a linguagem possui para resolver os mais variados problemas.

A instalação desses pacotes geralmente é muito fácil, e pode ser feita utilizando um gerenciador de pacotes do Python como pip, `pip install nomedopacote`, porem com uma grande quantidade de pacotes e estes podem ter ainda varias versões diferentes visualizamos um problema, para cada projeto que fizermos teremos que instalar todos os pacotes que serão utilizados nesse projeto de forma global.

Mas esse ainda nem pode ser o maior problema que teríamos, supondo uma aplicação feita em Python 3.7, porem temos instalado a versão do Python 3.8 e assim que tentamos rodar a aplicação localmente ela quebra por incompatibilidade de versões, esse problema também pode acontecer com os pacotes usados nessa aplicação.

Nesse cenário notamos que teríamos que gerenciar varias versões de pacotes e do próprio Python na maquina, o que poderia rapidamente se transformar em uma grande confusão de versões entre projetos, um verdadeiro caos.

## Separando os ambientes com Virtual Env

Para resolver esse problema a solução seria a criação de uma ambiente virtual onde teríamos as versões corretas, dos pacotes instalados e até mesmo a versão correta do Python instalada nesse ambiente e criar um arquivo com todos os pacotes necessários.

Para isso vamos mostrar como criar e ativar uma ***Virtual Env*** que irá rodar tudo que é necessário para o projeto dentro de um ambiente separado do resto do sistema e criar arquivo ***requirements.txt*** para termos todos os pacotes nas versões corretas para rodar o programa.

Tendo o Python instalado no seu sistema operacional, digite o comando `python3 -m venv nome_da_virtual_venv`, no exemplo abaixo eu utilizei o nome venv que é muito utilizado, meu terminal quando coloquei o nome venv, ele indica o nome da pasta como ambiente virtual como veremos mais a frente.

![Comando para criar uma venv](../images/como-criar-uma%20-virtual-env-e-um-arquivo-de-requirements-txt-no-python/img1.png "comando para criar uma venv"){:width=100%}

Agora se listarmos o conteúdo da pasta com o comando ls no linux e dir para o windows, podemos notar que foi criado uma pasta com o nome que definimos na criação da venv.

![Listando conteudo da pasta](../imagnes/../images/como-criar-uma%20-virtual-env-e-um-arquivo-de-requirements-txt-no-python/img2.png "Listando o conteudo da pasta"){:width=100%}

Porem ainda não estamos utilizando o ambiente virtual que acabamos de criar, para isso teremos que executar o arquivo ***activate*** que esta no caminho **venv/bin/activate**.

![Ativando o ambiente virtual](../images/como-criar-uma%20-virtual-env-e-um-arquivo-de-requirements-txt-no-python/img3.png "Ativando o ambiente virtual"){:width=100%}

No windows, o comando é uma pouco diferente, sendo preciso executar o arquivo **activate.bat**, dessa forma o comando para se ativar a venv no windows seria `venv\Scripts\activate.bat`.

Depois de ativado irá indicar que a venv está ativada.

![Indicação da venv ativada](../images/como-criar-uma%20-virtual-env-e-um-arquivo-de-requirements-txt-no-python/img4.png "Indicacao da venv ativada"){:width=100%}

O meu terminal coloca os termos **via nomeDaPasta** indicando que a venv está ativada, isso pode variar um pouco, sendo indicado por (nome_da_venv).

Pronto agora estamos com o ambiente virtual em Python criado e ativado, já podemos instalar os pacotes necessários sem precisar fazer uma instalação global. Para a instalação pode utilizar o gerenciador de pacotes de sua preferência, nas imagens a seguir eu criei um segundo ambiente virtual e realizei a instalação do pacote Pillow que é utilizado para manipulação de imagens, notem que fiz a instalação de versões diferentes uma em cada venv sem que houvesse problema.

![Versões diferentes para ambientes diferentes](../images/como-criar-uma%20-virtual-env-e-um-arquivo-de-requirements-txt-no-python/img6.png "Versoes diferentes para ambientes diferentes"){:width=100%}

## Salvando as dependencias com requirements.txt

Pois bem mas ainda temos um problema, depois de instalado todos os pacotes necessários para a sua aplicação, assim que fizer um push para o github gostaríamos que quem fizer um clone do projeto não tenha que instalar todas as dependências manualmente, ou pior, ter que saber qual é exatamente a versão utilizada do pacote a ser instalado. O gerenciador de pacotes *pip* nos traz uma solução pra isso, onde criaremos um arquivo *requirements.txt* para deixar disponível as dependências necessárias para que o seu projeto rode.

Para criarmos o arquivo *requirements.txt* já com todas as dependências do ambiente é bem simples, precisamos apenas do comando  `pip freeze > requirements.txt`.

![Criando o arquivo requirements.txt](../images/como-criar-uma%20-virtual-env-e-um-arquivo-de-requirements-txt-no-python/img7.png "Criando o arquivo requirement.txt"){:width=100%}

Pronto, agora já temos o arquivo como os pacotes que são utilizados no projeto, informando também as versões que foram utilizadas.

![Arquivo de controle de pacotes](../images/como-criar-uma%20-virtual-env-e-um-arquivo-de-requirements-txt-no-python/img8.png){:width=100%}

Agora se outro desenvolvedor for rodar o projeto, ele pode utilizar o comando `pip install -r requirements.txt` que o gerenciador de pacotes cuidará de baixar e instalar as versões corretas de todos os pacotes que foram utilizados no sistema.

