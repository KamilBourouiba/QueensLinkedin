import numpy as np
from collections import defaultdict
from colorama import init, Fore, Back, Style

init(autoreset=True)

def solve_puzzle(grid):
    rows, cols = grid.shape
    color_regions = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            color_regions[grid[r, c]].append((r, c))
    
    def is_safe(r, c):
        for i in range(rows):
            if solution[i, c] == 1:
                return False
        for j in range(cols):
            if solution[r, j] == 1:
                return False
        
        for i in range(max(0, r-1), min(rows, r+2)):
            for j in range(max(0, c-1), min(cols, c+2)):
                if solution[i, j] == 1:
                    return False
        
        color = grid[r, c]
        if sum(solution[i, j] for i, j in color_regions[color]) >= 1:
            return False
        
        return True
    
    def backtrack(index=0):
        if index == rows * cols:
            return all(sum(solution[i, j] for i, j in region) == 1 for region in color_regions.values())
        
        r, c = index // cols, index % cols
        
        if is_safe(r, c):
            solution[r, c] = 1
            if backtrack(index + 1):
                return True
            solution[r, c] = 0
        
        if backtrack(index + 1):
            return True
        
        return False
    
    solution = np.zeros((rows, cols), dtype=int)
    
    if backtrack():
        return solution
    return None

def print_colored_solution(grid, solution):
    color_map = {
        0: Fore.YELLOW,
        1: Fore.CYAN,
        2: Fore.MAGENTA,
        3: Fore.BLUE,
        4: Fore.GREEN,
        5: Fore.RED,
        6: Fore.LIGHTYELLOW_EX,
        7: Fore.WHITE
    }
    
    crown = '♛'
    
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            color = color_map[grid[r, c]]
            if solution[r, c] == 1:
                print(f"{color}{Back.BLACK}{crown}", end=' ')
            else:
                print(f"{color}{Back.BLACK}□", end=' ')
        print(Style.RESET_ALL)

grid = np.array([
    [0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 1, 1, 1],
    [0, 2, 0, 0, 5, 4, 1, 4],
    [2, 2, 0, 5, 5, 5, 4, 4],
    [2, 2, 6, 5, 5, 5, 4, 4],
    [2, 6, 6, 5, 5, 6, 6, 4],
    [5, 6, 5, 5, 7, 7, 6, 0],
    [5, 5, 5, 5, 5, 7, 7, 0]
])

solution = solve_puzzle(grid)

if solution is not None:
    print("Solution found:")
    print_colored_solution(grid, solution)
else:
    print("No solution exists.")