import random

# Aseta labyrintin leveys ja korkeus, seed jos haluat luoda saman labyrintin uudestaan
width = int(input('Enter width: '))
height = int(input('Enter height: '))
seed = (input('Enter seed (leave empty to create a random maze): '))

if seed == '':
    seed = random.randint(0, 0xFFFFFFFF)
    
random.seed(int(seed))


grid = [[0 for x in range(width)] for y in range(height)]

# Asetetaan suunnat ja koordinaattien muutokset
N, S, E, W = 1, 2, 4, 8
DX = { E: 1, W: -1, N: 0, S: 0 }
DY = { E: 0, W: 0, N: -1, S: 1 }
OPPOSITE = { E: W, W: E, N: S, S: N }

# Algoritmi
def create_passages(cx, cy, grid):
    directions = [N, S, E, W]
    random.shuffle(directions)

    for direction in directions:
        nx, ny = cx + DX[direction], cy + DY[direction]

        # Tarkastetaan onko piste ruudukon sisällä ja onko siellä jo käyty
        if ny in range(height) and nx in range(width) and grid[ny][nx] == 0:
            # Kun piste on validi poistetaan seinä välistä
            grid[cy][cx] |= direction
            grid[ny][nx] |= OPPOSITE[direction]
            # Sitten kutsutaan funktiota uudestaan uudesta pisteestä
            create_passages(nx, ny, grid)

create_passages(0, 0, grid)

# Tulostetaan labyrintti
print(" " + "_" * (width * 2 - 1))
for y in range(height):
    print("|", end="")
    for x in range(width):
        print(" " if grid[y][x] & S != 0 else "_", end="")
        if grid[y][x] & E != 0:
            print(" " if (grid[y][x] | grid[y][x+1]) & S != 0 else "_", end="")
        else:
            print("|", end="")
    print()

# Näytä labyrintin luontiin käytetyt paramtetrit
print(f"width: {width} height: {height} seed: {seed}")