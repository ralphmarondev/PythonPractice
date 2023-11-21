# generate random string until given string is generated

import string
import random
import time

# all possible chars including lowercase
# uppercase and special symbol
possible_chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

# string to be generated
t = "ralphmaron"

attempt_this = "".join(random.choice(possible_chars) for i in range(len(t)))
attempt_next = ""

completed = False
iteration = 0

# iterate while completed is false
while not completed: # completed == False
    print(attempt_this)

    attempt_next = ""
    completed = True

    # fix the index if matches with the string
    # to be generated
    for i in range(len(t)):
        if attempt_this[i] != t[i]:
            completed = False
            attempt_next += random.choice(possible_chars)
        else:
            attempt_next += t[i]

    # increment the iteration
    iteration += 1
    attempt_this = attempt_next
    time.sleep(0.1)


# driver code
print(f"Target matched after: {str(iteration)} iterations")
