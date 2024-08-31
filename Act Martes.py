palabras = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]
palabra = palabras.count("Python")
print(f'La palabra "Python" aprece {palabra} veces')

#----------------------------------#

frases = ["hola", "mundo", "python", "es", "genial"]

fraseM = []
for palabra in frases:
    nuevoM = ""
    for letra in palabra:
        if 'a' <= letra <= 'z':
            letraM = chr(ord(letra) - 32)
        else:
            letraM = letra
        nuevoM += letraM
    fraseM.append(nuevoM)

print(fraseM)

#----------------------------------#

palas4 = ["sol", "luna", "cielo", "mar", "estrella", "pez"]

palabrasf = []
for letras in palas4:
    if len(letras) >=4:
        palabrasf.append(letras)
print(palabrasf)

#----------------------------------#

numeros = [15, 22, 8, 34, 9, 6, 17]

numeromax = numeros [0]

for numero in numeros:
    if numero > numeromax:
        numeromax = numero

print(f'El numero maximo es {numeromax}')

#----------------------------------#

numerosx = [-3, 5, -7, 2, -8, 10, -4, 6]

positivo = 0
for pos in numerosx:
    if pos > 0:
        positivo += 1
print(f'hay {positivo} numeros positivos')

#----------------------------------#

numeroso = [1, 2, 3, 4, 5]

alreves = []

for i in range(len(numeroso) -1, -1, -1):
    alreves.append(numeroso[i])

print(alreves)

#----------------------------------#

numerosos = [4, 7, 2, 9, 3, 8, 5]

valores = len(numerosos)

suma = sum(numerosos)

promedio = round (suma / valores) 
print(f'El promedio es de {promedio}')