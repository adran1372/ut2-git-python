print("---MENU---\n1- Hola\n2-Adios\n3-Saliendo")

opcion = int(input("Dime tu opcion"))
match opcion:
    case 1:
        print("Hola")
    case 2:
        print("Adios") 
    case 3:
        print("Hasta pronto") 
    case _:
        print("Opcion no valida") 
