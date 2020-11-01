# from modules.room import Room1


class Game:
    def __init__(self):
        self.is_active = True
        self.curr_level = Level_1()
        self.all_things = {
            "room_1": {
                "room": {
                    "look": (
                        "You can see a bed and a desk with a phone resting on top. "
                        "There's nothing else."
                    ),
                    "pickup": "Don't be ridiculous.",
                    "approach": "You're already in the room, man. No need.",
                    "hit": "You kick and hit around the room. Nothing happens.",
                    "synonyms": {
                        "floor",
                        "wall",
                        "walls",
                        "ceiling",
                        "space",
                        "area",
                        "environment",
                    },
                },
                "phone": {
                    "look": "A small cheap phone. It appears to be ringing.",
                    "pickup": (
                        "You have taken the phone. It is still ringing. Enter "
                        "'i' or 'inventory' at any time to bring up your inventory."
                    ),
                    "approach": "You have approached the phone.",
                    "answer": (
                        "You answer it, the voice on the other line says 'You find "
                        "yourself in a room.' As the voice speaks, the room around you"
                        " starts to shift. You are now in a completely different room."
                    ),
                    "hit": "You hit the phone. Nothing happens.",
                    "synonyms": {"device", "cellphone"},
                },
                "desk": {
                    "look": "A flimsy wooden desk.",
                    "pickup": (
                        "Please. This desk is too heavy to pick up and take with you."
                    ),
                    "approach": "You have approached the desk.",
                    "hit": "You hit the desk. That was pointless.",
                    "synonyms": {"table"},
                },
                "bed": {
                    "look": "The bed you woke up from. Not sure how you got here.",
                    "pickup": "The bed's too big for that.",
                    "approach": "You have approached the bed.",
                    "sleep": "But you've just woke up. Get your head in the game, man!",
                    "hit": "You attack and hit the bed mercilessly. Nothing happens.",
                    "jump": (
                        "You jump on the bed for a bit, smiling and having a grand 'ol "
                        "time. Wow that was fun."
                    ),
                    "synonyms": {"mattress", "sheets", "pillow"},
                },
            },
            "room_2": {
                "room": {
                    "look": (
                        "Behind you is a whiteboard. To the left of you is a "
                        "door.\nWritten on the floor are markings that read 'THREE "
                        "BLANKS FOR THREE NUMBERS. THERE IS NO ROOM FOR FOUR.'"
                    ),
                    "pickup": "Don't be ridiculous.",
                    "approach": "You're already in the room, man. No need.",
                    "synonyms": {
                        "floor",
                        "wall",
                        "walls",
                        "ceiling",
                        "space",
                        "area",
                        "environment",
                    },
                },
                "whiteboard": {
                    "look": (
                        "A large whiteboard. It has this written on it:\n\n__ / __ = "
                        "__\n\n(Type and enter 'write' at any time if you wish to fill "
                        "in the blanks.)"
                    ),
                    "pickup": "Lol. You can't pick up the whiteboard, silly.",
                    "approach": "You approach the whiteboard.",
                    "synonyms": {"board", "canvas"},
                },
                "cone": {
                    "look": "Some paper cones.",
                    "pickup": "You pick up the cone and toss it aside.",
                    "approach": "You approach the cone.",
                    "synonyms": {"cones"},
                },
                "door": {
                    "look": "A normal door.",
                    "pickup": (
                        "You are physically unable to pick up and take a door with you "
                        "unfortunately."
                    ),
                    "approach": "You approach the door.",
                    "open": "You have opened the door and walked in.",
                    "synonyms": {"gate"},
                },
                "key": {
                    "look": "A pretty key.",
                    "pickup": "You have picked up the key.",
                    "approach": "You approach the key.",
                    "synonyms": {"keys"},
                },
            },
            "room_3": {
                "room": {
                    "look": (
                        "Except for a piece of chalk you see rested on the center of "
                        "the floor, this room is completely bare."
                    ),
                    "pickup": "Don't be ridiculous.",
                    "approach": "You're already in the room, man. No need.",
                    "synonyms": {
                        "floor",
                        "wall",
                        "walls",
                        "ceiling",
                        "space",
                        "area",
                        "environment",
                    },
                },
                "chalk": {
                    "look": (
                        "A normal piece of chalk. There is a sticky note attached to "
                        "it."
                    ),
                    "pickup": "You have picked up the chalk.",
                    "approach": "You have approached the chalk.",
                    "synonyms": {"chalks", "chlak"},
                },
                "note": {
                    "look": (
                        "A sticky note with a message written on it:\nYOU HAVE FOUND "
                        "THE KEY.\nNOW FIND THE DOOR."
                    ),
                    "approach": "You're already in the room, man. No need.",
                    "read": "YOU HAVE FOUND THE KEY.\nNOW FIND THE DOOR.",
                    "synonyms": {
                        "paper",
                        "message",
                        "writing",
                        "writings",
                        "markings",
                        "marks",
                        "sticky",
                    },
                },
                "door": {
                    "look": (
                        "Some chalk markings that have created the appearance of a "
                        "door."
                    ),
                    "pickup": "Don't be ridiculous.",
                    "approach": "You have approached the door.",
                    "draw": "You draw the door.",
                    "open": "You open the door and walk in.",
                    "synonyms": {"gate"},
                },
            },
            "room_4": {
                "room": {
                    "look": (
                        "The north wall that's facing me has some strange "
                        "writings/marks on it. There is a billiards table in the center"
                        " of the room in front of you."
                    ),
                    "pickup": "Don't be ridiculous.",
                    "approach": "You're already in the room, man. No need.",
                    "synonyms": {
                        "floor",
                        "wall",
                        "walls",
                        "ceiling",
                        "space",
                        "area",
                        "environment",
                    },
                },
                "wall": {
                    "look": "        3 -> 1 -> 4",
                    "pickup": "Don't be ridiculous.",
                    "approach": "You have approached the wall.",
                    "hit": "You hit the wall. Completely useless.",
                    "read": "3 -> 1 -> 4",
                    "synonyms": {
                        "walls",
                        "marks",
                        "markings",
                        "writing",
                        "writings",
                        "drawing",
                        "drawings",
                        "symbol",
                        "hint",
                        "numbers",
                    },
                },
                "table": {
                    "look": (
                        "A billiards table. No balls or any functionality to speak of. "
                        "It would probably be an ideal location to PLACE objects here."
                    ),
                    "pickup": "Don't be silly.",
                    "approach": "You have approached the table.",
                    "read": "insert symbol here",
                    "synonyms": {"desk"},
                },
                "rack": {
                    "look": "A large triangle rack used to play pool.",
                    "pickup": "You picked up the large triangle rack.",
                    "approach": "You have approached the large triangle rack.",
                    "place": (
                        "You have placed the large triangle rack down on the table."
                    ),
                    "synonyms": {"triangle"},
                },
                "clock": {
                    "look": "A medium-sized circular clock.",
                    "pickup": "You picked up the medium-sized clock.",
                    "approach": "You have approached the clock.",
                    "place": (
                        "You have placed the medium-sized clock down on the table."
                    ),
                    "synonyms": {"circle", "circular"},
                },
                "cube": {
                    "look": (
                        "A small rubix cube. Unfortunately doesn't work anymore and "
                        "might as well be a paperweight."
                    ),
                    "pickup": "You picked up the small rubix cube.",
                    "approach": "You have approached the small rubix cube.",
                    "place": "You have placed the small rubix cube down on the table.",
                    "synonyms": {"rubix", "square"},
                },
                "end sequence": {
                    "end text": (
                        "A small rumbling starts to occur and the floor falls.\nYou "
                        "land clumsily.\n\nYou are no longer in a room. You are "
                        "outside.\n\nTHE END."
                    )
                },
            },
        }

    def process_input(self, raw_input):
        # unintrusive cleansing & caps normalization
        clean_input = raw_input.lower().strip()

        return self.curr_level.process_cleaned_input(clean_input)

    def parse(self, raw_input):
        user_input = raw_input.lower().strip()
        # handle shortcut inputs as a priority
        if user_input in {"l", "look", "look around"}:
            return self.get_response("look", "room")
        elif user_input in {"i", "inventory"}:
            return self.get_inventory_text()

        input_words = user_input.split()
        action, thing = self.find_action_thing(input_words)
        return self.get_response(action, thing)

    def get_response(self, action, thing):
        # if theres a game function for this input, do that, otherwise just get the
        # text resource
        try:
            do_action = self.game_functions[thing][action]
        except KeyError:
            response = self.request_text(action, thing)
        else:
            response = do_action()
        return response + "\n"

    def request_text(self, action, thing):
        INVALID_ACTION = f"You can't do that to the {thing}."

        response = None
        if action and thing:
            response = self.room_things[thing].get(action, INVALID_ACTION)
        elif not action and thing:
            response = f"Not sure what you want to do to the {thing}."
        elif action and not thing:
            response = f"I can't do the '{action}' action on that."
        elif not action and not thing:
            response = (
                "Couldn't identify any eligible action or object in your command.\nA "
                "good command is something like:\nlook at desk"
            )
        return response

    def find_action_thing(self, input_words):
        action, thing = "", ""
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
                    if word == thing_key or word in thing_properties["synonyms"]:
                        thing = thing_key
                        thing_Found = True

        return action, thing

    def get_inventory_text(self):
        inventory_text = "Inventory:\n"
        inventory_text += (
            "\n".join(self.inventory.keys()) if self.inventory else "empty"
        )
        return inventory_text + "\n"

    def go_to_next_room(self):
        if self.curr_room_number < self.total_rooms:
            self.curr_room_number += 1
        self.room_things = self.all_things[f"room_{self.curr_room_number}"]


