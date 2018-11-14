title: Python: Como acessar os atributos de objeto da mesma forma como em um dicionário.
date: 2018-11-14
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: dict, object
image: /images/logo-python.png

Se você já trabalhou com dicionários em python, provavelmente já acessou seus atributos através de strings entre colchetes. Por exemplo:

```python
t = { 'a' : 5 }
t['a']
```

Isso resulta na saída abaixo.

![Acessando o atributo de um dicionário com colchetes em python](/images/como-acessar-atributo-classe-como-dict/acessando-atributo-dict.png){:width=100%}

Ou seja, sem problemas, com _dict_ nós conseguimos acessar um atributo através dos colchetes, passando o nome do atributo como string, assim: `t['a']`

Mas esta forma de acesso não funciona para objetos ou seja, instancias de classes. Veja o exemplo abaixo:

```python
class Teste:
    a = 5
t['a']
```

Nós conseguimos acessar o atributo `a` através do ponto `t.a`, mas não conseguimos através dos colchetes `t['a']`.
Acontece o erro `object is not subscriptable`, como podemos ver na imagem abaixo.

![Erro ao acessar atributo de uma classe com colchetes em python](/images/como-acessar-atributo-classe-como-dict/erro-ao-acessar-atributo-de-objecto-colchetes.png){:width=100%}

Isso implica que não conseguimos acessar um atributo de um object dinamicamente utilizando colchetes. 
Mas tem solução!

## Como acessar atributos de um objeto através de strings

Se tivermos uma string com o nome do atributo do objeto, conseguimos acessar esse atributo através da função `getattr` nativa do python.

Essa função tem o mesmo efeito que os colchetes nos dicionários.

O exemplo abaixo mostra como utilizar a `getattr`.

```python
class Teste:
    a = 5
getattr(t, 'a')
```

Veja este exemplo funcionando na prática.

![Exemplo de utilização da função getattr para obter o atributo de um objeto através de uma string](/images/como-acessar-atributo-classe-como-dict/exemplo-getattr.gif){:width=100%}

## Como alterar atributos de um objeto através de strings

Também conseguimos alterar o valor do atributo, mas aí precisamos usar a função `setattr`,
passando o novo valor do atributo como terceiro parâmetro. Assim:

```python
class Teste:
    a = 5
setattr(t, 'a', 6)
```

Veja este exemplo funcionando na prática.

![Exemplo de utilização da função setattr para alterar o atributo de um objeto através de uma string](/images/como-acessar-atributo-classe-como-dict/exemplo-setattr.gif){:width=100%}

E aí, gostou da dica? Se tiver alguma dúvida poste aí nos comentários!

Referências:

1. [Doc: getattr](https://docs.python.org/3/library/functions.html#getattr){:target=\_blank}
