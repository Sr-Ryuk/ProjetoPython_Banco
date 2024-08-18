from models.cliente import Cliente
from models.conta import Conta

diogo = Cliente('Diogo','diogo@email.com','154109872892','14/05/2004')
juliana = Cliente('Juliana', 'ju@email.com', '12345678900', '17/02/1984')

#print(diogo)
#print(juliana)

contad: Conta = Conta(diogo)
contaj: Conta = Conta(juliana)

print(contad)

