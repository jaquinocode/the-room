class Room:

  def __init__(self):
    self.room_number = 0
    self.room_things = {
      'room': {
        'look': 'A room.',
        'pickup': 'Don\'t be ridiculous.',
        'approach': 'You\'re already in the room, man. No need.',
        'hit': 'You kick and hit around the room. Nothing happens.',
        'synonyms': {'space', 'area', 'environment', 'everything'}
      }
    }


class Room1(Room):

  def __init__(self):
    super().__init__()
    self.room_number = 1
    self.room_things['room']['look'] = 'You can see a bed and a desk with a phone resting on top. There\'s nothing else.'
    self.room_things.update({
      'phone': {
        'look': "A small cheap phone. It appears to be ringing.",
        'pickup': "You have taken the phone. It is still ringing. Enter 'i' or 'inventory' at any time to bring up your inventory.",
        'approach': "You have approached the phone.",
        'answer': "You answer it, the voice on the other line says 'You find yourself in a room.' As the voice speaks the room around you starts to shift. You are now in a completely different room.",
        'hit': "You hit the phone. Nothing happens.",
        'synonyms': {'device', 'cellphone'}
      },
      'desk': {
        'look': "A flimsy wooden desk with a phone resting on it.",
        'pickup': "Please. This desk is too heavy to pick up and take with you.",
        'approach': "You have approached the desk.",
        'hit': "You hit the desk. That was pointless.",
        'synonyms': {'table'}
      },
      'bed': {
        'look': "The bed you woke up from. Not sure how you got here.",
        'pickup': "The bed's too big for that.",
        'approach': "You have approached the bed.",
        'sleep': "But you've just woke up. Get your head in the game, man!",
        'hit': "You attack and hit the bed mercilessly. Nothing happens.",
        'jump': "You jump on the bed for a bit, smiling and having a grand 'ol time. Wow that was fun.",
        'synonyms': {'mattress', 'sheets', 'pillow'}
      }
    })

  def print_things(self):
    print(self.room_things)