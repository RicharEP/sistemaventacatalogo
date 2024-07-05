class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Catalogo:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def obtener_producto(self, id_producto):
        return self.productos.get(id_producto, None)

class Carrito:
    def __init__(self):
        self.items = {}

    def agregar_producto(self, producto, cantidad):
        if producto.id_producto in self.items:
            if producto.stock >= self.items[producto.id_producto]['cantidad'] + cantidad:
                self.items[producto.id_producto]['cantidad'] += cantidad
            else:
                raise ValueError("Stock insuficiente")
        else:
            if producto.stock >= cantidad:
                self.items[producto.id_producto] = {'producto': producto, 'cantidad': cantidad}
            else:
                raise ValueError("Stock insuficiente")
        producto.stock -= cantidad

    def quitar_producto(self, producto, cantidad):
        if producto.id_producto in self.items:
            if self.items[producto.id_producto]['cantidad'] > cantidad:
                self.items[producto.id_producto]['cantidad'] -= cantidad
                producto.stock += cantidad
            elif self.items[producto.id_producto]['cantidad'] == cantidad:
                producto.stock += cantidad
                del self.items[producto.id_producto]
            else:
                raise ValueError("Cantidad a quitar es mayor que la cantidad en el carrito")
        else:
            raise ValueError("Producto no está en el carrito")

    def total(self):
        return sum(item['producto'].precio * item['cantidad'] for item in self.items.values())

class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.carrito = Carrito()

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.total = cliente.carrito.total()

    def confirmar(self):
        return f"Pedido confirmado para el cliente {self.cliente.nombre} por un total de ${self.total}"
