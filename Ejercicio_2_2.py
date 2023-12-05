billetes_monedas = [500,200,100,50,20,10,5,2,1,0.5,0.2, 0.1,0.05,0.02, 0.01]

precio = 1911.29
dinero = 7000
cambio_total = dinero-precio
cambio_dado = 0
mensaje = ""
if dinero < precio:
    print ("Dinero insuficiente")
else:
    for bi_mo in billetes_monedas:
        cambio_pendiente = cambio_total - cambio_dado
        if cambio_pendiente >= bi_mo:
            num = cambio_pendiente // bi_mo
            mensaje += f"numero de billetes/monedas de  {bi_mo} es {num} \n"
            cambio_dado += bi_mo * num
            cambio_pendiente = cambio_total - cambio_dado

    print (mensaje)