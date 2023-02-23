c_compra=0
codigos_ventas=[]
usuarios=[]
productos=[]
total=[]
c_computadora=0
c_tablet=0
c_celular=0
c_total=0

numeroDeVentas = int(input("Ingrese el numero de ventas que desea registrar: "))

for i in range (numeroDeVentas):
    c_compra+=1
    codigos_ventas.append(c_compra)
    i_nombre= str(input("Igrese su nombre: ")).lower()
    usuarios.append(i_nombre)
    p_comprar=int(input("Que producto quiere comprar 1.Computador 2.Tablet 3.Celular: "))
    if p_comprar == 1:
        productos.append("computadora")
        total.append(500000)
        c_computadora+=1
        c_total+=500000
    if p_comprar == 2:
        productos.append("tablet")
        total.append(200000)
        c_tablet+=1
        c_total+=200000
    if p_comprar == 3:
        productos.append("celular")
        total.append(100000)
        c_celular+=1
        c_total+=100000
menu=0
while menu <6:
    print("1. retomar productor comprado con codigo de venta")
    print("2. retornar las compras de un usuario")
    print("3. promedio total de ventas")
    print("4. indicar producto mas vendido")
    print("5. retornar usuarios que compraron un producto")
    print("6. salir")
    opcion=int(input("Elija una opcion: "))
    if opcion== 1:
        c_buscar=int(input("Ingrese el codigo a buscar: "))
        for i in range (len(codigos_ventas)):
            if c_buscar == codigos_ventas[i]:
                print("El producto comprado con el codigo de venta es: ", productos[i])
        input("presione enter")
    if opcion== 2:
        u_buscar=str(input("Ingrese el nombre del usuario: ")).lower()
        print("Los productos comprados por el usuario", u_buscar,"son: ")
        for i in range (len(codigos_ventas)):
            if u_buscar == usuarios[i]:
                print(productos[i])
        input("presione enter")
    if opcion== 3:
        promedio= c_total/8
        print("El promedio de ventas es de: ", promedio)
    if opcion== 4:
        if c_computadora > c_tablet and c_computadora > c_celular:
            print("El producto más comprado vendido es computadora")
        if c_tablet > c_computadora and c_tablet > c_celular:
            print("El producto más comprado vendido es tablet")
        if c_celular > c_computadora and c_celular > c_tablet:
            print("El producto más comprado vendido es computadora")
        input("Presione enter")
    if opcion== 5:
        p_buscar=str(input("Escriba el nombre del producto: computadora, tablet o celular:  ")).lower()
        for i in range (len(codigos_ventas)):
            if p_buscar == productos[i]:
                print(usuarios[i])
        input("presione enter")
    if opcion==6:
        menu=7
        print("gracias")