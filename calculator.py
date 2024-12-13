szam1 = int(input('Első szám: '))
szam2 = int(input('Másik szám: '))
jel = str(input('Műveleti jel: '))


if jel == '+' :
    eredmeny = (szam1 + szam2)
elif jel == '-' :
    eredmeny = (szam1 - szam2)
elif jel == '*' :
    eredmeny = (szam1*szam2)
elif szam2 == 0 and jel == '/':
    eredmeny = " Ez a művelet nem lehetséges!"
elif jel == '/' :
    eredmeny = (szam1/szam2)
else:
    print('Ismeretlen művelet')

print(f"{szam1}{jel}{szam2}={eredmeny}")