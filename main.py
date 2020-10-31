from modules import text_game


def main():
    game = text_game.Game()
    print("You find yourself in a room.")

    while game.is_active:
        response = game.parse(input())
        print(response)


if __name__ == "__main__":
    main()
