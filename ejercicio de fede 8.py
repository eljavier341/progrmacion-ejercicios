ar=0
radio=0
alto=0
ab=0
vl=0
import math

def ac(radio):
    ar=math.pi*radio*radio
    print("area del circuclo", ar)
    
def vc (radio,alto):
    ab=math.pi*radio*radio
    vl=ab*alto
    print("el volumen del cilindro es",vl)
    
radio = int(input("Ingresa el radio"))
alto = int(input("Ingresa el alto"))

ac(radio)
vc(radio, alto)
