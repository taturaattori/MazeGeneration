from tkinter import *
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
            
            canvas.delete("all")
            draw_maze(canvas, grid, cell_width, cell_height)
            canvas.update()
            canvas.after(10)
            # Sitten kutsutaan funktiota uudestaan uudesta pisteestä
            create_passages(nx, ny, grid)

def draw_maze(canvas, grid, cell_width, cell_height):

    canvas.create_line(0, 0, cell_width * width, 0, width=8)
    canvas.create_line(0, 0, 0, cell_height * height, width=8)

    for y in range(height):
        for x in range(width):
            if not grid[y][x] & N:
                canvas.create_line(x*cell_width, y*cell_height, (x+1)*cell_width, y*cell_height, width=2)
            if not grid[y][x] & W:
                canvas.create_line(x*cell_width, y*cell_height, x*cell_width, (y+1)*cell_height, width=2)
            if not grid[y][x] & E:
                canvas.create_line((x+1)*cell_width, y*cell_height, (x+1)*cell_width, (y+1)*cell_height, width=2)
            if not grid[y][x] & S:
                canvas.create_line(x*cell_width, (y+1)*cell_height, (x+1)*cell_width, (y+1)*cell_height, width=2)

root = Tk()
root.title("Maze Generator")


cell_width = 40
cell_height = 40
canvas = Canvas(root, width=cell_width*width, height=cell_height*height)
canvas.pack()


create_passages(0, 0, grid)


draw_maze(canvas, grid, cell_width, cell_height)

# Näytä labyrintin luontiin käytetyt paramtetrit
print(f"width: {width} height: {height} seed: {seed}")

root.mainloop()