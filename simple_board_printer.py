import blessed
import random
position = 0
BOARD_END = 200


def board_printer(walk_speed: int):
    terminal = blessed.Terminal()
    print(terminal.home + terminal.normal + terminal.clear)

    player_extra_speed = random.randint(1, 2)
    player = f"""
{" " * (walk_speed + player_extra_speed) + terminal.red}You
{" " * (walk_speed + player_extra_speed) + terminal.red}/|\\
{" " * (walk_speed + player_extra_speed) + terminal.red}| |
    """

    bob_random = random.randint(-2, 1)
    bob = f"""
{" " * (walk_speed + bob_random) + terminal.blue}Bob
{" " * (walk_speed + bob_random) + terminal.blue}/|\\
{" " * (walk_speed + bob_random) + terminal.blue}/ /
    """

    jan_random = random.randint(-2, 1)
    jan = f"""
{" " * (walk_speed + jan_random) + terminal.green}Jan
{" " * (walk_speed + jan_random) + terminal.green}/|\\
{" " * (walk_speed + jan_random) + terminal.green}/ /
    """

    kim_random = random.randint(-2, 1)
    kim = f"""
{" " * (walk_speed + kim_random) + terminal.yellow}Kim
{" " * (walk_speed + kim_random) + terminal.yellow}/|\\
{" " * (walk_speed + kim_random) + terminal.yellow}/ /
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

    if walk_speed + player_extra_speed >= BOARD_END:
        print("You have won!")
        exit()
    elif walk_speed + bob_random >= BOARD_END:
        print("Bob has won!")
        exit()
    elif walk_speed + jan_random >= BOARD_END:
        print("Jan has won!")
        exit()
    elif walk_speed + kim_random >= BOARD_END:
        print("Kim has won!")
        exit()

def print_crowd():
    crowd_reactions = ["Gogogo!", "You can do it!", "Keep going!", "Don't give up!", "End of quarter sucks!!!"]
    crowd = f"""
{'      (˵ ͡° ͜ʖ ͡°˵)      (̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄    ヽ༼ຈل͜ຈ༽ﾉ       ' * 3}
"""
    random_reaction = random.choice(crowd_reactions)
    random_space = random.randint(0, len(crowd) - 50)

    for element in crowd:
        if element != " ":
            print((random_space * " ") + random_reaction)
            break
    print(crowd, end="")
