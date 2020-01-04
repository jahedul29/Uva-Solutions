value = 2
counter = 1
while True:
    if value%2 ==0 or value%3 == 0 or value%5 ==0:
        counter += 1
        print(value)
    if counter == 1500:
        print(f"The 1500'th ugly number is <{value}>")
        break
    value += 1