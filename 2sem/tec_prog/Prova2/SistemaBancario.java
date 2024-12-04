import java.util.Date;

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

    public Date dataDeAbertura() {
        return dtAbertura;
    }

    public Date dataDeEncerramento() {
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

class ContaEspecial extends ContaComum {
    // Atributo específico
    private double limiteConta;

    // Construtor
    public ContaEspecial(long nroConta, Date dtAbertura, int senha, double limiteConta) {
        super(nroConta, dtAbertura, senha);
        this.limiteConta = limiteConta;
    }

    @Override
    public boolean saque(double valor) {
        if (situacao == 1 && (saldo + limiteConta) >= valor) {
            saldo -= valor;
            System.out.println("Saque de " + valor + " realizado com sucesso (usando limite especial).");
            return true;
        } else {
            System.out.println("Saldo insuficiente, mesmo com limite especial.");
            return false;
        }
    }
}

class ContaPoupanca extends ContaComum {
    // Atributo específico
    private Date dtAniversario;

    // Construtor
    public ContaPoupanca(long nroConta, Date dtAbertura, int senha, Date dtAniversario) {
        super(nroConta, dtAbertura, senha);
        this.dtAniversario = dtAniversario;
    }

    public Date getDtAniversario() {
        return dtAniversario;
    }
}

// Classe para testar
public class SistemaBancario {
    public static void main(String[] args) {
        Date hoje = new Date();

        // Criando uma ContaComum
        ContaComum contaComum = new ContaComum(12345, hoje, 1234);
        contaComum.deposito(500);
        contaComum.saque(200);
        contaComum.encerrarConta();

        // Criando uma ContaEspecial
        ContaEspecial contaEspecial = new ContaEspecial(54321, hoje, 5678, 1000);
        contaEspecial.deposito(300);
        contaEspecial.saque(1200);

        // Criando uma ContaPoupanca
        ContaPoupanca contaPoupanca = new ContaPoupanca(67890, hoje, 9876, hoje);
        contaPoupanca.deposito(1000);
        System.out.println("Data de aniversário da conta poupança: " + contaPoupanca.getDtAniversario());
    }
}
