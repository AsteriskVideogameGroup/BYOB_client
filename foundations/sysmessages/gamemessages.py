from enum import Enum


class GameMessages(Enum):
    # eventi dal server
    MAPREADY: int = 1  # la mappa è pronta per il game
    GAMECREATED: int = 2  # è stato creato un game in cui il playter può giocare

    # eventi user input
    INITUNRANKEDGAME: int = 3  # il giocatore vuole iniziare una partita unranked
    INITRANKEDGAME: int = 4
    EXITPROGRAM: int = 5  # esci da tutto il programma
    NEXT: int = 6
    PREVIOUS: int = 7
    ACCEPT: int = 8
    RANKEDMODESELECTED: int = 9
    UNRANKEDMODESELECTED: int = 10
    BOBCHOSEN: int = 11


