title: Python: Como limpar a tela do console
date: 2018-08-03
author: Gustavo Furtado de Oliveira Alves
category: Util
tags: console, system
image: /images/logo-python.png

Para limpar a tela do console com python nós precisamos executar o comando  `clear` utilizando a função `system` da biblioteca padrão `os`.

Além disso, nós podemos forçar o retorno ser "None" para não sobrar um "0" no prompt do python.

Veja no código a seguir.

```python
import os
os.system('clear') or None
```

## Resultado

Veja abaixo a execução deste programa.

![Limpando a tela do console com Python](/images/python-limpar-console.gif){:width=100%}
