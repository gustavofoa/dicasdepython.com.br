---
title: 'Pandas: Como criar um DataFrame vazio'
date: '2018-07-10'
author: Gustavo Furtado de Oliveira Alves
category: Frameworks
tags: Pandas, DataFrame
image: /images/logo-pandas.jpg
---

Para criar um dataframe com o pandas, primeiro nós temos que importar o pandas.

```python
import pandas as pd
```

Agora, podemos criar o nosso dataframe.

```python
df = pd.DataFrame()
df
```

Saída:

```
Empty DataFrame
Columns: []
Index: []
```

Além disso, nós podemos já definir as colunas do nosso dataframe na criação.

```python
COLUNAS = [
    'Coluna-1',
    'Coluna-2',
    'Coluna-3',
    'Coluna-4'
]

df = pd.DataFrame(columns=COLUNAS)
df
```

Saída:

```
Empty DataFrame
Columns: [Coluna-1, Coluna-2, Coluna-3, Coluna-4]
Index: []
```


Referências:

1. [Documentação: DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html){:target=\_blank}
