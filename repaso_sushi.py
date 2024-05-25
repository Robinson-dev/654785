import os
import time
clean="cls"
os.system(clean)
sushi=0
sushiP=0
sushiA=0
sushiO=0
sushiV=0
valorp=0
valorV=0
valorO = 0
valorA=0
descuento=0
respuesta=1
Mensaje="\n"+("_"*34)
while True:
    volver=" "
    try:
        time.sleep(1)
        os.system(clean)
        print("Bienvenidos al delivery de sushi")
        print("seleccione el tipo de sushi : ")
        print("1. Pikachu Roll $4.500")
        print("2. Otaku Roll $5.000")
        print("3. Pulpo Venenoso Roll $5.200")
        print("4. Anguila Elétrica Roll $4.800")
        print(" proceder a pago")
        print(Mensaje)
        total = sushiP * valorp + sushiO * valorV + sushiV * valorV * sushiA * valorA
        menu2 = f" Llevas la cantidad de : {sushi} y su cuenta es : {total}"
        print(menu2)# se imprime cuantos rolls lleva y cuanto cuesta el pedido
        tipo = 1
        if tipo == 1:
            sushiP += 1
            sushi += 1
            valorp += 4500
            continue
        elif tipo == 2:
            sushiO += 1
            sushi += 1
            valorO = 5000
            continue
        elif tipo==3:
            sushiV += 1
            sushi += 1
            valorV = 5200
            continue
        elif tipo == 4:
            sushiA += 1
            sushi += 1
            valorA = 4800
            continue
        elif tipo == 5:
            print(" ingrese un valor de 1 - 5 ")  
        else:
            print(" ingrese un numero valido")
            time.sleep(1)
            continue      
    except ValueError:
        print(" ingrese un numero valido")    
        time.sleep(1)
        continue
    while True:
        try:
            os.system(clean)
            time.sleep(1)
            print("posee codigo de descuento?")
            print("1. si")
            print("2. no ")
            codigo = int(input("ingrese su opcion 1 o 2 :"))
            if codigo >=1 and codigo <= 2:
                break
            else:
                print(" --> debe ingresar un numero valido 1 o 2 :")
                continue
        except ValueError:
            print("--> debe ingresar un numero valido 1 o 2 ")    
            time.sleep(1)
            continue
    total = sushiP * valorp + sushiO * valorO + sushiV * valorV + sushiA * valorA
    while codigo == 1:
        try:
            os.system(clean)
            time.sleep(1)
            nomDescuento = input(" Ingrese un codigo de descuento :")
            if nomDescuento == "soyotaku":
               descuento = total * 0.10
               print(" Has obtenido un 10% de descuento")
               break
            else:
                print("codigo no valido")
                print("desea reingresar el codigo? ") 
                print("V = si")
                print("x = volver al menú")
                volver= input(" ")
                if volver == "V":
                    continue
                else:
                    break
        except ValueError:
            print(" No ha ingresado un valor correcto")
    else:
        os.system(clean)
        time.sleep(1)
    if volver == "X":
        continue
    os.sistem(clean)
    time.sleep(1)
    print(""*50)
    print(f"Total productos : {sushi}")
    print(f"picachu roll : {sushiP} ")
    print(f"Otaku roll : {sushiO}")
    print(f"Pulpo Venenoso : {sushiP} ")
    print(f"Anguila Alectrica Roll : {sushiA}")
    print("*"*50)
    print(f"Subtotal a pagar : $ {total}")
    print("descuento por codigo :$",int(descuento))
    total-=descuento
    print("TOTAL:$",(total))
    print(" Desea realizar otro pedido?")
    print("1. Si")
    print("2. No")
    try:
        if respuesta == 2:
            print(" HAZ SALIDO DEL PROGRAMA")
            print(" G R A C I A S")
        elif respuesta == 1:
            os.system(clean)
            time.sleep(1)     
            sushi=0
            sushiP=0
            sushiA=0
            sushiO=0
            sushiV=0
            valorp=0
            valorV=0
            valorO = 0
            valorA=0
            descuento=0
            respuesta=1
            continue
        else:
            print(" Ingrese un numero dentro del rango del 1 - 2")
    except ValueError:
        print(" ingrese un numero valido")        



