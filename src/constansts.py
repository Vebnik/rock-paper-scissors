ITEMS = ("paper", "scissors", "rock", "lizard", "spock")

RULE_MATRIX = {
    "scissors": {"paper", "lizard"},
    "paper": {"rock", "spock"},
    "rock": {"lizard", "scissors"},
    "lizard": {"spock", "paper"},
    "spock": {"scissors", "rock"},
}
