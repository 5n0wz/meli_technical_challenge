#!/usr/bin/env python3.11
import numpy as np


def count_adj_bombs(input_matrix, row, col) -> int:
    num_rows, num_cols = input_matrix.shape
    num_adj_bombs = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if 0 <= row + x < num_rows and 0 <= col + y < num_cols:
                if input_matrix[row + x, col + y] == 1:
                    num_adj_bombs += 1
    return num_adj_bombs


def reveal_board(board) -> np.ndarray:
    input_matrix = np.array(board)
    output_matrix = np.zeros_like(input_matrix)
    for row in range(input_matrix.shape[0]):
        for col in range(input_matrix.shape[1]):
            if input_matrix[row][col] == 1:
                output_matrix[row][col] = 9
            else:
                output_matrix[row][col] = count_adj_bombs(
                    input_matrix, row, col)

    return output_matrix


def main() -> None:
    input_board = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 0]
    ]
    output_board = reveal_board(input_board)
    print(output_board)


if __name__ == '__main__':
    main()
