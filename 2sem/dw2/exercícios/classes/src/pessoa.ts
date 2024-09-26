export default class Pessoa {
    nome: string
    idade: number
    email: string

    constructor(nome: string, idade: number, email: string) {
        this.nome = nome
        this.idade = idade
        this.email = email
    }

    apresentar() {
        console.log(`Olá, meu nome é ${this.nome}, tenho ${this.idade} anos e meu email é: ${this.email}`)
    }
}

const pessoa = new Pessoa("Jorge", 18, "jorginho@exemplo.com");
pessoa.apresentar();
