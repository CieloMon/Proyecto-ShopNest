# ------------------------------
# Proyecto: ShopNest
# Autora: Cielo Liliana Monterrubio Martínez
# Descripción: Estructura base orientada a objetos para el e-commerce ShopNest
# ------------------------------

# Clase base
class Usuario:
    def __init__(self, id_usuario, nombre, email, contrasena):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

# Clase Cliente (hereda de Usuario)
class Cliente(Usuario):
    def __init__(self, id_usuario, nombre, email, contrasena, direccion, telefono):
        super().__init__(id_usuario, nombre, email, contrasena)
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras = []

    def realizar_compra(self, pedido):
        self.historial_compras.append(pedido)

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock, id_emprendedor):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.id_emprendedor = id_emprendedor

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

# Clase ItemCarrito
class ItemCarrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

# Clase Carrito
class Carrito:
    def __init__(self, id_carrito, id_cliente):
        self.id_carrito = id_carrito
        self.id_cliente = id_cliente
        self.productos = []

    def agregar_producto(self, item):
        self.productos.append(item)

    def calcular_total(self):
        return sum(item.producto.precio * item.cantidad for item in self.productos)

# Clase Pedido
class Pedido:
    def __init__(self, id_pedido, id_cliente, lista_productos):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.lista_productos = lista_productos
        self.total = self.calcular_total()
        self.estado = "Creado"

    def calcular_total(self):
        return sum(item.producto.precio * item.cantidad for item in self.lista_productos)

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

# Clase Venta
class Venta:
    def __init__(self, id_venta, pedido):
        self.id_venta = id_venta
        self.pedido = pedido

    def procesar_pago(self, monto):
        if monto >= self.pedido.total:
            self.pedido.actualizar_estado("Pagado")
            return True
        return False

# Clase Notificación
class Notificacion:
    def __init__(self, id_notificacion, id_usuario, mensaje):
        self.id_notificacion = id_notificacion
        self.id_usuario = id_usuario
        self.mensaje = mensaje
        self.leido = False

    def marcar_leido(self):
        self.leido = True


# Ejemplo rápido de prueba
if __name__ == "__main__":
    producto1 = Producto(1, "Playera ShopNest", "Camiseta con logo", 250.0, 20, 101)
    item = ItemCarrito(producto1, 2)
    carrito = Carrito(1, 2001)
    carrito.agregar_producto(item)
    pedido = Pedido(1, 2001, carrito.productos)
    cliente = Cliente(2001, "Cielo", "cielo@shopnest.com", "1234", "Xalapa, Veracruz", "2281112233")
    cliente.realizar_compra(pedido)

    print(f"Cliente: {cliente.nombre}")
    print(f"Total del pedido: ${pedido.total}")
    print(f"Estado del pedido: {pedido.estado}")