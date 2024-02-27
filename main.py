from conta import CartaoDeCerdito, ContaCorrente
from agencia import AgenciaComum, Agencia, AgenciaPremium, AgenciaVirtual



#programa_cartao_de_credito:
conta_wendell = ContaCorrente('wendell', '111.222.333.45', 12345, 6789)

cartao_wendell = CartaoDeCerdito('wendell', conta_wendell)

#programa_conta_corrente:
conta_usuario = ContaCorrente('wendell', '444.555.667-23', 1234, 2048)



#AgenciaPremium
agencai_premium = AgenciaPremium(119686258, 101125467781)

#Agenciacomum
agencia_comum = AgenciaComum(119686256, 1010235411000)


#-------ContaVirtual------
agencia_virtual = AgenciaVirtual('www.agenciaVirtual.com', 11667788359, 11213148000)

#---------------AGENCIA---------------------
agencia1 = Agencia(11226633987, 121548125484000, 4561)

