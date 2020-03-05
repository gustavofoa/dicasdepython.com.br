---
title: 'Python: Como identificar o dia da semana de uma data'
date: '2018-06-29'
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: Data
image: /images/logo-python.png
---

O código abaixo mostra como identificar o dia da semana de uma data em Python

```python
from datetime import date

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

data = date(year=2018, month=6, day=29)
print(data)

indice_da_semana = data.weekday()
print(indice_da_semana)

dia_da_semana = DIAS[indice_da_semana]
print(dia_da_semana)

numero_do_dia_da_semana = data.isoweekday()
print(numero_do_dia_da_semana)
```

Saída:

```
2018-06-29
4
Sexta-feira
5
```

É importante observar que o método `weekday()` da classe `date` retorna o dia da semana como um número inteiro,
onde 0 representa a segunda-feira e 6 representa o domingo.

Podemos também usar o método `isoweekday()` que retorna o dia da semana onde 1 representa segunda-feira e 7 representa domingo.

Referências:

1. [Documentação: datetime](https://docs.python.org/3/library/datetime.html){:target=\_blank}
