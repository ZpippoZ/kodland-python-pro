from random import choice, randint
import string

chars = string.ascii_letters + string.digits + string.punctuation
pw = "".join(choice(chars) for _ in range(randint(8, 20)))
print(pw)
