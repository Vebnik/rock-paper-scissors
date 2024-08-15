from dataclasses import dataclass

from src.constansts import ITEMS


@dataclass
class Player:
    item: str

    @staticmethod
    def make_player():
        user_item = input("Select item (paper, scissors, rock, lizard, spock): ")

        if user_item not in ITEMS:
            raise Exception(f"Not found right item: {user_item}")

        return Player(item=user_item)
