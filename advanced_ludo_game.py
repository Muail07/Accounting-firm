# advanced_ludo_game.py
import random

class LudoPlayer:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces = [0, 0, 0, 0]  # Pieces positions (0 means at home)

    def roll_dice(self):
        return random.randint(1, 6)

    def move_piece(self, piece_index, steps):
        if self.pieces[piece_index] == 0 and steps == 6:
            self.pieces[piece_index] = 1
        elif self.pieces[piece_index] != 0:
            self.pieces[piece_index] += steps

    def has_won(self):
        return all(pos >= 57 for pos in self.pieces)  # Assuming 57 is the end position

class LudoGame:
    def __init__(self):
        self.players = []
        self.current_turn = 0
        self.board_size = 52  # Main track size

    def add_player(self, name, color):
        self.players.append(LudoPlayer(name, color))

    def play_turn(self):
        player = self.players[self.current_turn]
        print(f"{player.name}'s turn")
     
        dice_roll = player.roll_dice()
        print(f"{player.name} rolled a {dice_roll}")

        move_possible = False
        for i, pos in enumerate(player.pieces):
            if pos != 0 or dice_roll == 6:  # Piece can move
                move_possible = True
                break

        if not move_possible:
            print(f"{player.name} cannot move any piece")
        else:
            piece_to_move = int(input(f"{player.name}, choose a piece to move (0-3): "))
            player.move_piece(piece_to_move, dice_roll)

        if player.has_won():
            print(f"{player.name} has won the game!")
            return True

        if dice_roll != 6:
            self.current_turn = (self.current_turn + 1) % len(self.players)
        return False

    def play_game(self):
        while True:
            if self.play_turn():
                break

def main():
    game = LudoGame()
    game.add_player("Alice", "Red")
    game.add_player("Bob", "Blue")
    game.add_player("Charlie", "Green")
    game.add_player("Diana", "Yellow")
    game.play_game()

if __name__ == "__main__":
    main()
