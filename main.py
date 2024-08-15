from src.models import Player
from src.constansts import RULE_MATRIX
from src.utils import build_results_table


def main():
    table = build_results_table(RULE_MATRIX)

    while True:
        state = frozenset(
            (
                Player.make_player().item,
                Player.make_player().item,
            )
        )

        try:
            print(table[state])
        except KeyError:
            print("Draw")


main()
