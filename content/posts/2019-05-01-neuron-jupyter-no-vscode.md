---
title: 'Neuron: Executando jupyter notebook dentro do VS Code'
date: '2019-05-01'
author: Gustavo Furtado de Oliveira Alves
category: Ferramentas
tags: Pandas, jupyter, vscode, plugin
image: /images/logo-vscode.png
---

Se você já trabalhou com _Machine Learning_, muito provavelmente já utilizou
o _Jupyter Notebook_ para executar seu código python.

Entretanto nem todo mundo gosta de escrever código python no browser,
principalmente quem vem do mundo da programação.

Felizmente existe um plugin que combina o poder de uma IDE, como o **Visual Studio Code**, com a interatividade do _Jupyter Notebook_. Este plugin é o **Neuron**.

![Plugin Neuron no VS Code](/images/neuron/neuron.png){:style="width:100%; padding: 10px;"}

O **Neuron** foi desenvolvido por um time de estudantes do _Imperial College London_, em colaboração com a Microsoft no [final do ano passado](https://blogs.msdn.microsoft.com/uk_faculty_connection/2018/10/29/data-science-in-visual-studio-code-using-neuron-a-new-vs-code-extension/){:target=\_blank} (2018) e, basicamente, possibilita executar o seu código _python_ dentro do VS Code como se estivesse em um _Jupyter Notebook_.

## Como instalar o NEURON no VS Code

Primeiro, talvez nem fosse necessário dizer, mas você precisa ter o _jupyter_ instalado no seu ambiente para usar o _neuron_, além de todas as outras bibliotecas que você vai utilizar no seu código, como pandas, matplotlib, numpy, etc.

Se você ainda não tem o _jupyter_ instalado, basta executar o comando abaixo no seu prompt de comandos para instalá-lo.

```
pip install jupyter
```

Com o _jupyter_ instalado, a forma mais fácil de instalar o Neuron é através do _Marketplace_ do próprio VS Code. Veja abaixo como procurar, instalar a extensão Neuron no seu VS Code e usá-la de forma bem simples (para executar você deve abrir a janela do neuron, selecionar o código que você quer executar e pressionar **Alt+Enter**).

![Como instalar o NEURON no VS Code](/images/neuron/instalacao.gif){:style="width:100%; padding: 10px;"}

Depois que o Neuron estiver instalado, aparecerá um ícone de uma "janelinha" no canto superior direito do seu arquivo python aberto, conforme apresentado no _gif_ acima.
Clicando neste ícone, o VS Code abre uma aba à direita do seu código que é onde aparecerá a saída da execução do seu código python.

Caso você não tenha instalada alguma dependência que o neuron necessita como o próprio _jupyter_ ou alguma outra dependência do seu código como o _matplotlib_, o VS Code vai oferecer para instalar a dependência faltante.

## Como usar o Neuron

O básico da utilização do Neuron é:

1. Instale o Neuron
2. Abra (ou crie) um arquivo python (ou R)
3. Clique no ícone do Neuron (janelinha no canto superior direito) para abrir a aba do Neuron
4. Selecione código python que você quer executar.
5. Pressione: **Alt+Enter**

Veja abaixo um exemplo de execução de um código que gera um gráfico no Neuron.

![Exemplo de execução de código no Neuron](/images/neuron/exemplo-execucao.gif){:style="width:100%; padding: 10px;"}

O neuron possui várias ferramentas para interação com os resultados do seu código.
Mostrei no gif acima uma movimentação no gráfico 3D que o código gerou.

Além de gráficos o neuron possúi várias outras ferramentas, ele imprime gráficos 2D e 3D, mapas, visualização de código latex, etc.
Vale a pena começar a usar.

O que você achou do Neuron? Deixe aí nos comentários.

Referências:

1. [Documentação: DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html){:target=\_blank}

2. [Data Science in Visual Studio Code using Neuron, a new VS Code extension](https://blogs.msdn.microsoft.com/uk_faculty_connection/2018/10/29/data-science-in-visual-studio-code-using-neuron-a-new-vs-code-extension/){:target=\_blank}
