import pi

#Que tenga una expresión .pyc significa que después de la primera ejecución, el programa Python utilizará el .pyc compilado al importar.


t_upla = (10,100,1000,10000,100000,1000000,10000000)
def f():
  lista = []
  for j in range (0,len(t_upla)):
    Pi = pi.g(t_upla[j])
    lista = lista + [Pi]
  print lista

f()

#No se invierte mucho tiempo, solo el que se tarda en introducir el apartado 2 dentro de una función dejando fuera la t_upla
#Con un cronómetro