import unittest
from sistema_venta import Producto, Catalogo, Carrito, Cliente, Pedido

# Pruebas de Caja Negra
def test_agregar_producto_catalogo():
    catalogo = Catalogo()
    producto = Producto(1, "Laptop", 1500, 10)
    catalogo.agregar_producto(producto)
    assert catalogo.obtener_producto(1) == producto

def test_agregar_producto_carrito():
    cliente = Cliente(1, "Juan")
    producto = Producto(1, "Laptop", 1500, 10)
    cliente.carrito.agregar_producto(producto, 2)
    assert cliente.carrito.items[1]['cantidad'] == 2

def test_quitar_producto_carrito():
    cliente = Cliente(1, "Juan")
    producto = Producto(1, "Laptop", 1500, 10)
    cliente.carrito.agregar_producto(producto, 2)
    cliente.carrito.quitar_producto(producto, 1)
    assert cliente.carrito.items[1]['cantidad'] == 1

# Pruebas de Partición de Equivalencias
def test_particion_equivalencias():
    cliente = Cliente(1, "Juan")
    producto = Producto(1, "Laptop", 1500, 10)
    cliente.carrito.agregar_producto(producto, 5)  # Caso válido
    assert cliente.carrito.items[1]['cantidad'] == 5

    try:
        cliente.carrito.agregar_producto(producto, 6)  # Caso inválido
    except ValueError as e:
        assert str(e) == "Stock insuficiente"

# Pruebas de Valores Límites
def test_valores_limites():
    cliente = Cliente(1, "Juan")
    producto = Producto(1, "Laptop", 1500, 10)
    cliente.carrito.agregar_producto(producto, 10)  # Límite superior válido
    assert cliente.carrito.items[1]['cantidad'] == 10

    producto.stock = 10
    try:
        cliente.carrito.agregar_producto(producto, 11)  # Límite superior inválido
    except ValueError as e:
        assert str(e) == "Stock insuficiente"

    try:
        cliente.carrito.agregar_producto(producto, 0)  # Límite inferior inválido
    except ValueError as e:
        assert str(e) == "Stock insuficiente"

# Pruebas de Transición de Estado
def test_transicion_estado():
    cliente = Cliente(1, "Juan")
    producto = Producto(1, "Laptop", 1500, 10)
    cliente.carrito.agregar_producto(producto, 2)
    pedido = Pedido(cliente)
    assert pedido.confirmar() == "Pedido confirmado para el cliente Juan por un total de $3000"

# Tablas de Decisión
def test_tabla_decision():
    cliente = Cliente(1, "Juan")
    producto = Producto(1, "Laptop", 1500, 10)

    # Caso 1: Producto en stock y cantidad válida
    cliente.carrito.agregar_producto(producto, 5)
    assert cliente.carrito.total() == 7500

    # Caso 2: Producto sin stock suficiente
    producto.stock = 2
    try:
        cliente.carrito.agregar_producto(producto, 3)
    except ValueError as e:
        assert str(e) == "Stock insuficiente"

# Unittest
class TestSistemaVentas(unittest.TestCase):
    def test_agregar_producto_catalogo(self):
        test_agregar_producto_catalogo()

    def test_agregar_producto_carrito(self):
        test_agregar_producto_carrito()

    def test_quitar_producto_carrito(self):
        test_quitar_producto_carrito()

    def test_particion_equivalencias(self):
        test_particion_equivalencias()

    def test_valores_limites(self):
        test_valores_limites()

    def test_transicion_estado(self):
        test_transicion_estado()

    def test_tabla_decision(self):
        test_tabla_decision()

if __name__ == "__main__":
    unittest.main()