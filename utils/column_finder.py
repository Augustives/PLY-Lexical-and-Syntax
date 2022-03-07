def find_column(text, line, char):
    column = 2
    num_lines = 1
    for i in text:
        if num_lines == line:
            if i == char:
                return column 
            column += 1
        elif i == '\n':
            num_lines += 1
