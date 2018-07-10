title: Pandas: Como criar um DataFrame vazio
date: 2018-07-10
author: Gustavo Furtado de Oliveira Alves
category: Frameworks
tags: Pandas, DataFrame
image: /images/logo-pandas.jpg

O código abaixo mostra como criar um dataframe vazio utilizando o Pandas.

```python
import pandas as pd

COLUNAS = [
    'Coluna-1',
    'Coluna-2',
    'Coluna-3',
    'Coluna-4'
]

df = pd.DataFrame(columns=COLUNAS)

print(df)
```

Saída:

```
Empty DataFrame
Columns: [Coluna-1, Coluna-2, Coluna-3, Coluna-4]
Index: []
```

Referências:

1. [Documentação: DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html){:target=\_blank}
