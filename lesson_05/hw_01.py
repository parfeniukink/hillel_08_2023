from pprint import pprint as print

team: list[dict] = [
    {"age": 20, "name": "John", "number": 17},
    {"age": 33, "name": "Mark", "number": 3},
    {"age": 17, "name": "Cavin", "number": 17},
    {"age": 31, "name": "Cris", "number": 17},
    {"age": 39, "name": "Bob", "number": 3},
    {"age": 31, "name": "Stive", "number": 17},
    {"age": 39, "name": "Org", "number": 17},
]


def remove_player_by_number(_team: list[dict], n: int):
    print(_team)

    index = 0

    while True:
        if index >= len(_team):
            break

        if _team[index]["number"] == n:
            del _team[index]
            index -= 1

        index += 1

    print(_team)


remove_player_by_number(team, 17)
