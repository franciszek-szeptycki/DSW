# Bogosort

import random

attempt = 0
while True:
    # list parameters
    random_list = []
    n = 3

    # generate random list
    for i in range(n):
        random_list.append(random.randint(0, 10))

    # check is list sorted
    done = False
    previous_index = 100
    current_index = 0

    for item in random_list:
        if previous_index < item:
            break
        else:
            if current_index == n - 1:
                done = True
                break
            else:
                previous_index = item
                current_index += 1

    # print current action info
    attempt += 1
    print(f"{random_list} - number of attempts: {attempt}")

    if done:
        print("done!")
        break



