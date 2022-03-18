import re
import sys

# Checking if the filename exists otherwise exit
# Possible improvement: Ask user again for filename and don't exit right away
try:
    text_file = open(input('Enter text file name. Example: test.txt: '), 'r')
except FileNotFoundError as e:
    print('File not found, check filename.')
    sys.exit()

# Reading the text file
file_text = text_file.read()
text_file.close()

# Initiate the search
keys_found = re.findall(r"\bvaluation_\w+", file_text)

# Removing possible duplicates from array
keys_without_duplicates = list(dict.fromkeys(keys_found))

# Getting the amount of keys finds
keys_amount_found = len(keys_without_duplicates)

# Checking if keys are found
if keys_amount_found > 0:
    print(f"Found {str(keys_amount_found)} keys in file!")
    single_or_array = input('You want them printed out as array or single? single/array: ')
    single_or_array = single_or_array.strip()
    if single_or_array == 'array':
        print('\n', keys_without_duplicates)
    elif single_or_array == 'single':
        for key in keys_without_duplicates:
            print(key)
    else:
        print('Input not recognized.')
        sys.exit()
else:
    print('No keys found! Check if file is saved as .txt file. You can do this easily with Notepad ++')
