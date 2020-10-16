from Classes.Room import Room1

class Game:
  inventory = []

  def __init__(self):
    self.is_active = True
    self.total_rooms = 4
    self.current_room_number = 1
    self.room_1 = Room1()
    self.action_synonyms = {
      'look': {'l', 'look', 'look around', 'see', 'view', 'survey', 'observe', 'observe around', 'inspect', 'scrutinize', 'examine', 'investigate', 'check', 'checkout', 'review', 'monitor', 'search', 'watch', 'identify', 'analyze', 'peek', 'describe', 'find'},
      'pickup': {'pick up', 'pick', 'pickup', 'take', 'grab', 'weild', 'hold', 'lift'},
      'approach': {'approach', 'go', 'goto', 'reach', 'walk'},
      'answer': {'answer', 'respond', 'talk'},
      'sleep': {'sleep', 'rest'},
      'hit': {'hit', 'kick', 'smack', 'slap', 'punch', 'pound', 'fight', 'headbutt', 'attack'},
      'open': {'open', 'unlock', 'enter'},
      'help': {'h', 'help'},
      'exit': {'exit', 'quit'},
      'read': {'read'},
      'draw': {'draw', 'illustrate', 'paint', 'inscribe', 'mark'},
      'place': {'place', 'put', 'set', 'lie'},
      'jump': {'bounce'}
    }
    self.all_things = {
      'Room1': {
        'room': {
          'look': "You can see a bed and a desk with a phone resting on top. There's nothing else.",
          'pickup': "Don't be ridiculous.",
          'approach': "You're already in the room, man. No need.",
          'hit': "You kick and hit around the room. Nothing happens.",
          'synonyms': {'floor', 'wall', 'walls', 'ceiling', 'space', 'area', 'environment'}
        },
        'phone': {
          'look': "A small cheap phone. It appears to be ringing.",
          'pickup': "You have taken the phone. It is still ringing. Enter 'i' or 'inventory' at any time to bring up your inventory.",
          'approach': "You have approached the phone.",
          'answer': "You answer it, the voice on the other line says 'You find yourself in a room.' As the voice speaks the room around you starts to shift. You are now in a completely different room.",
          'hit': "You hit the phone. Nothing happens.",
          'synonyms': {'device', 'cellphone'}
        },
        'desk': {
          'look': "A flimsy wooden desk.",
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
      },
      'Room2': {
        'room': {
          'look': "Behind you is a whiteboard. To the left of you is a door.\nWritten on the floor are markings that read 'THREE BLANKS FOR THREE NUMBERS. THERE IS NO ROOM FOR FOUR.'",
          'pickup': "Don't be ridiculous.",
          'approach': "You're already in the room, man. No need.",
          'synonyms': {'floor', 'wall', 'walls', 'ceiling', 'space', 'area', 'environment'}
        },
        'whiteboard': {
          'look': "A large whiteboard. It has this written on it:\n\n__ / __ = __\n\n(Type and enter 'write' at any time if you wish to fill in the blanks.)",
          'pickup': "Lol. You can't pick up the whiteboard, silly.",
          'approach': "You approach the whiteboard.",
          'synonyms': {'board', 'canvas'}
        },
        'cone': {
          'look': "Some paper cones.",
          'pickup': "You pick up the cone and toss it aside.",
          'approach': "You approach the cone.",
          'synonyms': {'cones'}
        },
        'door': {
          'look': "A normal door.",
          'pickup': "You are physically unable to pick up and take a door with you unfortunately.",
          'approach': "You approach the door.",
          'open': "You have opened the door and walked in.",
          'synonyms': {'gate'}
        },
        'key': {
          'look': "A pretty key.",
          'pickup': "You have picked up the key.",
          'approach': "You approach the key.",
          'synonyms': {'keys'}
        }
      },
      'Room3': {
        'room': {
          'look': "Except for a piece of chalk you see rested on the center of the floor, this room is completely bare.",
          'pickup': "Don't be ridiculous.",
          'approach': "You're already in the room, man. No need.",
          'synonyms': {'floor', 'wall', 'walls', 'ceiling', 'space', 'area', 'environment'}
        },
        'chalk': {
          'look': "A normal piece of chalk. There is a sticky note attached to it.",
          'pickup': "You have picked up the chalk.",
          'approach': "You have approached the chalk.",
          'synonyms': {'chalks', 'chlak'}
        },
        'note': {
          'look': "A sticky note with a message written on it:\nYOU HAVE FOUND THE KEY.\nNOW FIND THE DOOR.",
          'approach': "You're already in the room, man. No need.",
          'read': "YOU HAVE FOUND THE KEY.\nNOW FIND THE DOOR.",
          'synonyms': {'paper', 'message', 'writing', 'writings', 'markings', 'marks', 'sticky'}
        },
        'door': {
          'look': "Some chalk markings that have created the appearance of a door.",
          'pickup': "Don't be ridiculous.",
          'approach': "You have approached the door.",
          'draw': "You draw the door.",
          'open': "You open the door and walk in.",
          'synonyms': {'gate'}
        }
      },
      'Room4': {
        'room': {
          'look': "The north wall that's facing me has some strange writings/marks on it. There is a billiards table in the center of the room in front of you.",
          'pickup': "Don't be ridiculous.",
          'approach': "You're already in the room, man. No need.",
          'synonyms': {'floor', 'wall', 'walls', 'ceiling', 'space', 'area', 'environment'}
        },
        'wall': {
          'look': "        3 -> 1 -> 4",
          'pickup': "Don't be ridiculous.",
          'approach': "You have approached the wall.",
          'hit': "You hit the wall. Completely useless.",
          'read': "3 -> 1 -> 4",
          'synonyms': {'walls', 'marks', 'markings', 'writing', 'writings', 'drawing', 'drawings', 'symbol', 'hint', 'numbers'}
        },
        'table': {
          'look': "A billiards table. No balls or any functionality to speak of. It would probably be an ideal location to PLACE objects here.",
          'pickup': "Don't be silly.",
          'approach': "You have approached the table.",
          'read': "insert symbol here",
          'synonyms': {'desk'}
        },
        'rack': {
          'look': "A large triangle rack used to play pool.",
          'pickup': "You picked up the large triangle rack.",
          'approach': "You have approached the large triangle rack.",
          'place': "You have placed the large triangle rack down on the table.",
          'synonyms': {'triangle'}
        },
        'clock': {
          'look': "A medium-sized circular clock.",
          'pickup': "You picked up the medium-sized clock.",
          'approach': "You have approached the clock.",
          'place': "You have placed the medium-sized clock down on the table.",
          'synonyms': {'circle', 'circular'}
        },
        'cube': {
          'look': "A small rubix cube. Unfortunately doesn't work anymore and might as well be a paperweight.",
          'pickup': "You picked up the small rubix cube.",
          'approach': "You have approached the small rubix cube.",
          'place': "You have placed the small rubix cube down on the table.",
          'synonyms': {'rubix', 'square'}
        },
        'end sequence': {
          'end text': "A small rumbling starts to occur and the floor falls.\nYou land clumsily.\n\nYou are no longer in a room. You are outside.\n\nTHE END."
        }
      },
      'misc': {
        'inventory': {
          'synonyms': {'i'}
        }
      }
    }
    self.room_things = self.all_things['Room'+str(self.current_room_number)]


  def parse(self, raw_input):
    self.user_input = raw_input.lower()
    self.input_words = self.to_words(self.user_input)
    action, thing = self.find_action_thing(self.input_words)

    self.room_1.print_things()

    return self.get_response(action, thing)


  def get_response(self, action, thing):
    INVALID_ACTION = f'You can\'t do action \'{action}\' on the {thing}.'

    if self.user_input == 'inventory' or self.user_input in self.all_things['misc']['inventory']['synonyms']:
      response = 'Inventory:\n' + '\n'.join(self.inventory)
      return response

    if self.user_input in {'l', 'look', 'look around'}:
      action, thing = 'look', 'room'

    if not action and not thing:
      response = 'Couldn\'t identify any eligible action or object in your command. A good command is something like:\nlook at the desk'
    elif not action and thing:
      response = f'Not sure what you want to do to the {thing}.'
    elif action and not thing:
      response = f'I see you want to do the \'{action}\' action but am unable to find an object that you want to act on.\nFor instance, \'hit it\' won\'t work but \'hit desk\' will.'
    elif action and thing:
      response = self.room_things[thing].get(action, INVALID_ACTION)
      if callable(response):
        response = response()
    else:
      response = 'Runtime error in get response method.'

    print(f'{action=}\n{thing=}')

    return response


  def find_action_thing(self, input_words):
    action, thing = '', ''
    action_Found, thing_Found = False, False

    # iterating through words to check for a direct match with any actions and
    # objects available or their synonyms
    for word in input_words:
      if not action_Found:
        for action_key, synonyms in self.action_synonyms.items():
          if word == action_key or word in synonyms:
            action = action_key
            action_Found = True

      if not thing_Found:
        for thing_key, thing_properties in self.room_things.items():
          if word == thing_key or word in thing_properties['synonyms']:
            thing = thing_key
            thing_Found = True

    return action, thing


  def go_to_next_room(self):
    if self.current_room_number < self.total_rooms:
      self.current_room_number += 1
    self.room_things = self.all_things['Room'+str(self.current_room_number)]


  def to_words(self, user_input):
    return user_input.split()


  def R1_answer_phone(self):
    self.go_to_next_room()
    self.inventory.clear()
    return "You answer it, the voice on the other line says 'You find yourself in a room.' As the voice speaks the room around you starts to shift. You are now in a completely different room."

  def R1_pickup_phone(self):
    if 'phone' in self.inventory:
      return "You already have the phone."
    self.inventory.append('phone')
    return "You have taken the phone. It is still ringing. Enter 'i' or 'inventory' at any time to bring up your inventory."

  def R1_room_look(self):
    phone_phrase = '' if 'phone' in self.inventory else ' with a phone resting on top'
    return f"You can see a bed and a desk{phone_phrase}. There's nothing else."