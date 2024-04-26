import blessed
position = 0
BOARD_END = 100


def board_printer(walk_speed: int, run_speed: int):
    terminal = blessed.Terminal()
    print(terminal.home + terminal.normal + terminal.clear)
    npc_walk = f"""
    {" " * walk_speed} This is you!
    {" " * walk_speed}     O
    {" " * walk_speed}    /|\\
    {" " * walk_speed}    | |
    """

    npc_sprint = f"""
    {" " * run_speed} This is AI Bob
    {" " * run_speed}     O
    {" " * run_speed}    /|\\
    {" " * run_speed}    / /
    """

    print(npc_walk)
    # print(npc_walk, end="")
    print("-" * BOARD_END)
    print(npc_sprint, end="")
