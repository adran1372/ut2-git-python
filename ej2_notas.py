nota = float(input("Dime tu calificacion: "))

if(nota < 5):
    print("Suspenso")
elif(nota >= 5 or nota < 7):
    print("Aprobado")
elif(nota >=7 or nota < 9):
    print("Notable")
else:
    print("Sobresaliente")