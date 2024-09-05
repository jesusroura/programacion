zapatillas={"COD1":{"modelo":"vans", "material":["cuero","goma","nylon"],"numero":38,"cantidadstock":39},
            "COD2":{"modelo":"toper blancas", "material":["cuero","goma","nylon","algodon"],"numero":38,"cantidadstock":89},
            "COD3":{"modelo":"air for blancas", "material":["cuero","goma","nylon","algodon"],"numero":38,"cantidadstock":99}}

while True:
    opcion=input("ingrese una de las siguientes opciones: \n1 Mostrar las zapas en stock \n2 agregar zapas al stock \n3 salir \n ")
    if opcion=="1":
        print("______________________")
        print("------zapatillas------")
        print("______________________")
        for c,v in zapatillas.items():
            print(c,  ":",  v)
            print("_______________")
    elif opcion=="2":
        
        zapatillaAgrgar=input("ingrese el nombre de las zapatillas que quiera agragar al stock: ")
        modelo=input("ingrese el modelo de la zapatilla: ")
        material=input("ingrese el material de la zapatilla: ")
        numero=input("ingrese el numero de la zapatilla: ")
        CantidadDeStock=input("ingrese la cantidad en stock que se vendan: ")
        zapatillas[zapatillaAgrgar]=modelo,material,numero,CantidadDeStock
    elif opcion==3:
        break