# Concurrency for Sudoku validation

## Theory

A valid 9×9 Sudoku contains digits 1–9 exactly once in every row, column and 3×3 subgrid. The exercise creates 27 worker threads: 9 for rows, 9 for columns and 9 for subgrids.

## Question

> Validate a 9×9 Sudoku solution concurrently by checking all rows, columns and 3×3 subgrids in separate threads.

## Python implementation

The exercise is implemented in Python 3. See the command examples in this README and the lab manual.
