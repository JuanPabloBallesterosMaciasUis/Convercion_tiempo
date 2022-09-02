# Programa No 4 : Segundos en horas, minutos y segundos

print("-----------------------------------------------")
print("----SEGUNDOS EN HORAS MINUTOS Y SEGUNDOS-------")

# input
n = input(" el tiempo en segundos: ")
n = int(n)

# process
h = n/3600

h1 = int(h)
m1 = (h-h1)*60

m2 = int(m1)
s1 = int((m1-m2)*60)

# output
if h1==1:
    print("De los ",n," segundos, seria ",h1,"hora con ",m2,"minutos y ",s1,"segundos")
else:
    print("De los ",n," segundos, seria ",h1,"horas con ",m2,"minutos y ",s1,"segundos")




    







