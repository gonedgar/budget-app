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
        if self.withdraw(amount, 'Transfer to '+ category.category) == False:
            return False
        else:
            # Se llama el método deposit del objeto al que se le hace la transferencia
            category.deposit(amount, 'Transfer from '+self.category)
            return True

def print_category(Category):
    dots = 0
    title = ''
    total = 0
    # Se identifica la cantidad de * que van a la izquierda y a la derecha de la categoría
    dots = int((30 - len(Category.category)) / 2)
    # Primer loop para los * a la izquierda de la categoría
    for x in range(dots):
        title = title + '*'
    # Se concatena la categoría con los primeros *
    title = title + Category.category
    # Segundo loop para concatenar los * de la derecha a la cadena anterior
    for x in range(dots):
        title = title + '*'
        # Si el título es menor a 30, se añade un * al final para que sea 30
        if len(title) < 30:
            title = title + '*'
    # Se imprime el título
    print(title) # <----------------------------------------------------------------------------------------
    # Loop para imprimir cada elemento de la lista
    for x in Category.ledger:
        # Se obtiene la longitud de la cantidad junto con el signo (si es negativo) y dos espacios decimales
        monto = float(str("{a:.2f}").format(a = x['amount']))
        cantidad = len(str(monto))
        # Se obtiene la longitud de la descripción
        descripcion = len(x['description'])
        # Se suma (o resta si es negativa) la cantidad al total
        total = total + x['amount']
        # Si la descripción es mayor a 23
        if descripcion > 23:
            # La descripción se acorta a 23 y se concatena al inicio de la string
            imprimir = '' + x['description'][:23]
            # Se determinan y concatenan los espacios que se dejan de acuerdo al amount
            for y in range((30 - cantidad) - 23):
                imprimir = imprimir + ' '
            # Se concatena el amount formateado con dos decimales
            imprimir = imprimir + str(monto)
            # Se imprime el amount en consola
            print(imprimir)
        # Si la descripción no es mayor a 23
        else:
            # Se concatena la descripción tal cual al inicio de la string
            imprimir = '' + x['description']
            # Se determinan y concatenan los espacios que se dejan de acuerdo al amount
            for y in range((30 - cantidad) - descripcion):
                imprimir = imprimir + ' '
            # Se concatena el amount formateado con dos decimales
            imprimir = imprimir+str(monto)
            # Se imprime el amount en consola
            print(imprimir)
    
    print("Total:{a: .2f}".format(a = total))
    
def create_spend_chart(categories:list):
    # Se crea la variable bar_chart en la que se guardará toda la cadena de texto que compondrá la gráfica
    # obviamente comienza por el texto 'Percentage spent by category' que se mostrarà siempre al principio
    bar_chart = 'Percentage spent by category\n'
    # Variable en la que se guardan las categorías y se va sumando el monto gastado para obtener el total de cada categoría
    gastos = []
    # Primero se obtiene la cantidad total de gastos (withdrawals) para poder obtener los porcentajes
    
    
    return bar_chart