from cgi import print_form


def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc


peso = float(input('ingrese su peso en kg'))
alturaEnCM = int (input('Ingrese su altura en cm'))
alturaEnMetros = alturaEnCM / 100
imc = calcularIMC(peso, alturaEnMetros)

print('Su IMC es de ' + str(imc))

if imc < 20:
    print ('Estado de delgadez')
if imc >= 20 and imc < 26:
    print('Peso normal') 
if imc >= 26 and imc < 30:
    print('Peso sobrepeso')       
if imc >= 30:
    print('Estado de obesidad')     







