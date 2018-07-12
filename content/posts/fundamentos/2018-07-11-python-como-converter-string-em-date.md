title: Python: Como converter string em date
date: 2018-07-11
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: String, date, datetime
image: /images/logo-python.png

Para converter uma string em date em python, basta usar a função `strptime` da classe datetime, para obter um objeto datetime e em seguida, obter o objeto date através da função `date()`.

O código abaixo exemplifica a conversão de duas strings em formatos diferentes em objetos `date`.

```python
from datetime import datetime

str_date = '11/07/2018'

date = datetime.strptime(str_date, '%d/%m/%Y').date()

print(date, type(date))

str_date = '2018-07-11'

date = datetime.strptime(str_date, '%Y-%m-%d').date()

print(date, type(date))
```

Saída:

```
2018-07-11 <class 'datetime.date'>
2018-07-11 <class 'datetime.date'>
```

Referências:

1. [Documentação: datetime](https://docs.python.org/2/library/datetime.html){:target=\_blank}
