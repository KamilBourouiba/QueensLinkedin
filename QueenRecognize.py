import numpy as np
import cv2
from collections import defaultdict
from colorama import init, Fore, Back, Style
import os
from sklearn.cluster import KMeans

init(autoreset=True)

def detect_grid_from_image(image_path, grid_size, num_colors):
    image = cv2.imread(image_path)

    if image is None:
        print(f"[ERROR] Unable to load image at {image_path}. Please check the file path and integrity.")
        return None, None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image_resized = cv2.resize(image_rgb, (grid_size, grid_size))

    pixels = image_resized.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    cluster_centers = np.uint8(kmeans.cluster_centers_)

    labels = kmeans.labels_

    grid_indices = labels.reshape((grid_size, grid_size))

    palette = cluster_centers.tolist()

    return grid_indices, palette

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
            color = color_map.get(grid[r, c], Fore.WHITE)
            if solution[r, c] == 1:
                print(f"{color}{Back.BLACK}{crown}", end=' ')
            else:
                print(f"{color}{Back.BLACK}□", end=' ')
        print(Style.RESET_ALL)

def print_grid(grid):
    print("Grid Indices:")
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()

image_path = 'Grid.jpg'
grid_size = 7
num_colors = 7

if os.path.exists(image_path):
    grid_indices, palette = detect_grid_from_image(image_path, grid_size, num_colors)

    if grid_indices is not None:
        #print_grid(grid_indices)  # Print the grid in the terminal
        
        # Ask for user confirmation
        # confirm = input("Do you want to proceed with solving the puzzle? (yes/no): ").strip().lower()
        # if confirm == 'yes':
        solution = solve_puzzle(grid_indices)

        if solution is not None:
                print("Solution found:")
                print_colored_solution(grid_indices, solution)
        else:
                print("No solution exists.")
        #else:
            #print("Puzzle solving canceled.")
    else:
        print("Failed to detect grid from image.")
else:
    print("Image not found. Please check the path.")