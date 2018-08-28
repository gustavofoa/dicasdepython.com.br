title: Python: Como converter uma string JSON em um dicionário
date: 2018-08-28
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: string, json, converter
image: /images/logo-python.png

Suponha que você tenha uma String que representa um JSON válido e queira transformar esta String em um objeto (dicionário) no Python.

Para fazer isso, basta utilizar o método `json.loads(texto)` da biblioteca `json`.

Veja um exemplo no código abaixo:

```javascript
import json

texto = '{"atributo1": "valor 1", "atributo2": 23}'

objeto = json.loads(texto)

print(objeto['atributo1'])
```

Abaixo um exemplo de execução deste código no prompt do python.

![Exemplo de conversão de uma string em um objeto json em Python](/images/converte-string-para-json-em-python.gif){:width=100%}

## Referências

1. [Doc: json.loads](https://docs.python.org/3/library/json.html#json.loads){:target=\_blank}
