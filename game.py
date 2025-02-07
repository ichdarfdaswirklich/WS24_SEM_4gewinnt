
from board import Board
from player import Player, PlayerAI



class VierGewinnt:
    """
    VierGewinnt Python Terminal Spiel
    Gewinn-Voraussetzung: 4 Token eines Spielers aneinander.
    Horizontal, vertikal oder diagonal.
    Spielbrett: 7 Zeilen, 6 Spalten

    Zwei Spieler (Human oder AI) setzen abwechselnd ihre Tokens.
    Nach jedem Zug wird überprüft, ob Gewinn-Voraussetzung erfüllt ist.
    Falls ja - Spiel endet.
    Falls nein - Spielerwechsel.
    """

    def welcome_message(self):
        """
        Gibt eine Willkommensnachricht im Terminal aus.

        Returns
        -------
        None
        """
        creators = "Vici + Angie haben ihr bestes gegeben"
        print("---------------------------------------")
        print("---------------------------------------")
        print("---------------------------------------")

        print("---------------------------------------")
        print("Willkommen zu unserem verzweifelten Versuch 4 gewinnt zu programmieren")
        print("---------------------------------------")
        print(creators)
        print("---------------------------------------")
        print("---------------------------------------")




    def game_loop(self):
        """
        Hauptmethode für den Spielablauf von VierGewinnt.

        Returns
        -------
        None
        """
        self.welcome_message()

        game_is_active = True
        active_board = Board()

        player_list = []
        player_ai_list = []
        player1 = Player("X")
        player2 = Player("O")
        playerai = PlayerAI()
        player_list.append(player1)
        player_list.append(player2)
        player_ai_list.append(player1)
        player_ai_list.append(playerai)
        chose_gamestyle = input("Mensch oder AI? (Enter M oder A)")
        while game_is_active:
            if chose_gamestyle == "M":
                for current_player in player_list:  # Spielerwechsel nach jedem Zug
                    active_board.show_board()
                    current_player.get_move()
                    if current_player.current_move == 0:
                        game_is_active = False  # Beenden, falls der Spieler aufhören will
                        break
                    if active_board.update_board(current_player):
                        if active_board.check_for_win(current_player.player_id):
                            active_board.show_board()
                            print(f"Spieler {current_player.player_id} hat gewonnen!")
                            game_is_active = False
                            break
            elif chose_gamestyle == "A":
                for current_player in player_ai_list:  # Spielerwechsel nach jedem Zug
                    active_board.show_board()
                    current_player.get_move()
                    if current_player.current_move == 0:
                        game_is_active = False  # Beenden, falls der Spieler aufhören will
                        break
                    if active_board.update_board(current_player):
                        if active_board.check_for_win(current_player.player_id):
                            active_board.show_board()
                            print(f"Spieler {current_player.player_id} hat gewonnen!")
                            game_is_active = False
                            break



if __name__ == "__main__":
    gametest = VierGewinnt()
    gametest.game_loop()

