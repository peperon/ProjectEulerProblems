def problem6():
    sum_squares, sum_sequence = 1, 1
    for i in range(2, 101):
        sum_squares += i ** 2
        sum_sequence += i
    square_sum = sum_sequence ** 2

    return square_sum - sum_squares

if __name__ == "__main__":
    print(problem6())
