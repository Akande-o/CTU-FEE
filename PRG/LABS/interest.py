def compute_final_amount(P, r, n, t):
    if n == 0:
        raise ZeroDivisionError("n should not be zero")
    else:
        A = P * (1 + r/n) ** n*t
        return A
if __name__ == "__main__":
    final_amount = compute_final_amount(10000, 0.08, 0, 24)
    if final_amount != None:
        print("You will get ", final_amount, "dollars!")