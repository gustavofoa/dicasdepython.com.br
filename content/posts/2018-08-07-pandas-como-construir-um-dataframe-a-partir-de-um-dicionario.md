---
title: 'Pandas: Como construir um DataFrame a partir de um dicionário'
date: '2018-08-07'
author: Gustavo Furtado de Oliveira Alves
category: Frameworks
tags: Pandas, DataFrame
image: /images/logo-pandas.jpg
---

Há muitas formas de criar dataframes do pandas e já falamos aqui sobre
[como criar um DataFrame vazio](https://dicasdepython.com.br/pandas-como-criar-um-dataframe-vazio/){:target=\_blank}.

Vamos ver neste post como criar um dataframe a partir de um dicionário (objeto).

Primeiro temos que importar a biblioteca pandas para criar o nosso dataframe.

```python
import pandas as pd
```

Agora, vamos criar um objeto dicionário de exemplo.

```python
obj = {'col1': [1, 2], 'col2': [3, 4]}
```

Com o objeto podemos criar o dataframe passando-o como parâmetro `data`.

```python
df = pd.DataFrame(data=obj)
df
```

Saída:

```
   col1  col2
0     1     3
1     2     4
```

**Importante!** Repare que as chaves do dicionário definem as colunas do dataframe.

Referências:

1. [Documentação: DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html){:target=\_blank}
