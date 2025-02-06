

class Player:
    def __init__(self, player_id : str):
        self.player_id = player_id
        self.current_move = 0


    def get_move(self):
        """
        Gewünschter Zug wird von Player abgefragt
        ________
        Wert wird dem Attribut self.current_move übergeben, dieses wird im Game Loop auf Zug-Möglichkeit überprüft
        """
        current_move = input("Enter your move: (Enter '0' to exit)")
        if "0" <= current_move <= "7":
            self.current_move = int(current_move)






    def check_for_win(self):
        pass



class PlayerAI:
    def __init__(self):
        pass

    def get_move(self):
        pass

if __name__ == "__main__":
    pass