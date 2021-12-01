def read_input(filename: str) -> list[str]:
    file = open(f'input/{filename}', 'r')
    return file.readlines()
