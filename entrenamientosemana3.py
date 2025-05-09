inventario = []

def nombre_producto():
    while True:
        nombre = input("ingresar nombre del producto: ")
        #verificar que no este vacio, hacer cadena de texto para que no ingresar algo diferente que no sea una letra
        if nombre.strip() and all(c.isalpha() for c in nombre):
            #si es valido, repetir nombre
            return nombre
        else:
            print("nombre no valido, intertar nuevamente: ")
            
#convertir la entrada a un numero
def solicitar_precio():
    while True:
        entrada = input("ingresar precio: ")
        try:
            numero = float(entrada)
            # si es valido, repite numero
            return numero
        except ValueError:
            print("entrada no valida, ingresar un numero: ")


#convertir cantidad a un numero, no permitir letras
def cantidad_productos():
    while True:
        cantidad = input("ingresar cantidad: ")
        try:
            producto = float(cantidad)
            #si es valido, repetir cantidad
            return producto
        except ValueError:
            print("entrada no valida, intentarlo nuevamente: ")
        
#agregar nuevos productos
def añadir_productos(nombre,precio,cantidad): 
    diccionario = { 
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
     }
    inventario.append(diccionario)
    print(f"producto '{nombre} precio del producto'{precio}' cantidad del producto '{cantidad}' se añadio al inventario.")
    print(inventario)

def mostrar_producto():
    if inventario:
        print("productos de inventario: ")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, cantidad{producto['cantidad']}")
    else:
        print("el inventario esta vacio")
    
#bucar productos existentes
def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            #repetir producto encontrado
            return producto    
        #repetir si no se encuentra el producto
    return None

def eliminar_producto(nombre):
    global inventario
    producto = buscar_producto(nombre)
    if producto:
        inventario = [p for p in inventario if p["nombre"].lower() != nombre.lower()]
        print(f"producto '{nombre}' eliminado del inventario. ")
    else:
        print(f"producto '{nombre}' no se encontro producto. ")

#actualizar precio de productos 
def precio_actualizar(nombre):
    global inventario 
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            nueva_cantidad = input("ingrese el valor a modificar : ")
            producto["precio"] = nueva_cantidad
            break  # opcional si solo hay un producto con ese nombre
#poder calcular el valor total de productos 
def calcular_total():
    calcular_lambda = sum(map (lambda precio: precio["precio"] * precio["cantidad"],inventario) )
    #total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)
    print({calcular_lambda})
    return 

if __name__ == "__main__":

    #menu de usuario
    while True:
        print("escoge tu opcion:")
        print("1. añade un producto: ")
        print("2. buscar producto: ")
        print("3. eliminar producto: ")
        print("4. actualizar precio: ")
        print("5. calcular total de los productos: ")
        print("6. salir. ")
      
        opcion = input("escoge una opcion: ").strip()

        if opcion == "1":
            nombre = nombre_producto()
            precio = solicitar_precio()
            cantidad = cantidad_productos()
            añadir_productos(nombre, precio, cantidad)
            
        elif opcion == "2":
            nombre = input("ingresar nombre producto que desea buscar: ").strip()
            producto = buscar_producto(nombre)
            if producto:
                print(f"producto encontrado: precio = {producto['precio']}, cantidad = {producto['cantidad']}")
            else:
                print("el producto no fue encontrado.")

        elif opcion == "3":
            nombre = input("ingresar nombre del producto a eliminar: ").strip()
            eliminar_producto(nombre)

        elif opcion == "4":
            nombre = input("ingresar nombre producto a actualizar: ").strip()
            #precio actualizar
            precio_actualizar(nombre)
          
        elif opcion == "5":
            calcular_lambda = sum(map (lambda precio: precio["precio"] * precio["cantidad"],inventario) )
            print(calcular_lambda)

        elif opcion == "6":
            print("salir del sistema. ")
            break
            
        else:
            print("esta opcion es incorrecta, intentar nuevamente.")

