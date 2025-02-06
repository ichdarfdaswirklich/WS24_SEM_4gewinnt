from random import random
import random



class Player:
    """
    Spieler Klasse für VierGewinnt Klasse

    Diese Klasse stellt das Grundgerüst für die Spielerobjekte dar.
    """
    def __init__(self, player_id : str):
        """
        Initialisierung der Player Klasse

        Parameters
        ----------
        player_id
        """
        self.player_id = player_id
        self.current_move = 0


    def get_move(self):
        """
        Eingabeaufforderung an Spielerobjekt für gewünschte Spalte für Spielstein

        Returns
        -------

        """
        while True:
            current_move = input(f"Spieler {self.player_id} Enter your move: (Enter '0' to exit)")
            if len(current_move) == 1:
                if "0" <= current_move <= "7":
                    self.current_move = int(current_move)
                    break
            print("Ungültiger Input, try again")

    #TODO Implementieren, dass wenn Spalte voll ist, invalid move bei erneuter Auswahl erscheint


class PlayerAI(Player):
    """
    PlayerAI Klasse abgeleitet von Player Klasse.

    Einfache "KI" für valide Züge.
    """
    def __init__(self, player_id="O"):
        """
        Initialisierung der PlayerAI Klasse
        Parameters
        ----------
        player_id
            fixe Zuweisung von "O", da PlayerAI immer zweiter Spieler ist.
        """
        super().__init__(player_id)
        self.current_move = 0


    def get_move(self):
        """
        Automatische Eingabe einer random Zahl zwischen 1 und 7
        Returns
        -------

        """
        current_move = random.randint(1, 7)
        self.current_move = current_move
        print(f"beep boop ich nehm die + {self.current_move}")



if __name__ == "__main__":
    pass