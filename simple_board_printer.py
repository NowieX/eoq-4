import blessed
import random
position = 0
BOARD_END = 100


def board_printer(walk_speed: int):
    terminal = blessed.Terminal()
    print(terminal.home + terminal.normal + terminal.clear)

    player = f"""
    {" " * walk_speed + terminal.red}    You
    {" " * walk_speed + terminal.red}    /|\\
    {" " * walk_speed + terminal.red}    | |
    """

    bob_random = random.randint(-2, 1)
    bob = f"""
    {" " * (walk_speed + bob_random) + terminal.blue}    Bob
    {" " * (walk_speed + bob_random) + terminal.blue}    /|\\
    {" " * (walk_speed + bob_random) + terminal.blue}    / /
    """

    jan_random = random.randint(-2, 1)
    jan = f"""
    {" " * (walk_speed + jan_random) + terminal.green}    Jan
    {" " * (walk_speed + jan_random) + terminal.green}    /|\\
    {" " * (walk_speed + jan_random) + terminal.green}    / /
    """

    kim_random = random.randint(-2, 1)
    kim = f"""
    {" " * (walk_speed + kim_random) + terminal.yellow}    Kim
    {" " * (walk_speed + kim_random) + terminal.yellow}    /|\\
    {" " * (walk_speed + kim_random) + terminal.yellow}    / /
    """

    print(player)
    print(terminal.normal)
    print("-" * BOARD_END)
    print(bob, end="")
    print(terminal.normal)
    print("-" * BOARD_END)
    print(jan, end="")
    print(terminal.normal)
    print("-" * BOARD_END)
    print(kim, end="")
    print(terminal.normal)

