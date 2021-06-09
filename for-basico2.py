# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def big(a):
    for i in range (len(a)):
        if a[i] > 0:
            a[i] = "big"
    return a
y = big([- 1, 3, 5, -5])
print(y)
# Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. 
# (Tenga en cuenta que cero no se considera un número positivo).
    # Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
    # Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve
def contps(a):
    pos = 0
    for i in range (len(a)):
        if a[i] > 0:
            pos += 1
    a[len(a)-1] = pos
    return a
y = contps([-1, -6, -4, -2, -7, -7, -4, -123, -34.4 -2])
print(y)
# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
    # Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
    # Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def sumatotal (a):
    sum = 0
    for i in range (len(a)):
        sum += a[i]
    return sum
y = sumatotal([6,3, -2]) 
print(y) 
z = sumatotal([-1, 3, 5, -5]) 
print(z)
# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def prom (a):
    sum = 0
    for i in range (len(a)):
        sum += a[i]
    return sum/len(a)
y = prom([6,3, -2]) 
print(y) 
z = prom([-1, 3, 5, -5]) 
print(z)
# crea una función que toma una lista y devuelve la longitud de la lista.
def longlista (a):
    return len(a)
y = longlista([6,3, -2]) 
print(y) 
z = longlista([-1, -6, -4, -2, -7, -7, -4, -123, -34.4 -2]) 
print(z)
# Crea una función que tome una lista de números y devuelva el valor mínimo en la lista. 
# Si la lista está vacía, haga que la función devuelva False.
    # Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
    # Ejemplo: mínimo ([]) debería devolver False    
def min(a):
    if a == []: 
        return False
    else:
        menor = a[0]
        for i in range (len(a)):
            if a[i] < menor:
                menor = a[i]
        return menor
x = min([])
print(x)
y = min([6,3,7,-2,1,2]) 
print(y) 
z = min([-1, -6, -4, -2, -7, -7, -4, -123, -34.4 -2]) 
print(z)
# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. 
# Si la lista está vacía, haga que la función devuelva False.
def max(a):
    if a == []: 
        return False
    else:
        mayor = a[0] 
        for i in range (len(a)):
            if a[i] > mayor:
                mayor = a[i]
        return mayor
x = max([])
print(x)
y = max([6,3,7,-2,1,2]) 
print(y) 
z = max([-1, -6, -4, -2, -7, -7, -4, -123, -34.4 -2]) 
print(z)
# Análisis final : crea una función que tome una lista y devuelva un diccionario que 
# tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
    # Ejemplo: ultimate_analysis ([37,2,1, -9]) 
    # debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}
def analisis (a): 
    return {'Total : ', sumatotal(a),
            'Promedio : ', prom(a),
            'Mínimo : ', min(a),
            'Máximo : ', max(a),
            'Longitud : ', longlista(a),}
y = analisis([6,3,7,-2,1,2]) 
print(y)
z = analisis([-1, -6, -4, -2, -7, -7, -4, -123, -34.4 -2]) 
print(z) 
# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. 
# Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def invertir (a):
    for i in range (len(a)//2): #recorre la primera mitad de la lista para intercambiarla con la otra mitad 
        aux = a[i]  # para la primera iteración, este auxiliar guarda el valor de a[0] - en la 2da iteración, guarda a[1]
        a[i] = a[len(a)-1-i] # reemplaza a[0] con el último valor de la lista - a[4-1-1]
        a[len(a)-1-i] = aux # reemplaza el último valor con lo guardado en aux - a[2] --> a[1]
    return a
y = invertir([37,2,1, -9]) 
print(y)
z = invertir([-1, -6, -4, -2, -7, -7, -4, -123, -34.4, -2]) 
print(z)