def print_right_triangle(n_rows, char):
    for i in range(n_rows):
        print(" " * (n_rows -(i+1)) + char * (i + 1))
if __name__ == "__main__":
    print_right_triangle(10, "R")