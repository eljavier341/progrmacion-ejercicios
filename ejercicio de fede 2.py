num=0
intento=0
intdelusu=0
import random 

numsec=random.randint(1,20)

print("estoy pensando un nunmero entre el 1 y 20, 100 a que no lo pegas")
print("tenes 6 intentos")
for intento in range(1,6):
    intdelusu=int(input(f"intento {intento}: cual es tu numero"))

    if intdelusu < numsec:
     print("jiji te falta sopa")
    if intdelusu > numsec:
     print("jiji mucha sopa")
    if intdelusu == numsec:
     print(f"te lo dejo ganar por pena dea")
    else:
     print(f"jaja re gil ni de cerca")
    
print(f"El número era {numsec}")
    