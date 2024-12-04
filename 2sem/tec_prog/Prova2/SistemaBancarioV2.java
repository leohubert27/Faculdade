import java.util.Date;

// Classe base ContaComum
class ContaComum {
    // Atributos
    protected long nroConta;
    protected Date dtAbertura;
    protected Date dtEncerramento;
    protected int situacao; // 1 = ativa, 2 = encerrada
    protected int senha;
    protected double saldo = 0;

    // Construtor
    public ContaComum(long nroConta, Date dtAbertura, int senha) {
        this.nroConta = nroConta;
        this.dtAbertura = dtAbertura;
        this.situacao = 1; // Conta ativa por padrão
        this.senha = senha;
    }

    // Métodos
    public void deposito(double valor) {
        if (situacao == 1) {
            saldo += valor;
            System.out.println("Depósito de " + valor + " realizado com sucesso.");
        } else {
            System.out.println("Conta encerrada, depósito não permitido.");
        }
    }

    public boolean saque(double valor) {
        if (situacao == 1 && saldo >= valor) {
            saldo -= valor;
            System.out.println("Saque de " + valor + " realizado com sucesso.");
            return true;
        } else {
            System.out.println("Saldo insuficiente ou conta encerrada.");
            return false;
        }
    }

    public Date getDataDeAbertura() {
        return dtAbertura;
    }

    public Date getDataDeEncerramento() {
        return dtEncerramento;
    }

    public boolean conferirSenha(int senha) {
        return this.senha == senha;
    }

    public void encerrarConta() {
        if (situacao == 1) {
            situacao = 2;
            dtEncerramento = new Date();
            System.out.println("Conta encerrada com sucesso.");
        } else {
            System.out.println("Conta já está encerrada.");
        }
    }
}

// Subclasse ContaEspecial
class ContaEspecial extends ContaComum {
    private double limite;

    // Construtor
    public ContaEspecial(long nroConta, Date dtAbertura, int senha, double limite) {
        super(nroConta, dtAbertura, senha);
        this.limite = limite;
    }

    @Override
    public boolean saque(double valor) {
        if (situacao == 1 && (saldo + limite) >= valor) {
            saldo -= valor;
            System.out.println("Saque de " + valor + " realizado com sucesso (utilizando limite).");
            return true;
        } else {
            System.out.println("Saldo insuficiente, mesmo com o limite.");
            return false;
        }
    }
}

// Subclasse ContaPoupanca
class ContaPoupanca extends ContaComum {
    private Date dtAniversarioMensal;

    // Construtor
    public ContaPoupanca(long nroConta, Date dtAbertura, int senha, Date dtAniversarioMensal) {
        super(nroConta, dtAbertura, senha);
        this.dtAniversarioMensal = dtAniversarioMensal;
    }

    // Método para aplicar juros mensais
    public void aplicarJurosMensais() {
        if (situacao == 1) {
            saldo += saldo * 0.01; // 1% de juros
            System.out.println("Juros de 1% aplicados. Saldo atual: " + saldo);
        } else {
            System.out.println("Conta inativa. Não é possível aplicar juros.");
        }
    }

    // Getter para data de aniversário mensal
    public Date getDtAniversarioMensal() {
        return dtAniversarioMensal;
    }
}

// Classe principal para teste
public class SistemaBancarioV2 {
    public static void main(String[] args) {
        Date hoje = new Date();

        // Testando Conta Especial
        ContaEspecial contaEspecial = new ContaEspecial(12345, hoje, 1234, 500);
        contaEspecial.deposito(200);
        contaEspecial.saque(600);
        contaEspecial.saque(200);

        // Testando Conta Poupança
        ContaPoupanca contaPoupanca = new ContaPoupanca(54321, hoje, 5678, hoje);
        contaPoupanca.deposito(1000);
        contaPoupanca.aplicarJurosMensais();
        System.out.println("Data de aniversário da conta poupança: " + contaPoupanca.getDtAniversarioMensal());
    }
}

//ATENÇÃO: Utilizando o compilador do próprio VSCode ocorre um ERRO! Para o Código funcionar normalmente, tem que compilar MANUALMENTE

// Para compilar, no terminal colocar esse código: javac SistemaBancarioV2.java
//Para executar, colocar esse código no terminal: java SistemaBancarioV2

