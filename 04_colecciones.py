#Array
'''
mi_array = [["cafe",1.5,True],["Te",2.1,False]]
mis_arrays = [[mi_array],[mi_array]]
print(mi_array[0][1])

if mi_array[0][2]:
    print(f"Si me gusta el {mi_array[0][0]} tomare uno a {mi_array[0][1]} eur")

print(mis_arrays)

cosas_que_me_gustan = []
respuesta = input("Que te gusta?:")
cosas_que_me_gustan.append(respuesta)
print("Cosas_que_me_gustan: \n")
print(cosas_que_me_gustan)

cosas_que_me_gustan = []
cuantas_cosas_te_gustan = int(input("¿Cuantas cosas te gustan? -->"))

for i in range(0,cuantas_cosas_te_gustan):
    respuesta = input("Que te gusta?:")
    cosas_que_me_gustan.append(respuesta)
print(cosas_que_me_gustan)

contador = 1
for me_gusta in cosas_que_me_gustan:
    print(f"{contador} - {me_gusta}")
    contador += 1
'''        

lista_alumnos = [{"nombre": "Bill1", "apellido": "Gates", "ciudad": "Seattel"},
                 {"nombre": "Bill2", "apellido": "Gates", "ciudad": "Seattel"},
                 {"nombre": "Bill3", "apellido": "Gates", "ciudad": "Seattel"},
                 {"nombre": "Bill4", "apellido": "Gates", "ciudad": "Seattel"},
                 {"nombre": "Bill5", "apellido": "Gates", "ciudad": "Seattel"}
                 ] 

print(len(lista_alumnos))