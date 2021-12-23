import unidecode
import string
import random
import re

all_characters = string.printable
n_characters = len(all_characters)

file = unidecode.unidecode(open('data/shakespeare_input.txt').read())
file_len = len(file)
print('file_len =', file_len)

chunk_len = 200


def random_chunk():
    start_index = random.randint(0, file_len-chunk_len)
    end_index = start_index + chunk_len + 1
    return file[start_index:end_index],file_len,chunk_len,start_index,end_index


print(random_chunk())

