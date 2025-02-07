from random import random
import random

import board


class Player:
    """
    Spieler Klasse für VierGewinnt Klasse

    Diese Klasse stellt das Grundgerüst für die Spielerobjekte dar.
    """
    def __init__(self, player_id : str):
        """
        Parameters
        ----------
        player_id : str
            Symbol des Spielers, z. B. "X" oder "O".
        """

        self.player_id = player_id
        self.current_move = 0


    def get_move(self):
        """
        Fordert den Spieler auf, eine Spalte für seinen Spielstein auszuwählen.

        Returns
        -------
        None
        """
        while True:
            current_move = input(f"Spieler {self.player_id} Enter your move: (Enter '0' to exit)")
            if current_move.isdigit(): #Prüft, ob die Eingabe eine Zahl ist
                current_move = int(current_move)
                if current_move == '0':
                    self.current_move = 0
                    break
                if 1 <= int(current_move) <= 7:
                        self.current_move = current_move
                        break
            print("Nur Zahlen zwischen 1 & 7 bitte :)")




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
        Wählt automatisch eine zufällige gültige Spalte für den AI-Spieler.

        Returns
        -------
        None

        """
        current_move = random.randint(1, 7)
        self.current_move = current_move
        print(f"beep boop ich nehm die + {self.current_move}")



if __name__ == "__main__":
    pass