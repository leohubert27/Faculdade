const Stack = require('./array-stack')
const Queue = require('./array-queue')

console.log("--------------------------------------- \n")
console.log("Leonardo Hubert | Arthur Davi Gomes \n")
console.log("--------------------------------------- \n")

const pilhaVazia = new Stack();  
let filaCheia = new Queue();      

filaCheia.enqueue(1);  // Adiciona itens na fila
filaCheia.enqueue(2);
filaCheia.enqueue(3);

console.log("Itens da filaCheia:", filaCheia.items); // Exibe os itens da fila [1, 2, 3]

let aux = [...filaCheia.items]; // Cria a variável aux e atribui os valores da fila a ela

// Exibe o conteúdo de aux
console.log("Conteúdo de aux antes de inverter:", aux);  // [1, 2, 3]

// Inverte a ordem dos elementos de aux
aux.reverse();

console.log("Conteúdo de aux depois de inverter:", aux); // [3, 2, 1]

// Remove os itens da fila 
filaCheia.dequeue();  
filaCheia.dequeue();  
filaCheia.dequeue();  

console.log("Itens restantes na filaCheia:", filaCheia.items);  // A fila deve estar vazia agora []

// Adiciona os valores de aux (invertidos) na pilhaVazia (Stack)
aux.forEach(item => pilhaVazia.push(item));

console.log("Itens empilhados na pilhaVazia:", pilhaVazia.items);  // Exibe os itens da pilha [3, 2, 1]

while (!pilhaVazia.isEmpty()) {
    const item = pilhaVazia.pop();  // Remove o item do topo da pilha
    // Para evitar adicionar o array `aux` inteiro à fila, adicionamos os itens individuais
    if (Array.isArray(item)) {
        item.forEach(innerItem => filaCheia.enqueue(innerItem)); // Adiciona os itens do array à fila
    } else {
        filaCheia.enqueue(item);  // Adiciona o item à fila
    }
}

console.log("Itens da filaCheia depois de transferir da pilha:", filaCheia.items);