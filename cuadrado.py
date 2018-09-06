import math

tumple1 = (1, 1)
tumple2 = (4, 1)
tumple3 = (1, 3)
tumple4 = (8, 3)

result = []

def principal(tumple1, tumple2, tumple3, tumple4):
    firstResult = calculateDistances(tumple1, tumple2 + tumple3 + tumple4)
    secondResult = calculateDistances(tumple2, tumple1 + tumple3 + tumple4)
    threeResult = calculateDistances(tumple3, tumple2 + tumple1 + tumple4)
    fourResult = calculateDistances(tumple4, tumple2 + tumple3 + tumple1)  

    isSquare = 0 
    for x in firstResult:
        if x in secondResult and x in threeResult and x in fourResult:
            isSquare = 1
            break

    if isSquare == 1:
        print("Es un cuadrado")
    else:
        print("No es un cuadrado")
        
def calculateDistances(argument, lista):
    result = []
    result.append(distanceFormula(argument[0], lista[0], argument[1], lista[1]))
    result.append(distanceFormula(argument[0], lista[2], argument[1], lista[3]))
    result.append(distanceFormula(argument[0], lista[4], argument[1], lista[5]))
    return result

def distanceFormula(x1, x2, y1, y2):
    cuadradoX = cuadrado(x2, x1)
    cuadradoY = cuadrado(y2, y1)
    sumCuadrado = cuadradoX + cuadradoY
    return math.sqrt(sumCuadrado)

def cuadrado(argument1, argument2):
    resta = (argument1 - argument2)
    return (resta * resta)

principal(tumple1, tumple2, tumple3, tumple4)