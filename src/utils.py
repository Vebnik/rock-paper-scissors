def build_results_table(rules: dict[str, set[str]]) -> dict:
    results = {}
    for key, values in rules.items():
        for value in values:
            state = frozenset((key, value))
            result = f"Winning {key}"
            results[state] = result
    return results
