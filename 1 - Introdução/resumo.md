

## Pesquisa Binária

    Vamos supor que estamos na era jurássica e você precisa procurar o nome de uma pessoa numa agenda telefônica. O nome começa com K, como você irá buscar esse nome na agenda? Começando da primeira página ou começando da metade da agenda? (já que o K é perto da metade)

Isso se chama <b>Pesquisa Binária</b>, um algoritmo onde a entrada é uma lista ordenada de elementos, e se o elemento desejado estiver na lista, ele retorna a localização dele, caso contrário retorna <i>None</i>. A pesquisa binária pega a metade da lista e verifica se o elemento desejado está antes ou depois da metade, se tiver antes, descarta tudo depois da metade e realiza essa lógica até achar o item. (1)

## Notação Big O

Entre a pesquisa simples e a Binária, se a simples verifica 100 elementos em 100ms e a binária em 7ms, é certo dizer que a pesquisa binária é quase 15x mais rápida que a simples? <b>NÃO!</b> Pois se aumentarmos o número de itens para 1 bilhão de elementos, a simples levará 11 dias para ler, enquanto a binária levará 32ms. Sensacional!

    Logo, conforme a lista de elementos aumenta, a pesquisa binária se mostra muito mais eficiente que a simples. Não compare algoritmos apenas por velocidade, mas leve também em consideração o crescimento da amostra utilizada.

É aí que entra a notação <b>Big O</b>, nela os segundos (tempo) não existe, apenas a quantidade de operações. Ou seja, ela compara a quantidade de operações entre dois algoritmos de acordo com o crescimento. Ela informa o quão rápido um algoritmo cresce.

- Se na pesquisa binária, precisa-se de log n (na base 2) operações, então o tempo de execução da notação Big O será de O(log n).

- A notação Big O leva em conta o pior caso (o caso que mais irá demorar) e o caso médio

## Principais Pontos

1) A rapidez de um algoritmo não é medida em segundos, mas sim pelo crescimento do número de operações
2) O tempo de execução em algoritmos é expresso na notação Big O
3) O(log n) é mais rápido que O(n) ou O(2 * log n), e isso fica mais visível quando a lista aumenta.



