import blessed


def board_printer():
    terminal = blessed.Terminal()
    print(terminal.home + terminal.normal + terminal.clear, end=" ")