class Level_1:
    def __init__(self):
        self.action_synonyms = {
            "look": {
                "l",
                "look",
                "look around",
                "see",
                "view",
                "survey",
                "observe",
                "observe around",
                "inspect",
                "scrutinize",
                "examine",
                "investigate",
                "check",
                "checkout",
                "review",
                "monitor",
                "search",
                "watch",
                "identify",
                "analyze",
                "peek",
                "describe",
                "find",
            },
            "pickup": {
                "pick up",
                "pick",
                "pickup",
                "take",
                "grab",
                "weild",
                "hold",
                "lift",
            },
            "approach": {"approach", "go", "goto", "reach", "walk"},
            "answer": {"answer", "respond", "talk"},
            "sleep": {"sleep", "rest"},
            "hit": {
                "hit",
                "kick",
                "smack",
                "slap",
                "punch",
                "pound",
                "fight",
                "headbutt",
                "attack",
            },
            "open": {"open", "unlock", "enter"},
            "help": {"h", "help"},
            "exit": {"exit", "quit"},
            "read": {"read"},
            "draw": {"draw", "illustrate", "paint", "inscribe", "mark"},
            "place": {"place", "put", "set", "lie"},
            "jump": {"bounce"},
        }
        self.things = {
            "room": {
                "look": (
                    "You can see a bed and a desk with a phone resting on top. "
                    "There's nothing else."
                ),
                "pickup": "Don't be ridiculous.",
                "approach": "You're already in the room, man. No need.",
                "hit": "You kick and hit around the room. Nothing happens.",
                "synonyms": {
                    "floor",
                    "wall",
                    "walls",
                    "ceiling",
                    "space",
                    "area",
                    "environment",
                },
            },
            "phone": {
                "look": "A small cheap phone. It appears to be ringing.",
                "pickup": (
                    "You have taken the phone. It is still ringing. Enter "
                    "'i' or 'inventory' at any time to bring up your inventory."
                ),
                "approach": "You have approached the phone.",
                "answer": (
                    "You answer it, the voice on the other line says 'You find "
                    "yourself in a room.' As the voice speaks, the room around you"
                    " starts to shift. You are now in a completely different room."
                ),
                "hit": "You hit the phone. Nothing happens.",
                "synonyms": {"device", "cellphone"},
            },
            "desk": {
                "look": "A flimsy wooden desk.",
                "pickup": (
                    "Please. This desk is too heavy to pick up and take with you."
                ),
                "approach": "You have approached the desk.",
                "hit": "You hit the desk. That was pointless.",
                "synonyms": {"table"},
            },
            "bed": {
                "look": "The bed you woke up from. Not sure how you got here.",
                "pickup": "The bed's too big for that.",
                "approach": "You have approached the bed.",
                "sleep": "But you've just woke up. Get your head in the game, man!",
                "hit": "You attack and hit the bed mercilessly. Nothing happens.",
                "jump": (
                    "You jump on the bed for a bit, smiling and having a grand 'ol "
                    "time. Wow that was fun."
                ),
                "synonyms": {"mattress", "sheets", "pillow"},
            },
        }
        self.functions = {
            "phone": {
                "pickup": self.pickup_phone,
                "answer": self.answer_phone,
            },
        }
        self.level_number = 1
        self.inventory = []

    def process_cleaned_input(self, clean_input):
        # handle shortcut inputs as a priority
        if clean_input in {"l", "look", "look around"}:
            return self.get_response("look", "room")

        input_words = clean_input.split()
        action, thing = self.find_action_thing(input_words)
        return self.get_response(action, thing)

    def find_action_thing(self, input_words):
        action, thing = "", ""
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
                for thing_key, thing_props in self.things.items():
                    if word == thing_key or word in thing_props["synonyms"]:
                        thing = thing_key
                        thing_Found = True

        return action, thing

    def get_response(self, action, thing):
        # if theres a game function for this input, do that, otherwise just get the
        # text resource
        try:
            do_action = self.functions[thing][action]
        except KeyError:
            response = self.request_text(action, thing)
        else:
            response = do_action()
        return response + "\n"

    def request_text(self, action, thing_name):
        INVALID_ACTION = f"You can't do that to the {thing_name}."

        response = None
        if action and thing_name:
            response = self.things[thing_name].get(action, INVALID_ACTION)
        elif not action and thing_name:
            response = f"Not sure what you want to do to the {thing_name}."
        elif action and not thing_name:
            response = f"I can't do the '{action}' action on that."
        elif not action and not thing_name:
            response = (
                "Couldn't identify any eligible action or object in your command.\nA "
                "good command is something like:\nlook at desk"
            )
        return response

    def go_to_next_room(self):
        # TODO: magic num
        # TODO: this func should probably be passed from Game, so Game decides what to 
        # do
        if self.level_number < 4:
            self.level_number += 1

    # this section has all the specific game actions that need to be expressed as
    # functions since they need to do things other than just give back the string
    # resource to the player
    def pickup_phone(self):
        if "phone" in self.inventory:
            return "You already have the phone."

        response = self.request_text("pickup", "phone")

        # move phone object to inventory
        self.inventory["phone"] = self.room_things["phone"]
        del self.room_things["phone"]
        # remove no longer required entries
        del self.inventory["phone"]["pickup"]
        del self.inventory["phone"]["approach"]
        # update environment description
        self.room_things["room"][
            "look"
        ] = "You can see a bed and a desk. There's nothing else."
        # picking up phone function no longer needed
        del self.game_functions["phone"]["pickup"]

        return response

    def answer_phone(self):
        self.go_to_next_room()
        self.inventory.clear()
        return (
            "You answer it, the voice on the other line says 'You find yourself in "
            "a room.' As the voice speaks the room around you starts to shift. You "
            "are now in a completely different room."
        )