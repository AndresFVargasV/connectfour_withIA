class Tablero:
    def __init__(self, fila: int, columna: int):
        self.fila = fila
        self.columna = columna
        self.matriz = self.hacer_matriz()
        
    # Metodo para devolver el tablero de juego 
    def hacer_matriz(self) -> list:
        return [[0] * self.columna for _ in range(self.fila)]
    
    # Metodo para verificar el jugador ganador
    def verificar_ganador(self, jugador) -> bool:
        valor_juego = jugador.valor_juego
        
        # Verificar filas
        for fila in self.matriz:
            for col in range(self.columna - 3):
                if all(cell == valor_juego for cell in fila[col:col+4]):
                    return True
        
        # Verificar columnas
        for col in range(self.columna):
            for row in range(self.fila - 3):
                if all(self.matriz[row+i][col] == valor_juego for i in range(4)):
                    return True
        
        # Verificar diagonales ascendentes
        for row in range(self.fila - 3):
            for col in range(self.columna - 3):
                if all(self.matriz[row+i][col+i] == valor_juego for i in range(4)):
                    return True
        
        # Verificar diagonales descendentes
        for row in range(3, self.fila):
            for col in range(self.columna - 3):
                if all(self.matriz[row-i][col+i] == valor_juego for i in range(4)):
                    return True
        
        return False
        
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

while True:
    
    if tablero_juego.verificar_ganador(B):
        print(f"¡El jugador {B.nombre} ha ganado!")
        break
    else:
        B.jugar(tablero_juego.matriz)
        for filas in tablero_juego.matriz:
            print(filas)

    
