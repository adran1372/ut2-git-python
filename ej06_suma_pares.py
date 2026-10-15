limite = int(input("Cuantos pares quieres que sume: "))
suma = 0
for i in range(1, limite+1):
    if(i%2 == 0):
        suma += i
    else:
        continue
print(suma)