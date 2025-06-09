cara=0
est=1
carapest=0
sobra=0

cara=int(input("cuants caramelos hay en la la bolsa magica"))
est=int(input("cuantos estudiantes hay en el 5toc<"))
 
carapest= cara // est
sobra= cara % est

print("a cada estudiante le toca ",carapest,"caracamelos")
print("sobran",sobra,"caracmels en la bolsa")

