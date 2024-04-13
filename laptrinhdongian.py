import math
a,b,c = eval(input(
    "Nhap cac so a,b,c lan luot la  "))
Denta = b**2 - 4*a*c 
if a == 0: 
    print("khong phai phuong trinh bac hai")
elif a != 0: 
    if Denta > 0:
        x1 = (-b + math.sqrt(Denta)) / (2*a)
        x2 = (-b - math.sqrt(Denta)) / (2*a)
        print("phuong trinh co hai nghiem x1= ",x1," x2= ",x2)
    elif Denta <= 0:
        if Denta == 0:
            x = (-b/(2*a))
            print("phuong trinh co nghiem kep la x= ",x)
        else:
            print("phuong trinh co nghiem phuc")







