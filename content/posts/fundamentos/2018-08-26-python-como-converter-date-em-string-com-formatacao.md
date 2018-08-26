title: Python: Como converter date em string com formatacao
date: 2018-08-26
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: String, date, formatação
image: /images/logo-python.png

Para converter um objeto date em em python, basta usar a função `strftime` da classe `datetime.date`.

O código abaixo exemplifica a conversão de uma data para string no formato mais utilizado no Brasil, ou seja `99/99/9999`.

> **Importante**: Vamos usar uma data qualquer baseado [neste outro post aqui].(https://dicasdepython.com.br/python-como-converter-string-em-date/){:target=\_blank}.

```python
from datetime import date, datetime

data = datetime.strptime('26/08/2018', '%d/%m/%Y').date()

print(data)

dataFormatada = data.strftime('%d/%m/%Y')

print(dataFormatada)
```

Saída:

```
2018-08-26
26/08/2018
```

Perceba que quando mandamos imprimir o objeto `data` na tela, o resultado foi uma formatação padrão do python `9999-99-99`,
isso porque o objeto `data` é do tipo `datetime.data`.

Mas quando mandamos imprimir o objeto `dataFormatada` na tela, o resultado foi uma data com o formato que pedimos,
isso porque o objeto `dataFormatada` é uma `string` e recebeu o resultado do método `strftime(%d/%m/%Y)` do objeto `data`.

Veja um exemplo de execução deste código:

![Como converter date em string em Python](/images/python-format-date-em-string.gif){:width=100%}

## Outros formatos

Você também pode converter um objeto `date` em `string` usando outros formatos de data.
Para isso você precisa conhecer os formatos de data disponíveis no python.
Para ver todas as possibilidades de formatação de datas no python [clique aqui](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior){:target=\_blank}.

Referências:

1. [Documentação: datetime](https://docs.python.org/3/library/datetime.html){:target=\_blank}
