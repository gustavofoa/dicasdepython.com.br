title: [Resolvido] 'pip' não é reconhecido como um comando interno
date: 2019-07-10
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: pip, linha de comando, variável de ambiente, erro
image: /images/logo-python.png

Quando estamos começando a aprender python, depois que
[instalamos o python](https://dicasdepython.com.br/como-instalar-o-python-no-windows-10/){:target=\_blank}
e estamos aptos a criar os nossos promeiros scripts,
o próximo passo é utilizar bibliotecas externas.

Neste momento nós conhecemos o **pip**, que é um gerenciador de pacotes muito útil
que por padrão já vem instalado com o python, mas se não estiver instalado veremos neste post como instalá-lo.

Usar o **pip** para instalar pacotes é muito simples. Basta digitar `pip install <nome-do-pacote>`
no prompt de comandos, que ele baixa e instala o pacote que você pediu.

Entretanto, pode acontecer que mesmo com o python instalado no seu computador,
o pip não esteja configurado corretamente. 
E quando você tenta executar o comando `pip` no prompt de comando e apareça o seguinte erro:

>'pip' não é reconhecido como um comando interno
ou externo, um programa operável ou um arquivo em lotes.

!['pip' não é reconhecido como um comando interno ou externo, um programa operável ou um arquivo em lotes.](/images/variavel-de-ambiente/pip-nao-e-reconhecido.png){:width=100%}

Não se apavore, tem solução!

## Primeiro: Diagnóstico

Este problema pode ter várias causas, mas primeiro precisamos verificar se o pip está instalado.
Pois, mesmo o pip sendo instalado por padrão junto com o python,
pode ser que no momento da instalação, tenha-se optado pela NÃO INSTALAÇÃO DO PIP.

Então a primeira coisa que você precisa fazer é verificar se o pip está instalado.

Para isso você precisa navegar até a pasta de instalação do seu python e dentro dela acessar a pasta `Scripts`.

No meu caso este é o caminho: `C:\Users\gustavo\AppData\Local\Programs\Python\Python37-32\Scripts`

No seu caso o caminho pode ser diferente, dependerá o caminho que você escolheu no momento da [instalação do python](https://dicasdepython.com.br/como-instalar-o-python-no-windows-10/){:target=\_blank}.

Na pasta de `Scripts` você precisa confirmar que existe o arquivo executável do pip, o `pip.exe`.

![Arquivo 'pip.exe' na pasta Scripts](/images/variavel-de-ambiente/pip-na-pasta-scripts.png){:width=100%}

Se o arquivo estiver nesta pasta, ótimo! Isso significa que você já tem o pip, só precisa adicionar esta pasta na variável de ambiente **PATH** para que o prompt de comandos reconheça este comando em qualquer pasta que você o esteja executando.

Já expliquei como fazer isso [neste outro post aqui](/resolvido-python-nao-e-reconhecido-como-um-comando-interno/){:target=\_blank}, mas vamos ver denovo pra reforçar o aprendizado...

Veja passo a passo como adicionar o caminho de uma pasta no **PATH**:

### 1. Clique com o botão direito do mouse no ícone do seu computador e clique em **Propriedades**.

![menu: propriedades do computador](/images/variavel-de-ambiente/meu-computador-propriedades.png){:width=100%}

### 2. Clique em **Configurações avançadas do sistema**.

![Configurações avançadas do sistema](/images/variavel-de-ambiente/configuracoes-avancadas-do-sistema.png){:width=100%}

### 3. Clique no botão **Variáveis de ambiente** dentro da aba **Avançado**.

![Configurações avançadas do sistema](/images/variavel-de-ambiente/botao-variaveis-de-ambiente.png){:width=100%}

### 4. Selecione a variável de ambiente **PATH** na lista e clique em **Editar**.

![Editar variável de ambiente PATH](/images/variavel-de-ambiente/edicao-variavel-de-ambiente-PATH.png){:width=100%}

### 5. Clique no botão **Novo** e adicione o caminho da pasta desejada. No nosso caso, é a pasta Scripts que está dentro da pasta de instalação do Python.

![Adicionando a pasta Scripts do python na variável de ambiente PATH](/images/variavel-de-ambiente/adicionar-pasta-scripts-do-python-no-path.png){:width=100%}

> **Importante**: Pode ser que na sua versão do Windows esta janela seja diferente, apresentando apenas um campo de texto com vários caminhos de pastas separadas por **ponto-e-vírgula (;)**. Neste caso, o que você precisa fazer é justamente **adicionar outro ponto-e-vírgula (;) e o caminho da nova pasta** que você deseja incluir no PATH.

### 6. REINICIE o prompt de comando!

Um passo muito importante que muitos esquecem.
Você precisa reiniciar o prompt de comandos para que as alterações de variáveis de ambiente sejam aplicadas.

### 7. Comando 'pip' funcionando normalmente

![Comando 'pip' funcionando normalmente no prompt de comandos](/images/variavel-de-ambiente/comando-pip-funcionando.png){:width=100%}

## Instalação do pip no Windows

Uma situação que pode acontecer é o pip não estar instalado no com o windows.
Ou seja, você não encontrou o executável do pip naquela pasta de Scripts que fica dentro da pasta de instalação do python.

Neste caso você precisa instalar o pip alí. E pra isso a gente usa o próprio python.
Vejamos então o **passo-a-passo para instalar o pip** no seu Windows.

### 1. Baixe o script get-pip.py para o seu computador

[**>> Clique aqui para baixar o script get-pip.py**](https://bootstrap.pypa.io/get-pip.py){:target=\_blank}

> Se o script só abrir no seu browser, pressione **Ctrl+S** para salvá-lo no seu computador.

### 2. Abra o prompt de comandos e navegue até a pasta onde você salvou o get-pip.py

### 3. Execute o seguinte comando.

```
python get-pip.py
```

O script executará parecido com a tela abaixo.

![Comando 'python get-pip.py'](/images/variavel-de-ambiente/python-get-pip.png){:width=100%}

[> Se tiver problemas com o python confira este post](/resolvido-python-nao-e-reconhecido-como-um-comando-interno/){:target=\_blank}

Pronto, após esse comando o pip já foi instalado e adicionado na sua variável de ambiente **PATH** e já deve estar funcionando.

Para testar basta tentar instalar uma biblioteca, no exemplo abaixo eu executei o pip para instalar a biblioteca **jupyter**

![Comando 'pip' funcionando normalmente no prompt de comandos](/images/variavel-de-ambiente/comando-pip-funcionando.png){:width=100%}

Espero que este post tenha ajudado.

Se você tiver alguma dúvida, poste aí nos comentários.