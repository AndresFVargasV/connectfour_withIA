class Tablero:
    def __init__(self, fila: int, columna: int):
        self.fila = fila
        self.columna = columna
        self.matriz = self.hacer_matriz()
        
    # Metodo para devolver el tablero de juego 
    def hacer_matriz(self) -> list:
        return [[0] * self.columna for _ in range(self.fila)]
        
class Jugador:
    def __init__(self, nombre: str, valor_juego: int, turno: int):
        self.nombre = nombre
        self.valor_juego = valor_juego
        self.turno = turno
        
        
    #Metodo para jugar y validar que la columna este disponible
    def jugar(self, tablero):
        colunma_juego = int(input('Ingrese la columna de juego: '))
        cont_colum = 0
        
        for i in range(len(tablero) - 1, -1, -1):
            if tablero[i][colunma_juego] != 0:
                cont_colum += 1
                if cont_colum == len(tablero):
                    print("Columna llena, elija otra")
                    return  # Salir de la función si la columna está llena
            else:
                # Aquí deberías tener la lógica para elegir el valor del juego (1 o 2)
                tablero[i][colunma_juego] = self.valor_juego
                break  # Salir del bucle una vez que se coloca la ficha

            
#Creación de jugadores
A = Jugador("A", 1, 1)
B = Jugador("B", 2, 2)

# Creación tablero de juego con clases
tablero_juego = Tablero(6, 7)

while(True):
    B.jugar(tablero_juego.matriz)

    for filas in tablero_juego.matriz:
        print(filas)