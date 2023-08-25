def capitalize(text: str) -> str:
    return f'{text[0].upper()}{text[1:]}' if text != '' else text
