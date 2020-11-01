from modules import text_game


def main():
    INTRO_TEXT = "You find yourself in a room."

    game = text_game.Game()
    print(INTRO_TEXT)

    while game.is_active:
        response = game.process_input(input())
        print(response)


if __name__ == "__main__":
    main()
