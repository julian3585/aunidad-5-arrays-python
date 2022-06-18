from abc import ABCMeta

class edad(ABCMeta):

    @staticmethod
    def calcularEdad(edadActual, años):
        edadFutura = edadActual + años

        return [edadFutura]

class pruebaArchivos:
    def leerArchivos(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split("#"))
        file.close()
        for f in range(0,len(lineas)):
            try:
                lineas_archivo.append(
                    [int(lineas[f][0]), int(lineas[f][1])])
            except ValueError:
                lineas_archivo.append([0,0])
        return lineas_archivo

    def chamu (self,lista):
        resultados = []
        for f in range(0, len(lista)):
            resultados.append(edad.calcularEdad(lista[f][0], lista[f][1]))
        return resultados

    def guardarResultados(self, entrada, resultados):
        file = open("resultados.txt", 'w')
        file.write('edadActual, años, edadFutura\n')
        for f in range(0,len(entrada)):
            linea = str(entrada[f][0]) + ';' + str(entrada[f][1]) + ';' + str(resultados[f][0]) + '\n'
            file.write(linea)
        file.close()

if __name__ == "__main__":
    prueba = pruebaArchivos()
    archivo = []
    archivo = prueba.leerArchivos("datos.txt")
    print(archivo)
    resultado = prueba.chamu(archivo)
    print(resultado)
    prueba.guardarResultados(archivo, resultado)



