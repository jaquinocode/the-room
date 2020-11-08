class Room:
    def __init__(self):
        self.room_number = 0
        self.room_things = {
            "room": {
                "look": "A room.",
                "pickup": "Don't be ridiculous.",
                "approach": "You're already in the room, man. No need.",
                "hit": "You kick and hit around the room. Nothing happens.",
                "synonyms": {"space", "area", "environment", "everything"},
            }
        }


class Room1(Room):
    def __init__(self):
        super().__init__()
        self.room_number = 1
        self.room_things["room"]["look"] = (
            "You can see a bed and a desk with a phone resting on top. There's nothing "
            "else."
        )
        self.room_things.update(
            {
                "phone": {
                    "look": "A small cheap phone. It appears to be ringing.",
                    "pickup": (
                        "You have taken the phone. It is still ringing. Enter 'i' or "
                        "'inventory' at any time to bring up your inventory."
                    ),
                    "approach": "You have approached the phone.",
                    "answer": (
                        "You answer it, the voice on the other line says 'You find "
                        "yourself in a room.' As the voice speaks the room around you "
                        "starts to shift. You are now in a completely different room."
                    ),
                    "hit": "You hit the phone. Nothing happens.",
                    "synonyms": {"device", "cellphone"},
                },
                "desk": {
                    "look": "A flimsy wooden desk with a phone resting on it.",
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
        )

    def print_things(self):
        print(self.room_things)

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