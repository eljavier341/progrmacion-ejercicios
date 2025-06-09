def facto(n):
   if n==0:
       return 1
   if n == 1:
        return 1
   return n * facto(n-1)

print("que numeros queres facto-rizar")
x=int(input())
print(f" el factorial de {x} es {facto(x)}")