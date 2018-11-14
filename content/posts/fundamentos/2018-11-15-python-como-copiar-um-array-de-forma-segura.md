title: Python: Como copiar um array/list de forma segura
date: 2018-11-15
author: Gustavo Furtado de Oliveira Alves
category: Fundamentos
tags: array
image: /images/logo-python.png

Muito cuidado quando for copiar um array/list em python, pois você pode provocar um grande problema no seu código.

Se você simplesmente copiar atribuir a variável de um array para outra variável,
as alterações que você fizer na segunda variável serão realizadas também na primeira.
Veja um exemplo:

```python
a = [1,2,3]
b = a
b[0] = 4
```

Você, pode até achar que alterou só o array da variável `b`,
mas na verdade o array da variável `a` também foi alterado.
Veja a execução desse código imprimindo o valor das variáveis `a` e `b`.

![Copiando array de forma insegura](/images/copiar-array-seguramente/copiando-mesmo-array.gif){:width=100%}

Perceba que a alteração no array da variável `b` (`b[0] = 4`)
teve impacto também no array da variável `a`.

Existe várias formas de copiar um array de forma segura em python, onde a alteração em um não impacta no outro
e eu vou mostrar 5 delas mais a frente.

Mas se quiser uma resposta rápida sobre como fazer essa cópia basta usar a função `copy()` do array, assim:

```python
b = a.copy()
```

Entretanto acho que você merece uma explicação mais aprofundada sobre o que acontece por baixo dos panos.

## O que acontece por baixo dos panos

Vamos pegar o nosso exemplo acima para entender o que acontece quando criamos um array.

Quando criamos um array e atribuimos à uma variável, por exemplo `a = [1,2,3]`,
o python cria um objeto na memória e atribui o endereço desse objeto à variável.
Pensa em algo assim:

![Criação de objeto array e atribuição de endereço à variável a](/images/copiar-array-seguramente/objeto-array-endereco-variavel.png){:width=100%}

Quando copiamos uma variável para outra, o que estamos copiando é o valor da variável, nesse caso o endereço.

Então, quando fazemo a atribuição `b = a`, estamos copiando o valor da variável `a` para a variável `b`.

Mais ou menos assim.

![Copiando o endereço de um array para outra variável](/images/copiar-array-seguramente/copia-endereco-para-outra-variavel.png){:width=100%}

Ou seja, **copiamos endereço para o mesmo objeto array**!

Isso significa que se fizermos uma alteração no objeto array em qualquer uma das variáveis,
estaremos alterando o mesmo objeto. Por isso acontece o exemplo que mostrei no inicio.

Então, o que precisamos fazer é uma cópia do objeto array e atribuir o endereço desse novo objeto para a outra variável.
Mais ou menos assim:

![Copiando o objeto array e atribuindo o novo endereço a outra variável](/images/copiar-array-seguramente/copiando-objeto-array.png){:width=100%}

Dessa forma as alterações feitas no objeto de uma das variáveis não impacta o outro objeto.

Existem várias formas de fazer isso, como o método `copy()`.

## 4 formas de copiar um objeto array

Como já disse a forma mais simples de copiar um objeto array é através do método `copy`.

## 1 - Método _copy()_ da classe Array

Perceba no exemplo abaixo que fizemos a cópia do objeto array da variável `a` e atribuimos esse novo objeto à variável `b` (`b = a.copy()`) e alteração `b[0] = 4` não alterou o array de `a`, somente o array de `b`.

![Copiando o objeto array e atribuindo o novo endereço a outra variável](/images/copiar-array-seguramente/copiando-array-metodo-copy.gif){:width=100%}

## 2 - Fazendo um filtro trazendo todos os itens de um array com [:]

Uma outra ideia é fazer um filtro no array original trazendo todos os registros assim: `b = a[:]`.

Isso cria um outro objeto array com o resultado do filtro, que nesse caso é _todos os registros_.
Veja:

![Copiando o objeto array através do filtro [:]](/images/copiar-array-seguramente/copiando-array-atraves-de-filtro.gif){:width=100%}

## 3 - Utilizando o construtor _list(<list>)

Neste post estou chamando _list_ do python de array para manter a linguagem comum com outras linguagens de programação,
visto que o modo literal com colchetes (exemplo [1,2,3]) cria um objeto do tipo _list_.

Mas em python um objeto _array_ é um pouco diferente de um objeto _list_.
Vou aprofundar na diferença entre eles em outro post.

Agora que você descobriu que o que vc achava que era um _array_ na verdade é um objeto _list_ (=P),
você pode criar um novo objeto utilizando o construtor da classe _list_ passando o objeto atual como parâmetro.
Ou seja `b = list(a)`.

Veja o resultado, vou aproveitar o gif pra mostrar o resultado de `type([1,2,3])`:

![Copiando o objeto array com o construtor list(<list>)](/images/copiar-array-seguramente/copiando-array-com-construtor-list.gif){:width=100%}

## 4 - Utilizando a biblioteca _copy_

Por fim, também podemos importar o pacote `copy` e utilizar a função também de nome `copy`. Assim:

```python
a = [1,2,3]
import copy
b = copy.copy(a)
```

O resultado é o mesmo, ou seja, copiamos o objeto _list_ e não só o valor da variável `a`. Veja:

![Copiando o objeto array com o método copy.copy()](/images/copiar-array-seguramente/copiando-array-com-metodo-copy.gif){:width=100%}




Referências:

1. [Doc: getattr](https://docs.python.org/3/library/functions.html#getattr){:target=\_blank}
