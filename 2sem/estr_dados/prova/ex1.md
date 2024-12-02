1 - Uma Binary Search Tree, ou Árvore Binária de Busca é um tipo de estrutura de dados que organiza seus elementos de maneira hierarquica, o que acaba facilitando muito algumas operações como busca, inserção e remoção de dados. Cada nó dessa árvore possui apenas dois filhos (por isso o termo "árvore binária"), e deve obedecer uma propriedade:
    - Para o nó da árvore de valor X:
        1- Os valores de todos os nós da subárvore a esquerda devem ser MENORES do que X
        2- Os valores de todos os nós da subárvore a direita devem ser MAIORES do que X

As principais operações são, como mencionadas previamente: 

- Busca: A busca começa na raiz e decide, com base no valor de busca se irá continuar à esquerda (caso o valor seja menor que o nó) ou a direita (caso o valor seja maior que o nó)
- Inserção: Um novo valor é colocado como uma folha em um local apropriado, seguindo a propriedade da árvore binária.
- Remoção: A remoção envolve três casos principais:
    1- Onde o nó é uma folha (não há filhos): É simplesmente removido'
    2 - Onde o nó possui um único filho: O filho irá substituir o nó que foi removido;
    3 - Onde o nó tem dois filhos: Nesse caso substitui-se o nó pelo menor valor da subárvore direta, ou o maior da esquerda.