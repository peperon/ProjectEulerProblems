def generate_products():
    lst = []
    for k in range(999, 100, -1):
        for l in range(999, 100, -1):
            lst.append(k * l)
    lst.sort()
    lst.reverse()
    return lst
  
def palindrom(number):
    number_string = str(number)
    return (number_string[::-1] == number_string)

if __name__ == "__main__":
  lst = generate_products()
  for k in lst:
      if palindrom(k):
        print(k)
        break
