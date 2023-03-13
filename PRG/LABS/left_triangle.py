def print_left_triangle(n_rows, char):
    # no return statement = return None
    for i in range(n_rows):
        print(char * (i+1))



if __name__ == "__main__":
    print_left_triangle(10, "T")
