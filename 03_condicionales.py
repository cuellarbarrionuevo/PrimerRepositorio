#if
llueve =False
if llueve:
    print("tomaré un paraguas")
else:
    print("NO tomare un paraguas")

print("Cuanto dinero tienes? ")
dinero_que_tengo = int(input())
if dinero_que_tengo<= 2:
    print("comprare algo del super") 
elif dinero_que_tengo <= 3:
    print("comprare algo del super2")
elif dinero_que_tengo <= 4:
    print("Ire restaurante 1")
elif dinero_que_tengo <= 5:
    print("Ire restaurante 2")
else:
    print("Ire restaurante 3")

dia_semana="martes"

match dia_semana:
    case "lunes":
        print("hoy es lunes")
    case _:
        print("Hoy no es lunes")
