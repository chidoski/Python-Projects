def print_quad(characters):
    print(characters)
    print(characters)
    print(characters)
    print(characters)

def grid(rows, columns):
    print(rows)
    print_quad(columns)
    print(rows)
    print_quad(columns)
    print(rows)
    print_quad(columns)
    print(rows)
    print_quad(columns)
    print(rows)

rows = ('+ - - - - + - - - - + - - - - + - - - - +');
columns = ('|         |         |         |         |');

grid(rows, columns)
