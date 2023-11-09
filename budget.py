class Category:
    
    category = ''
    ledger = []
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
    # Se guardan la cantidad y la descrición como diccionario dentro de la lista
    def deposit(self, amount:float, description:str = ''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount:float, description:str = ''):
        saldo:float = 0
        # Si la lista está vacía, entonces no hay fondos para retirar
        if len(self.ledger) == 0:
            return False
        # Se suma el amount de cada elemento de la lista para obtener el saldo
        for x in self.ledger:
            saldo = saldo + x['amount']
        # Se verifica que el amount que se va a retirar sea menor al saldo
        if (saldo - amount) < 0:
            return False
        else:
            # Se multiplica el amount por -1  porqu es retiro
            self.ledger.append({'amount': (amount * -1), 'description': description})
            return True
    
    def get_balance(self):
        balance = 0
        # Si la lista está vacía, el saldo es cero
        if len(self.ledger) == 0:
            return 0
        # Se suman todos los amount que están dentro de cada diccionario de la iista
        for x in self.ledger:
            balance = balance + x['amount']
        return balance
    
    # Pide como argumento el amount y el objeto al que va a ser hecho el depósito
    def transfer(self, amount:float, category):
        # Primero se valida que se pueda hacer el retiro comprobando la cantidad a  transferir
        if self.withdraw(amount, 'Transfer to '+category.category) == False:
            return False
        else:
            # Se llama el método deposit del objeto al que se le hace la transferencia
            category.deposit(amount, 'Transfer from '+self.category)
            return True