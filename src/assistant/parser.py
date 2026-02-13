def parse_input(user_input: str):
    """Split user input into a command and argument list."""
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args
