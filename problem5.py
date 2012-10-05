def divide_of_1_20_range(number):
    for value in range(2, 21):
        if number % value != 0:
            return False

    return True


def problem5():
    result_number = 20
    while not divide_of_1_20_range(result_number):
        result_number += 20
#        print("not {0}", result_number)
    return result_number

if __name__ == "__main__":
    print(problem5())
