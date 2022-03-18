def find_column(text, line, char):
    if text is None:
        return None
    column = 2
    num_lines = 1
    for i in text:
        if num_lines == line:
            if i == char:
                return column 
            column += 1
        elif i == '\n':
            num_lines += 1
