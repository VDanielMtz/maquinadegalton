import random 
import matplotlib.pyplot as mt
numb= 100  # Número de bolitas que caerán
def main():
    nombrebarras=['Espacio 1', 'Espacio 2', 'Espacio 3', 'Espacio 4', 'Espacio 5']#definicion de nombres de columnas
    c1, c2, c3, c4, c5 = caidabolitas(numb)#rescate de valores 
    valores=[c1, c2, c3, c4, c5]#definicion de valores en la grafica 
    mt.bar(nombrebarras, valores)#funcion que grafica
    mt.xlabel('Espacios')#definicion de nombres
    mt.ylabel('Cantidad')
    mt.title('SIMULADOR DE MAQUINA DE GALTON')
    mt.show()#ejecucion de grafica 

def randomizarcaida():#funcion que genera numeros aleatorios 
    numcaida=random.randint(1, 5)#linea que genera numeros aleatorios con un rango de 1 al 5
    return numcaida#regreso de valor aleatorio
def caidabolitas (numb):#funcion que selecciona numeros 
    contf1=0#definicion de variables 
    contf2=0
    contf3=0
    contf4=0
    contf5=0
    for cont1 in range(numb):#ciclo for hasta el numero de bolitas 
        filaganadora=randomizarcaida()#rescate de valores aleatorios 
        if (filaganadora==1):#condicional que selecciona 
            contf1=contf1+1
        elif (filaganadora==2):
            contf2=contf2+1
        elif(filaganadora==3):
            contf3=contf3+1
        elif (filaganadora==4):
            contf4=contf4+1
        elif(filaganadora==5):
            contf5=contf5+1
    return contf1, contf2, contf3, contf4, contf5#regreso de valor 

if __name__ == "__main__":
    main() #llamada al metodo main 