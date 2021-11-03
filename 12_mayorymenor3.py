print("En este programa solicitará 3 números y nos indicará el mayor y menor de los 3")
n1=float(input("Da un número "))
n2=float(input("Da otro número "))
n3=float(input("Da otro número "))
if n1>n2:
    if n1>n3:
        if n2>n3:
            print(f"El mayor es {n1} y el menor es {n3}")
        else:
            print(f"El mayor es {n1} y el menor es {n2}")
    else:
        print(f"El mayor es {n3} y el menor es {n2}")
elif n2>n3:
    if n1>n3:
        print(f"El mayor es {n2} y el menor es {n3}")
    else:
        print(f"El mayor es {n2} y el menor es {n1}")
else:
    print(f"El mayor es {n3} y el menor es {n1}")