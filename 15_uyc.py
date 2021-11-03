print("Este ejercicio solicita y compara valores para un usuario y contraseña")
u = str(input("USUARIO: "))
if u=="ANDRES":
    p = str(input("CONTRASEÑA: "))
    if p=="123456":
        print(f"Bienvenid@ {u}")
    else:
        print("Contraseña incorrecta, sáquese")
else:
    print("Usuario incorrecto, sáquese")
