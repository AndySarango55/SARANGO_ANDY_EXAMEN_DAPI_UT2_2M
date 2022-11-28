def convert_rgb2gray():
    """Esta funcion convierte una lista de pixeles de espectro de color a otra liste de pixeles en escala grises
    Parámetros:
                Rojo:
                Verde:
                Azul:
    Salidas:
                return: obtendremos una lista de valores de luminancia
                """

    rojo = ["r1, g1, b1"]
    verde = ["r2, g2, b2"]
    azul = ["rn, gn, bn"]

help(convert_rgb2gray)

def rgb2grey(r, g, b):
    """Esta funcion debe calcular la componente de luminancia

    Parametros:
                R: valor para el calculo de luminancia
                G: valor para el calculo de luminancia
                B: valor para el calculo de luminancia

    Salidas:
                Return: te devuelve el resultado del calculo
                
                """""

    return  int((r + g + b) / 3 )
help(rgb2grey)