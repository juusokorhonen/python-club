

def parse_command_39(command):
    # According to Python 3.9
    cmd = command.split()
    if len(cmd) == 1 and cmd[0] == "look":
        return "You see a door and a table."
    if len(cmd) == 2 and cmd[0] == "open" and cmd[1] == "door":
        return "You open the door."
    if len(cmd) == 2 and cmd[0] == "open":
        return f"You try to open {cmd[1]}, but fail."
    if len(cmd) >= 2 and cmd[0] == "take":
        items_str = " ".join(cmd[1:])
        return f"You take the {items_str} and place {'them' if len(cmd[1:]) > 1 else 'if'} in your pocket."
    if len(cmd) == 2 and cmd[0] == "go" and cmd[1] in ("north", "south", "east", "west"):
        return f"You go {cmd[1]}."
    return f"You don't know how to {command}."


def parse_command_310(command):
    # According to PEP634 (Python 3.10)
    match command.split():
        case ["look"]:
            return "You see a door and a table."
        case ["open", "door"]:
            return "You open the door."
        case ["open", item]:
            return f"You try to open {item}, but fail."
        case ["take", *items]:
            items_str = " ".join(items)
            return f"You take the {items_str} and place {'them' if len(items) > 1 else 'if'} in your pocket."
        case ["go", ("north" | "south" | "east" | "west" as direction)]:
            return f"You go {direction}."
        case _:
            return f"You don't know how to {command}."


def main():

    commands = [
        "look",
        "open door",
        "open passage",
        "go west",
        "go down",
        "take rose",
        "take keys and wallet",
        "run",
        "foobar baz"
    ]

    for command in commands:
        print(f"     CMD: {command}")
        out_310 = parse_command_310(command)
        out_39 = parse_command_39(command)
        print(f"OUT 3.10: {out_310}")
        print(f"OUT 3.9 : {out_39}")
        assert out_310 == out_39, "Outputs do not match."


if __name__ == "__main__":
    main()
