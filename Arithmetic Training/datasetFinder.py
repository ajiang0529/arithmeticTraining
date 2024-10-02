import datasets

# Load the dataset with a specific configuration
dataset = datasets.load_dataset('joshuaau37/arithmetic_words', 'arithmetic_1dc')

# Print out the structure of a few examples
print(dataset['validation'][0])
print(dataset['validation'][1])
