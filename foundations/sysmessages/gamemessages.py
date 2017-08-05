from enum import Enum


class GameMessages(Enum):
    # eventi dal server
    MAPREADY: int = 1  # la mappa è pronta per il game
    GAMECREATED: int = 2  # è stato creato un game in cui il playter può giocare

    # eventi user input
    INITUNRANKEDGAME: int = 3  # il giocatore vuole iniziare una partita unranked
    EXITPROGRAM: int = 4  # esci da tutto il programma
    NEXT: int = 5
    PREVIOUS: int = 6
    ACCEPT: int = 7
    MODESELECTED: int = 8


