from datetime import date
from dateutil.relativedelta import relativedelta
añnac=int(input("cual es tu version de vida (año)"))
mnac=int(input("cual es tu version de vida (mes)"))
dnac=int(input("cual es tu version de vida (dia)"))

fnac=date(añnac, mnac, dnac)
hoy=date.today()
td=(hoy - fnac).days
print(f"felicidades arruinaste al mundo por {td} dias dea")


diferencia=relativedelta(hoy, fnac)
print(f"tu edad  por en meses dias y años es: {diferencia.years}, {diferencia.months} ,{diferencia.days} ")
