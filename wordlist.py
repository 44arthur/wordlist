import itertools

# list the words you want to make a wordlist with
words = [""]

combinations = []
for r in range(2, len(words) + 1):  
    combinations.extend([''.join(comb) for comb in itertools.permutations(words, r)])

# define the path for the file
file_path = ""  # change the path if needed

with open(file_path, 'w') as file:
    for combo in combinations:
        file.write(combo + "\n")

print(f"Wordlist saved to {file_path}")
