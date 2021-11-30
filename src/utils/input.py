def getInput(day: str, ext: str = '.txt') -> list[str]:
    file = open(f'input/{day}{ext}', 'r')
    return file.readlines()
