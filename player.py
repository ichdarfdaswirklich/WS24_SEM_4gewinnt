

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

    def get_move(self):
        pass

if __name__ == "__main__":
    pass