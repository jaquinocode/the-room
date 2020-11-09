class Game:
    def __init__(self):
        self.is_active = True
        self.LEVEL_CLASSES = [Level_1, Level_2, Level_3]
        self.curr_level_index = 0
        self.curr_level = self.LEVEL_CLASSES[self.curr_level_index](
            self.go_to_next_level
        )

    def go_to_next_level(self):
        self.curr_level_index += 1
        self.curr_level = self.LEVEL_CLASSES[self.curr_level_index](
            self.end_game
            if self.curr_level_index == len(self.LEVEL_CLASSES) - 1
            else self.go_to_next_level
        )

    def end_game(self):
        self.is_active = False

    def process_input(self, raw_input):
        # unintrusive cleansing & caps normalization
        cleaned_input = raw_input.lower().strip()

        return self.curr_level.process_cleaned_input(cleaned_input)


class Level_1:
    def __init__(self, go_to_next_level):
        self.go_to_next_level = go_to_next_level
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
            "quit",
            "read",
            "draw",
            "place",
            "jump",
        }
        self.FUNCTIONS = {
            "bed": {"hit": self.hit_bed},
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
            "quit": {"quit"},
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
        thing_props = {
            "bed": {"wasHit": False},
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

    def get_response_for_command(self, action, thing):
        THING_HAS_NO_ACTION = f"You can't perform action '{action}' on the {thing}."

        response = None
        if action and thing:
            response = self.state["responses"][thing].get(action, THING_HAS_NO_ACTION)
        elif not action and thing:
            response = f"Not sure what you want to do to the {thing}."
        elif action and not thing:
            response = f"I can't perform action '{action}' on that."
        elif not action and not thing:
            response = (
                "Couldn't find an eligible verb or object in your command.\n"
                "Example of a good command:\n"
                "hit desk\n"
                "Here, 'hit' is the verb and 'desk' is the object."
            )
        return response + "\n"

    # // ----------------------------------
    # SMART ACTIONS
    # this section has all the specific game actions that need to do things other than
    # just give back the string resource to the player

    def pickup_phone(self):
        response = self.get_response_for_command("pickup", "phone")

        responses, inventory = (self.state[k] for k in ("responses", "inventory"))
        if "phone" not in inventory:
            inventory.add("phone")

            # room
            responses["room"][
                "look"
            ] = "You can see a bed and a desk. There's nothing else."
            # phone
            responses["phone"]["look"] = (
                "A small cheap phone. It is ringing. Now that it is on your person, "
                "you can feel an unexplainable force emanating from it."
            )
            responses["phone"]["pickup"] = "You already have the phone!"
            responses["phone"][
                "approach"
            ] = "You can't approach something that's already on your person!"

        return response

    def answer_phone(self):
        response = self.get_response_for_command("answer", "phone")

        self.go_to_next_level()

        return response

    def hit_bed(self):
        response = self.get_response_for_command("hit", "bed")

        thing_props, responses = (self.state[k] for k in ("thing_props", "responses"))
        if not thing_props["bed"]["wasHit"]:
            thing_props["bed"]["wasHit"] = True
            responses["bed"]["hit"] = (
                "You attack and hit the bed mercilessly. Nothing continues to happen. "
                "Do you need help?"
            )

        return response


class Level_2:
    def __init__(self, go_to_next_level):
        self.go_to_next_level = go_to_next_level
        self.LEVEL_NUMBER = 2
        # things and actions should never be changed, if thing/action no longer exists
        # then set that as one of its properties e.g. phone_exists: False
        self.THINGS = {"room", "chalk", "note", "door"}
        self.ACTIONS = {
            "look",
            "pickup",
            "approach",
            "answer",
            "sleep",
            "hit",
            "open",
            "help",
            "quit",
            "read",
            "draw",
            "place",
            "jump",
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
            "quit": {"quit"},
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
            "chalk": {"chalk", "chalks", "chlak"},
            "note": {
                "note",
                "paper",
                "message",
                "writing",
                "writings",
                "markings",
                "marks",
                "sticky",
            },
            "door": {"door", "gate"},
        }
        self.FUNCTIONS = {
            "chalk": {"pickup": self.pickup_chalk},
            "door": {"draw": self.draw_door, "open": self.open_door},
        }
        # never delete a thing/action, just update
        thing_props = {"door": {"exists": False}}
        responses = {
            "room": {
                "look": (
                    "Except for a piece of chalk you see rested on the center of "
                    "the floor, this room is completely bare."
                ),
                "pickup": "Don't be ridiculous.",
                "approach": "You're already in the room, man. No need.",
            },
            "chalk": {
                "look": (
                    "A normal piece of chalk. There is a sticky note attached to it."
                ),
                "pickup": "You have picked up the chalk.",
                "approach": "You have approached the chalk.",
            },
            "note": {
                "look": (
                    "A sticky note with a message written on it:\nYOU'VE FOUND THE "
                    "KEY. NOW FIND THE DOOR."
                ),
                "approach": "You have approached the note.",
                "read": "YOU'VE FOUND THE KEY. NOW FIND THE DOOR.",
            },
            "door": {
                "look": (
                    "You try to look for a door, but alas. There is none to be found."
                ),
                "pickup": "Even if there was a door, that's quite silly.",
                "approach": "There is no door to approach.",
                "draw": "Can't draw a door without a writing utensil.",
                "open": "You can't open a non-existent door.",
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

    def get_response_for_command(self, action, thing):
        THING_HAS_NO_ACTION = f"You can't perform action '{action}' on the {thing}."

        response = None
        if action and thing:
            response = self.state["responses"][thing].get(action, THING_HAS_NO_ACTION)
        elif not action and thing:
            response = f"Not sure what you want to do to the {thing}."
        elif action and not thing:
            response = f"I can't perform action '{action}' on that."
        elif not action and not thing:
            response = (
                "Couldn't find an eligible verb or object in your command.\n"
                "Example of a good command:\n"
                "hit desk\n"
                "Here, 'hit' is the verb and 'desk' is the object."
            )
        return response + "\n"

    # // ----------------------------------
    # SMART ACTIONS
    # this section has all the specific game actions that need to do things other than
    # just give back the string resource to the player

    def pickup_chalk(self):
        response = self.get_response_for_command("pickup", "chalk")

        responses, inventory = (self.state[k] for k in ("responses", "inventory"))
        if "chalk" not in inventory:
            inventory.add("chalk")

            # room
            responses["room"]["look"] = "The room is completely bare."
            # chalk
            responses["chalk"]["pickup"] = "You already have the chalk!"
            responses["chalk"][
                "approach"
            ] = "No need to approach the chalk since you have it already."
            # note
            responses["note"][
                "approach"
            ] = "No need to approach the note since you have it already."
            # door
            responses["door"]["draw"] = "You draw the door."

        return response

    def draw_door(self):
        response = self.get_response_for_command("draw", "door")

        thing_props, responses, inventory = (
            self.state[k] for k in ("thing_props", "responses", "inventory")
        )
        if not thing_props["door"]["exists"] and "chalk" in inventory:
            thing_props["door"]["exists"] = True

            # room
            responses["room"][
                "look"
            ] = "The room is completely bare, except for a crudely drawn chalk door."
            # door
            responses["door"][
                "look"
            ] = "A badly drawn, human-sized door drawn with chalk."
            responses["door"]["pickup"] = "You can't do that to the door silly."
            responses["door"]["approach"] = "You approach the door."
            responses["door"]["draw"] = "You've already drawn the door!"
            responses["door"][
                "open"
            ] = "You try to open the door and somehow it works? You enter and are now in a completely different room."

        return response

    def open_door(self):
        response = self.get_response_for_command("open", "door")

        thing_props = self.state["thing_props"]
        if thing_props["door"]["exists"]:
            self.go_to_next_level()

        return response


class Level_3:
    def __init__(self, end_game):
        self.end_game = end_game
        self.LEVEL_NUMBER = 3
        # things and actions should never be changed, if thing/action no longer exists
        # then set that as one of its properties e.g. phone_exists: False
        self.THINGS = {"room", "wall", "table", "rack", "clock", "cube"}
        self.ACTIONS = {
            "look",
            "pickup",
            "approach",
            "answer",
            "sleep",
            "hit",
            "open",
            "help",
            "quit",
            "read",
            "draw",
            "place",
            "jump",
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
            "quit": {"quit"},
            "read": {"read"},
            "draw": {"draw", "illustrate", "paint", "inscribe", "mark"},
            "place": {"place", "put", "set", "lie"},
            "jump": {"jump", "bounce"},
        }
        self.SYNONYMS_FOR_THING = {
            "room": {"room", "floor", "ceiling", "space", "area", "environment"},
            "wall": {
                "wall",
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
            "table": {"table", "desk"},
            "rack": {"rack", "triangle"},
            "clock": {"clock", "circle", "circular"},
            "cube": {"cube", "rubix", "square"},
        }
        self.FUNCTIONS = {}
        # never delete a thing/action, just update
        thing_props = {}
        responses = {
            "room": {
                "look": (
                    "The north wall that's facing me has some strange "
                    "writings/marks on it. There is a billiards table in the center "
                    "of the room in front of you. There is a clock hanging on the same "
                    "wall. There is a rubix cube lying on the floor."
                ),
                "pickup": "Don't be ridiculous.",
                "approach": "You're already in the room, man. No need.",
            },
            "wall": {
                "look": (
                    "You see a clock hanging on the wall. Below that are some markings:"
                    "\n3 -> 1 -> 4"
                ),
                "pickup": "Don't be ridiculous.",
                "approach": "You have approached the wall.",
                "hit": "You hit the wall. Completely useless.",
                "read": "3 -> 1 -> 4",
            },
            "table": {
                "look": (
                    "An old no longer working billiards table. There is a triangle rack"
                    " on it. It would probably be an ideal location to PLACE objects "
                    "onto this table."
                ),
                "pickup": "Don't be silly.",
                "approach": "You have approached the table.",
            },
            "rack": {
                "look": "A large triangle rack used to play pool.",
                "pickup": "You picked up the large triangle rack.",
                "approach": "You have approached the large triangle rack.",
                "place": (
                    "You need to have the rack on your person if you want to place it."
                ),
            },
            "clock": {
                "look": "A medium-sized circular clock.",
                "pickup": "You picked up the medium-sized clock.",
                "approach": "You have approached the clock.",
                "place": (
                    "You need to have the clock on your person if you want to place it."
                ),
            },
            "cube": {
                "look": (
                    "A small rubix cube. Unfortunately doesn't work anymore and "
                    "might as well be a paperweight."
                ),
                "pickup": "You picked up the small rubix cube.",
                "approach": "You have approached the small rubix cube.",
                "place": (
                    "You need to have the cube on your person if you want to place it."
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

    def get_response_for_command(self, action, thing):
        THING_HAS_NO_ACTION = f"You can't perform action '{action}' on the {thing}."

        response = None
        if action and thing:
            response = self.state["responses"][thing].get(action, THING_HAS_NO_ACTION)
        elif not action and thing:
            response = f"Not sure what you want to do to the {thing}."
        elif action and not thing:
            response = f"I can't perform action '{action}' on that."
        elif not action and not thing:
            response = (
                "Couldn't find an eligible verb or object in your command.\n"
                "Example of a good command:\n"
                "hit desk\n"
                "Here, 'hit' is the verb and 'desk' is the object."
            )
        return response + "\n"

    # // ----------------------------------
    # SMART ACTIONS
    # this section has all the specific game actions that need to do things other than
    # just give back the string resource to the player

