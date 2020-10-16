from Classes.Game import Game

def main():
  game = Game()
  print('You find yourself in a room.')

  while game.is_active:
    response = game.parse(input())
    print('\n' + response)


if __name__ == '__main__':
  main()