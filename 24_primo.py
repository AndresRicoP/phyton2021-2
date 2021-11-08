print("Determina si un número X es primo o no")
n=int(input("Da un número "))
if n<0 or n==1:
    print("No es primo")
elif n==2 or n==3:
    print("Es primo")
elif n%2==0:
    print("No es primo")
else:
    p=0
    i=2
    ls=n-1
    while i<=ls:
        if n%i==0:
            p=1
            break
        i+=1
    if p==1:
        print("No es primo")
    else:
        print("Es primo")