import blessed
position = 0


def board_printer(walk_speed: int, run_speed: int):
    terminal = blessed.Terminal()
    print(terminal.home + terminal.normal + terminal.clear)

    print(" " * walk_speed + npc_walk)
    print("-" * 100)
    print(" " * run_speed + npc_sprint)


npc_walk = """
     O
    /|\\
    | |
"""

npc_sprint = """
     O
    /|\\
    / /
"""
