from player import Player


class Board:

    """Board Klasse zur Initialisierung und Anzeige des Spielfelds

    TODO: Public Attribute hier Dokumentieren

    Attribute
    ----------
    rows = statischer Wert 6
        initialisiert Reihenwert mit 6.
    columns = statischer Wert 7
        initialisiert Reihenwert mit 7.
    class_gameboard - initialisiert leere Liste
    Anschließend wird leeres Board erstellt im Konstruktor
    Wird als private Attribute umgesetzt, da show_board/update_board Methode für Darstellung erstellt wurde
   TODO: falls irrelevant (aufgrund anderer noch zu implementierenden Methoden) anpassen

    """

    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.__class_gameboard = []
        for columns in range(self.columns):
            self.__class_gameboard.append([])

    def __repr__(self):
        return f"Board: {self.__class_gameboard}"


    def show_board(self):
        """
        Methode zur visuell "ansprechenden" Darstellung des Boards
        """
        for row in range(self.rows):
            row_string = ""
            for column in self.__class_gameboard:
                cell_index = self.rows - row - 1
                if len(column) > cell_index:
                    symbol_player = column[cell_index]
                else:
                    symbol_player = " "
                row_string += "| " + symbol_player + " "
            row_string += "|"
            print(row_string)



    def update_board(self, player: Player) -> bool:
        """
        Überprüfung auf Zug-Möglichkeit und Update des Boards mit aktuellen Zug
        Parameters
        ----------
        player: Player Objekt

        Returns
        -------
        True: Zug ist möglich + Board wurde abgedated
        False: Zug ist nicht möglich
        """
        desired_column = player.current_move
        column_to_update = self.__class_gameboard[desired_column - 1]
        if len(column_to_update) < self.rows:
            self.__class_gameboard[desired_column - 1].append(player.player_id)
            return True
        else:
            return False


if __name__ == "__main__":
    board_test1 = Board()
    board_test1.show_board()






