

# Como funciona a memória

    O computador possui várias "gavetas" (slot), e cada uma delas com seu endereço. Cada vez que você pede espaço para o computador, ele te dará um endereço no qual você possa armazenar seu item. Se quiser guardar múltiplos itens, existem duas maneiras de fazer isso: array e listas.

## Array:
- Tudo dentro de um array está localizado sequencialmente na memória, um do lado do outro. Ou seja, se você está no primeiro elemento, você sabe que pra chegar no quarto, você só precisa "somar 3" ao endereço do primeiro. Não precisou passar pelo segundo nem terceiro item.

### Tempo de Execução
- Leitura -> O(1)
- Inserção -> O(n)
- Deleção -> O(n)

## Listas encadeadas:
- Tudo dentro da lista encadeada não estará, necessariamente, em sequencia na memória. Cada item, além de seu valor, terá o endereço do próximo item, o quarto item tem o endereço do quinto item. Ou seja, se você quer o último item da lista, terá que passar por todos elementos.

### Tempo de Execução
- Leitura -> O(n)
- Inserção -> O(1)
- Deleção -> O(1)

## Qual o melhor?

Depende! Depende do propósito e o dinamismo que você pretende fazer com esse array/lista. Porém, o mais comum é o array por que ele permite a busca aleatória, ou seja, pra chegar no quinto elemento não é necessário passar pelos 4 primeiros.
