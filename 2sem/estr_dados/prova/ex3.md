Código relacionado ao exercício 3 da prova (pode ser encontrado no arquivo BinarySearchTree.js)

class Node {
    constructor(key) {
        this.key = key;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(key) {
        const newNode = new Node(key);
        if (this.root === null) {
            this.root = newNode;
        } else {
            this.#insertNode(this.root, newNode);
        }
    }

    #insertNode(node, newNode) {
        if (newNode.key < node.key) {
            if (node.left === null) {
                node.left = newNode;
            } else {
                this.#insertNode(node.left, newNode);
            }
        } else {
            if (node.right === null) {
                node.right = newNode;
            } else {
                this.#insertNode(node.right, newNode);
            }
        }
    }

    inOrderTraverse(node) {
        if (node !== null) {
            this.inOrderTraverse(node.left);
            console.log(node.key);
            this.inOrderTraverse(node.right);
        }
    }

    // Outros métodos omitidos para brevidade
}

// Cria uma nova instância da árvore binária de busca
const tree = new BinarySearchTree();

// Lista de nomes de alunos
const alunos = [
    "LEONARDO VINÍCIUS G. HUBERT",
    "WILLIAM SILVA DOS REIS",
    "JOAO VITOR F. M. ROCHA",
    "CAIO HENRIQUE F. DE SOUZA",
    "ERIC VINICIUS DA S. MENEGON",
    "DANIEL GALVAO M. DA SILVA",
    "GIOVANI DE BIAGI ALVES",
    "VITOR CARDOSO DA CRUZ",
    "GUSTAVO SILVA DE CARVALHO",
    "HOSANA AZEVEDO PIRES",
    "NATHAN FERRACINI BATISTA",
    "JOAO PEDRO SOUZA SILVA",
    "DANIEL BRITO DA SILVA JUNIOR",
    "ARTHUR DAVI GOMES",
    "ROBSON ALAN MANTOVANI",
    "MARCELO HENRIQUE REDUZINO",
    "ADRIANO DOS SANTOS",
    "MATHEUS HENRIQUE A. V. NEVES",
    "PEDRO HENRIQUE B. SANTOS",
    "RAMON GODINHO",
    "GRAZIELLA SOUZA",
    "RODRIGO MORAES DE S. GARCIA",
    "BRUNO HENRIQUE Q. GARCIA"
];


alunos.forEach(nome => tree.insert(nome));


console.log("Percurso in-order (inOrderTraverse):");
tree.inOrderTraverse(tree.root);
