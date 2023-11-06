# Function to count word frequency in a text file
def count_word_frequency(file_path):
    word_frequency = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Remove punctuation and convert to lowercase
                    word = word.strip('.,!?":;()[]{}').lower()
                    if word:
                        if word in word_frequency:
                            word_frequency[word] += 1
                        else:
                            word_frequency[word] = 1

        return word_frequency

    except FileNotFoundError:
        return None

# Input: Provide the path to the text file you want to analyze
file_path = 'sample.txt'   # Change this to the path of your text file

result = count_word_frequency(file_path)

if result is not None:
    print("Word frequency in the file:")
    for word, frequency in result.items():
        print(f"{word}: {frequency}")
else:
    print("File not found.")
