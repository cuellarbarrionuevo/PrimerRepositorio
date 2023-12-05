B500 = 500
B200 = 200
B100 = 100
B50 = 50
B20 = 20
B10 = 10
B5 =5
M50 = 0.5
M20 = 0.2
M10 = 0.1
M05 = 0.05
M02 = 0.02
M01 = 0.01

precio = 1001.63
dinero = 2300

CB500 = dinero//B500
CB200 = (dinero%B500)//B200
CB100 = ((dinero%B500)%B200)//B100
CB50 = (((dinero%B500)%B200)%B100)//B50
CB20 = ((((dinero%B500)%B200)%B100)%B50)//B20
CB10 = (((((dinero%B500)%B200)%B100)%B50)%B20)//B10
CB5 = ((((((dinero%B500)%B200)%B100)%B50)%B20)%B10)//B5
CM50 = (((((((dinero%B500)%B200)%B100)%B50)%B20)%B10)%B5)//M50
CM20 = ((((((((dinero%B500)%B200)%B100)%B50)%B20)%B10)%B5)%M50)//M20
CM10 = (((((((((dinero%B500)%B200)%B100)%B50)%B20)%B10)%B5)%M50)%M20)//M10


cambio = f'''
Billetes 500 : {CB500}
Billetes 200 : {CB200}
Billetes 100 : {CB100}
Billetes 50  : {CB50}
Billetes 20  : {CB20}
Billetes 10  : {CB10}
Billetes 5  : {CB5}
Monedas 50  : {CM50}
Monedas 20  : {CM20}
Monedas 10  : {CM10}


'''

print(cambio)