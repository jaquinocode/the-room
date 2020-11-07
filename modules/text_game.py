class Game:
    def __init__(self):
        self.is_active = True
        self.curr_level = Level_1()
        """
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
        """

    def process_input(self, raw_input):
        # unintrusive cleansing & caps normalization
        cleaned_input = raw_input.lower().strip()

        return self.curr_level.process_cleaned_input(cleaned_input)


class Level_1:
    def __init__(self):
        self.LEVEL_NUMBER = 1
        # things and actions should never be changed, if thing/action no longer exists
        # then set that as one of its properties e.g. phone_exists: False
        self.THINGS = {"room", "phone", "desk", "bed"}
        self.ACTIONS = {
            "look",
            "pickup",
            "approach",
            "answer",
            "sleep",
            "hit",
            "open",
            "help",
            "exit",
            "read",
            "draw",
            "place",
            "jump",
        }
        self.FUNCTIONS = {
            "phone": {"pickup": self.pickup_phone, "answer": self.answer_phone},
        }
        self.SYNONYMS_FOR_ACTION = {
            "look": {
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
                "pickup",
                "pick up",
                "pick",
                "get",
                "take",
                "grab",
                "weild",
                "hold",
                "lift",
            },
            "approach": {"approach", "go", "goto", "reach", "walk"},
            "answer": {"answer", "respond", "talk"},
            "sleep": {"sleep", "rest", "nap"},
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
            "help": {"help", "h"},
            "exit": {"exit", "quit"},  # TODO: replace exit w/ quit
            "read": {"read"},
            "draw": {"draw", "illustrate", "paint", "inscribe", "mark"},
            "place": {"place", "put", "set", "lie"},
            "jump": {"jump", "bounce"},
        }
        self.SYNONYMS_FOR_THING = {
            "room": {
                "room",
                "floor",
                "wall",
                "walls",
                "ceiling",
                "space",
                "area",
                "environment",
            },
            "phone": {"phone", "device", "cellphone"},
            "desk": {"desk", "table"},
            "bed": {"bed", "mattress", "sheets", "pillow"},
        }
        # never delete a thing/action, just update
        # TODO: have hit bed be function & have it say something different if you do it 
        # twice
        thing_props = {
            "bed": {"hasBeenHit": False},
        }
        responses = {
            "room": {
                "look": (
                    "You can see a bed and a desk with a phone resting on top. "
                    "There's nothing else."
                ),
                "pickup": "Don't be ridiculous.",
                "approach": "You're already in the room, man. No need.",
                "hit": "You kick and hit around the room. Nothing happens.",
            },
            "phone": {
                "look": "A small cheap phone. It appears to be ringing.",
                "pickup": "You have taken the phone. It is still ringing.",
                "approach": "You have approached the phone.",
                "answer": (
                    "You answer it, the voice on the other line says 'You find "
                    "yourself in a room.' As the voice speaks, the room around you"
                    " starts to shift. You are now in a completely different room."
                ),
                "hit": "Why? Stop being so violent.",
            },
            "desk": {
                "look": "A flimsy wooden desk.",
                "pickup": (
                    "Please. This desk is too heavy to pick up and take with you."
                ),
                "approach": "You have approached the desk.",
                "hit": "You hit the desk. That was pointless.",
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
            },
        }
        inventory = set()
        self.state = {
            "thing_props": thing_props,
            "responses": responses,
            "inventory": inventory,
        }

        # all these dicts should include all things or actions
        assert self.THINGS == set(self.state["responses"].keys())
        assert self.THINGS == set(self.SYNONYMS_FOR_THING.keys())
        assert self.ACTIONS == set(self.SYNONYMS_FOR_ACTION.keys())

    def process_cleaned_input(self, cleaned_input):
        # quickly return response for look shortcuts
        if cleaned_input in self.SYNONYMS_FOR_ACTION["look"] | {"l"}:
            return self.process_command("look", "room")

        # extracting verb and object out of input, then process verb object command
        input_words = cleaned_input.split()
        action, thing = self.extract_action_and_thing(input_words)
        return self.process_command(action, thing)

    def extract_action_and_thing(self, input_words):
        action, thing = "", ""
        action_Found, thing_Found = False, False

        # iterating through words to check for a direct match with any actions and
        # things available or their synonyms
        for input_word in input_words:
            if not action_Found:
                for action_key, synonyms in self.SYNONYMS_FOR_ACTION.items():
                    if input_word in synonyms:
                        action = action_key
                        action_Found = True

            if not thing_Found:
                for thing_key, synonyms in self.SYNONYMS_FOR_THING.items():
                    if input_word in synonyms:
                        thing = thing_key
                        thing_Found = True

        print(f"ACTION:", action)
        print(f"THING:", thing)
        return action, thing

    def process_command(self, action, thing):
        # if theres a game function for this input, do that, otherwise just get the
        # text resource
        try:
            do_action = self.FUNCTIONS[thing][action]
        except KeyError:
            return self.get_response_for_command(action, thing)
        else:
            return do_action()

    # TODO: add below functionality
    # nap >> I cant perform the "nap" action on nothing!
    # nap on the unknown_object >> I cant perform the "nap" action on that.
    # nap on phone >> I cant perform the "nap" action on the "phone" object. (maybe)
    def get_response_for_command(self, action, thing):
        INVALID_ACTION = f"You can't do that to the {thing}."

        response = None
        if action and thing:
            # being here assumes action & thing are recognized
            # we dont need an invalid object option since recognized things will always
            # exist in all our dicts but recognized actions might not. e.g. sleep on
            # phone.
            # yes, even if thing gets destroyed, itll still be in all our dicts
            response = self.state["responses"][thing].get(action, INVALID_ACTION)
        elif not action and thing:
            response = f"Not sure what you want to do to the {thing}."
        elif action and not thing:
            response = f"I can't do the '{action}' action on that."
        elif not action and not thing:
            response = (
                "Couldn't find an eligible verb or object in your command.\n"
                "Example of a good command:\n"
                "hit desk\n"
                "Here, 'hit' is the verb and 'desk' is the object."
            )
        return response + "\n"

    def go_to_next_room(self):
        # TODO: magic num
        # TODO: this func should probably be passed from Game, so Game decides what to
        # do appropriately
        self.state["inventory"].clear()
        if self.level_number < 4:
            self.level_number += 1

    # // ----------------------------------
    # SMART ACTIONS
    # this section has all the specific game actions that need to do things other than
    # just give back the string resource to the player

    def pickup_phone(self):
        # get our "render" (like in react) from our dict which should always contain
        # the proper up-to-date render given the current state
        # important that we get our render before running any state changes
        response = self.get_response_for_command("pickup", "phone")

        # change our state given the action
        # then change our responses dict so that it has all the right renders for the
        # now different current state
        # move phone object to inventory
        if "phone" not in self.state["inventory"]:
            # phone not picked up yet, do the state changes
            # change non-responses
            self.state["inventory"].add("phone")
            # change responses
            # room changes
            self.state["responses"]["room"][
                "look"
            ] = "You can see a bed and a desk. There's nothing else."
            # phone changes
            self.state["responses"]["phone"][
                "look"
            ] = "A small cheap phone. It is ringing. Now that it is on your person, you can feel an unexplainable force emanating from it."
            self.state["responses"]["phone"][
                "pickup"
            ] = "You already have the phone!"
            self.state["responses"]["phone"][
                "approach"
            ] = "You can't approach something that's already on your person!"

        # we already had our proper render prepared, now that the state and responses
        # has been properly changed for any future commands and get_response's, we can
        # finish our function
        return response

    def answer_phone(self):
        # get response and save that
        response = self.get_response_for_command("answer", "phone")

        # do the state change stuff so that our renders and shit are prepared
        # for now do nothing, I assume we would have to call a func ref passed down 
        # from Game object that would do the switch
        # self.go_to_next_room()

        # return that saved response
        return response
