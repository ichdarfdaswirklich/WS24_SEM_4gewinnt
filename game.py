# Platzhalter für Hauptdatei

from board import Board



class VierGewinnt:
    """VierGewinnt Python Terminal Spiel

    Gewinn-Voraussetzung: 4 Token eines Spielers aneinander.
    Horizontal, vertikal oder diagonal.
    Spielbrett: 7 Zeilen, 6 Spalten

    Zwei Spieler (Human oder AI) setzen abwechselnd ihre Tokens.
    Nach jedem Zug wird überprüft, ob Gewinn-Voraussetzung erfüllt ist.
    Falls ja - Spiel endet.
    Falls nein - Spielerwechsel.


    """
    def __init__(self, player1= "HUMAN1", player2 = "HUMAN2", player3 ="AI"):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3



    def get_player_move(self):
        pass

    def play_game(self):
        """
        Hauptfunktion für Spielablauf
        Returns
        -------
        Reihenfolge:
        Willkommens Nachricht
        Board initialisieren


        """
        Board.welcome_message()
        Board.display_board()





    def player_switch(self):
        pass



if __name__ == "__main__":
    game_test = VierGewinnt()
    game_test.play_game()
