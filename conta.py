from datetime import datetime
import pytz
from random import randint
class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.num_conta = num_conta
        self._saldo = 0
        self._limite = None
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f'seu saldo atual é de: R${self._saldo:,.2f}')

    def depositar_dinheiro(self, valor):
        self._saldo =+ valor
        self._transacoes.append((valor, (f'saldo{self._saldo}'), ContaCorrente._data_hora()))
    
    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print(f'você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, (f'saldo{self._saldo}'), ContaCorrente._data_hora()))
    
    def consultar_limite_chequeespecial(self):
        print(f'seu limite de cheque especial é de: R${self._limite:,.2f}')

    def consultar_historico_transacoes(self):
        print('Historico de transações')
        for transacao in self._transacoes:
            print(transacao)
    
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))
        
class CartaoDeCerdito:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoDeCerdito._data_hora().month, CartaoDeCerdito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha():
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Senha inválida')
