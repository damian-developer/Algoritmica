import array as arr
import numpy

arreglo1 = arr.array('i',[1,2,3,4,5,6,7,8])
arreglo2 = numpy.array([3,6,9,12])

division = arreglo2 / 3
print(division)

corte_arr1 = arreglo1[0:4]

print(f"Espacio en memoria del array 1: {id(arreglo1)}")
print(f"Espacio en memoria del array cortado: {id(corte_arr1)}\n")

print(f"Espacio en memoria del elemento 0 en el array1: {id(arreglo1[0])}")
print(f"Espacio en memoria del elemento 0 en el array1 corte es: {id(corte_arr1[0])}")

