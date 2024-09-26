# Queens Puzzle Solver

This repository contains two Python scripts, `Queen.py` and `QueenRecognizer.py`, designed to solve the "Queens" puzzle, where the goal is to place queens on a grid such that no two queens threaten each other. The grid has distinct color regions, and the challenge is to place exactly one queen in each row, column, and color region.

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Scripts](#scripts)
  - [Queen.py](#queenpy)
  - [QueenRecognizer.py](#queenrecognizerpy)
- [Example](#example)

## Overview

The "Queens" puzzle is a fun challenge that requires strategic placement of queens on a grid, but with an extra twist: the grid has multiple color regions, and the objective is to place exactly one queen in each row, column, and color region. The challenge can get complex, so these scripts aim to automate the process of finding solutions.

## How It Works

1. **Queen.py**: Manually builds a grid and finds a solution by using a backtracking algorithm. The grid can be visualized in the terminal with colored queens representing each placement.
  
2. **QueenRecognizer.py**: Detects the puzzle grid from an image using image processing (via OpenCV), identifies the distinct color regions with K-Means clustering, and then solves the puzzle automatically.

Both scripts utilize a backtracking algorithm to ensure that no two queens threaten each other, and that exactly one queen is placed in each color region.

## Getting Started

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/queens-puzzle-solver.git
    ```

2. Install the required Python libraries:
    ```bash
    pip install numpy colorama opencv-python scikit-learn
    ```

### Usage

For both scripts, ensure you have Python 3 installed.

- Run the `Queen.py` script:
    ```bash
    python Queen.py
    ```

- Run the `QueenRecognizer.py` script:
    ```bash
    python QueenRecognizer.py
    ```

## Scripts

### Queen.py

This script builds a grid directly in the code and attempts to solve the puzzle using a backtracking algorithm. Once the solution is found, it prints the grid to the terminal, with each queen displayed in a specific color corresponding to its region.

#### Key Functions:

- **`solve_puzzle(grid)`**: Solves the puzzle using a backtracking approach, ensuring no two queens are in the same row, column, or color region.
- **`print_colored_solution(grid, solution)`**: Displays the solved grid in the terminal with queens in different colors.

### QueenRecognizer.py

This script uses OpenCV to load an image of the grid, detects distinct color regions with K-Means clustering, and then solves the puzzle similarly to `Queen.py`. The user must specify the grid size and the number of colors (regions) present.

#### Key Functions:

- **`detect_grid_from_image(image_path, grid_size, num_colors)`**: Reads and processes the grid from an image, clustering it into distinct regions using K-Means.
- **`solve_puzzle(grid)`**: Solves the puzzle using the same backtracking algorithm as `Queen.py`.
- **`print_colored_solution(grid, solution)`**: Prints the solved grid with colored queens in the terminal.
- **`print_grid(grid)`**: Displays the detected grid indices before solving, useful for debugging.

## Example

### Queen.py

```bash
$ python Queen.py

Solution found:
♛ □ □ □ □ □ ♛ ♛ 
□ □ □ □ □ ♛ □ □ 
♛ □ □ □ □ □ ♛ ♛ 
```

### QueenRecognizer.py

1. Place your grid image in the working directory.
2. Ensure you specify the correct grid size and number of colors in the script.
3. Run the script, and the puzzle will be solved and printed similarly to `Queen.py`.
