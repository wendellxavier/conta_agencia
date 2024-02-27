from random import randint
class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimo = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'caixa com nivel abaixo, Caixa atual: R${self.caixa:,.2f}')
        else:
            print(f'O valor de caixa esta ok, caixa atual: R${self.caixa:,.2f}')

    def emprestimo_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimo.append((valor, cpf, juros))
        else:
            print('emprestimo não foi possivel')
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
        

class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        if self.caixa < valor:
            print(f'O dinheiro do caixa não esta diposnivel, o valor no caixa é R${self.caixa:,.2f}')
        else:
            self.caixa -= valor
            self.caixa_paypal += valor
    

    def sacar_paypal(self, valor):
        if self.caixa_paypal < valor:
            print(f'O dinheiro do paypal não esta diposnivel, o valor é R${self.caixa_paypal:,.2f}')
        else:
            self.caixa_paypal -= valor
            self.caixa += valor


class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj,):
        super().__init__(telefone, cnpj, numero=randint(1000, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj,):
        super().__init__(telefone, cnpj, numero=randint(1000,9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Seu patrimonio está abaixo para essa conta')



if __name__ == "__main__":
    #AgenciaPremium
    agencai_premium = AgenciaPremium(119686258, 101125467781)
    agencai_premium.adicionar_cliente('wendell', 144565599889, 20000000)
    print(agencai_premium.clientes)
            



    #Agenciacomum
    agencia_comum = AgenciaComum(119686256, 1010235411000)



    #-------ContaVirtual------
    agencia_virtual = AgenciaVirtual('www.agenciaVirtual.com', 11667788359, 11213148000)






    """
    ---------------AGENCIA---------------------
    agencia1 = Agencia(11226633987, 121548125484000, 4561)
    agencia1.caixa = 1000000
    agencia1.emprestimo_dinheiro(150, 45454645478 , 0.02)
    print(agencia1.emprestimo)
    agencia1.adicionar_cliente('wendell', 65445545623, 30000)
    print(agencia1.clientes)
    """