
total=0
P=0
im=0
imsiva=0
ct=0

def ct (imsiva,piva=21):
    total=imsiva+(imsiva*piva//100)
    return total
im=input("introduce un importee (no se hagan los piolas y pongan SOLO numeros enteros")
imsiva=int (im)

p=input("introcue un iva o preciona enter para que sea 21%")

if p.strip()=="":
    piva=21
else:
    piva=int(p)
    
total=ct(imsiva,piva)

print("importe sin iva",imsiva,"pesitos")
print("iva aplicado",piva, "%")
print("importe total con iva ",total,"pesitos")