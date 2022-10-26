import random
import json
import string


MAIN_PATH = f'..'
DATA_FOLDER_NAME = "bingo_cards/init"

SAVE_DATA_PATH = f'{MAIN_PATH}/{DATA_FOLDER_NAME}'

SUPPLY = 100

def main():
    # supply = int(input("supply: "))
    supply = SUPPLY
    for token_id in range(1,supply+1):
        print(token_id)
        data = create_bingo()
        output(data, token_id)

def output(data, token_id):
    template = open('../templates/init/template_bingo.html', 'r')

    reader = string.Template(template.read())
    html = reader.safe_substitute(data)

    with open(f'{SAVE_DATA_PATH}/{token_id}.html', mode='w') as file:
        file.write(html)

def create_bingo():
    b = []
    i = []
    n = []
    g = []
    o = []

    for column in "BINGO":
        if column == "B":
            while len(b) <= 5:
                rand = random.randint(1, 15)
                if not rand in b:
                    b.append(rand)
        elif column == "I":
            while len(i) <= 5:
                rand = random.randint(16, 30)
                if not rand in i:
                    i.append(rand)
        elif column == "N":
            while len(n) <= 5:
                if len(n) == 2:
                    n.append("FREE")
                    continue
                rand = random.randint(31, 45)
                if not rand in n:
                    n.append(rand)
        elif column == "G":
            while len(g) <= 5:
                rand = random.randint(46, 60)
                if not rand in g:
                    g.append(rand)
        elif column == "O":
            while len(o) <= 5:
                rand = random.randint(61, 75)
                if not rand in o:
                    o.append(rand)

    print("BINGO=", b, i, n, g, o)
    data = {
        'b0': b[0],
        'b1': b[1],
        'b2': b[2],
        'b3': b[3],
        'b4': b[4],
        'i0': i[0],
        'i1': i[1],
        'i2': i[2],
        'i3': i[3],
        'i4': i[4],
        'n0': n[0],
        'n1': n[1],
        'n2': n[2],
        'n3': n[3],
        'n4': n[4],
        'g0': g[0],
        'g1': g[1],
        'g2': g[2],
        'g3': g[3],
        'g4': g[4],
        'o0': o[0],
        'o1': o[1],
        'o2': o[2],
        'o3': o[3],
        'o4': o[4],
    }

    return data

if __name__ == '__main__':
    main()