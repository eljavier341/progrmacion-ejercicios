mon=0
b1000=0
b200=0
sse=0
rest=0
mon=int(input("cuantos dinero quieres sacar del sharkcajero"))

b1000=mon//1000
rest=mon%1000
b200=rest//200
sse=rest%200
print("seentrega")
print(b1000,"sharkbilletes de 1000")
print(b200,"sharkbilletes de 200")
print("lo que no se pudo sacar del sharkcajero",sse)