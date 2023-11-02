class conta_bancaria:
    def __init__(self,numero,saldo,nome,tipo,status,limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = 0

        self.ativado = False
        self.desativado = False

    def depositar(self,qtd):
        if self.ativado == True:
            self.saldo = int(self.saldo) + int(qtd)
            print(f'Você depositou {qtd} reais. Saldo atual: {self.saldo}')
            self.limite += int(self.saldo)
        else:
            print(f'Primeiro ative sua conta!')

    def sacar(self,valor):
        if self.ativado == True:

            if int(valor) <= self.saldo:
                self.saldo = self.saldo - int(valor)
                print(f'Você sacou {valor} reais. ')
            else:
                print('Saldo insuficiente!')
        else:
            print(f'Primeiro ative sua conta!')


    def ativar_conta(self):
        if self.ativado == True:
            print('A conta está ativada!')
        else:
            print('Conta foi ativada!')
            self.ativado = True

    def desativar_conta(self):

        if self.saldo == 0:
            if self.desativado == True:
                print(f'Conta está desativada!')
            else:
                print(f'Conta foi desativada!')
                self.desativado = True
        else:
            print('Não é possível desativar uma conta com saldo!')


    def verificar_saldo(self):
        if self.ativado == True:
            print(f'O seu saldo atual é {self.saldo}')
        else:
            print(f'Primeiro ative sua conta!')

    def verificar_limite(self):
        if self.ativado == True:
            print(f'O seu limite atual é: {self.limite}')
        else:
            print('Primeiro ative sua conta!')