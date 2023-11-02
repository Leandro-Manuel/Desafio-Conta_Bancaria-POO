from biblioteca import *

conta_bancaria1 = conta_bancaria("123456","0","Leandro", "Conta salário","ativos","100")

conta_bancaria1.ativar_conta()
conta_bancaria1.depositar("100")
conta_bancaria1.sacar("10")
conta_bancaria1.verificar_saldo()
conta_bancaria1.verificar_limite()
