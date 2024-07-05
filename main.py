from sistema_venta import Producto, Catalogo, Carrito, Cliente, Pedido
from tabulate import tabulate

def inicializar_datos():
    # Crear productos
    producto1 = Producto(1, "Laptop", 1500, 10)
    producto2 = Producto(2, "Mouse", 25, 50)
    producto3 = Producto(3, "Teclado", 75, 30)

    # Crear catálogo y agregar productos
    catalogo = Catalogo()
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Crear cliente
    cliente = Cliente(1, "Juan")

    return catalogo, cliente

def mostrar_carrito(carrito):
    data = []
    for item in carrito.items.values():
        data.append([item['producto'].nombre, item['cantidad'], item['producto'].precio, item['cantidad'] * item['producto'].precio])
    headers = ["Producto", "Cantidad", "Precio Unitario", "Total"]
    print(tabulate(data, headers, tablefmt="grid"))

def ejecutar_operaciones(catalogo, cliente):
    # Agregar productos al carrito
    cliente.carrito.agregar_producto(catalogo.obtener_producto(1), 2)
    cliente.carrito.agregar_producto(catalogo.obtener_producto(2), 5)

    # Mostrar productos en el carrito
    print("Productos en el carrito:")
    mostrar_carrito(cliente.carrito)

    # Quitar un producto del carrito
    cliente.carrito.quitar_producto(catalogo.obtener_producto(2), 3)
    print("\nDespués de quitar 3 unidades del producto Mouse:")
    mostrar_carrito(cliente.carrito)

    # Confirmar pedido
    pedido = Pedido(cliente)
    print("\n" + pedido.confirmar())

if __name__ == "__main__":
    catalogo, cliente = inicializar_datos()
    ejecutar_operaciones(catalogo, cliente)


