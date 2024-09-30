import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")    
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):

    res = "Perdiste"
    if jugada_usuario == jugada_ordenador:
        res = "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        res = "Ganaste"
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        res = "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        res = "Ganaste"

    return res