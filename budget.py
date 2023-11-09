class Category:
    
    category = ''
    ledger = []
    
    def __init__(self, category):
        self.category = category
        self.ledger = []
        
    def check_funds(self, amount:float):
        if amount > self.get_balance():
            return False
        else:
            return True
        
    # Se guardan la cantidad y la descrición como diccionario dentro de la lista
    def deposit(self, amount:float, description:str = ''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount:float, description:str = ''):
        # Si no hay suficientes fondos, se retorna False
        if self.check_funds(amount) == False:
            return False
        else:
            # Se multiplica el amount por -1  porque es retiro
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
        # Primero se valida que se pueda hacer el retiro comprobando la cantidad a transferir
        if self.withdraw(amount, 'Transfer to '+category.category) == False:
            return False
        else:
            # Se llama el método deposit del objeto al que se le hace la transferencia
            category.deposit(amount, 'Transfer from '+self.category)
            return True