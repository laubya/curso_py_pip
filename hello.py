print('Hola desde mi compu')

def solution(num):
    counter = 0
    
    # Ajustamos el número según si es par o impar
    if num % 2 == 0:
        while num > 1:
            num /= 2
            counter += 1
    else:
        num += 1
        while num > 1:
            num /= 2
            counter += 1
    
    return counter

# Ejemplo de uso
resultado = solution(5)
print(f'El resultado es: {resultado}')