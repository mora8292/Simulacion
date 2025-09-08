import numpy as np

def marioLuigi(juegos=1, t=1):
    # Contadores de ganadores
    gana_mario = 0
    gana_luigi = 0
    empates = 0

    for i in range(juegos):   # Ciclo de juegos
        libreta = [0, 0]      # [Mario, Luigi]

        for j in range(t):    # Ciclo de turnos en un juego
            bros = np.random.randint(0, 10, 2)
            if bros[0] == bros[1]:
                libreta[0] += 2
                libreta[1] += 2
            elif (abs(bros[0] - bros[1])) % 2 == 0:
                libreta[0] += 1
            else:
                libreta[1] += 1

        # Decidir ganador de este juego
        if libreta[0] == libreta[1]:
            empates += 1
        elif libreta[0] > libreta[1]:
            gana_mario += 1
        else:
            gana_luigi += 1

    # Mostrar resultados finales
    print(f"Total de juegos: {juegos}")
    print(f"Ganó Mario en {gana_mario} juegos")
    print(f"Ganó Luigi en {gana_luigi} juegos")
    print(f"Hubo {empates} empates")

# Ejemplo: 300 juegos de 1 turno cada uno (simulación 6.1)
marioLuigi(300, 1)

# Ejemplo: 200 juegos de 10 turnos cada uno (simulación 6.2)
#marioLuigi(200, 10)

# Ejemplo: 1 juego de 100 turnos (simulación 6.3)
#marioLuigi(1, 100)

# Ejemplo: 1000 juegos de 2000 turnos cada uno (simulación 6.4)
#marioLuigi(1000, 2000)
