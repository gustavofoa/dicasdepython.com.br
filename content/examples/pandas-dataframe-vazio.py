import pandas as pd

COLUNAS = [
    'Coluna-1',
    'Coluna-2',
    'Coluna-3',
    'Coluna-4'
]

df = pd.DataFrame(columns=COLUNAS)

print(df)