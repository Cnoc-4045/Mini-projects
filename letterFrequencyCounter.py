#letterFrequencyCounter

def letter_frequency_counter(text):
    count = {}
    for char in text.lower():
        count[char]= count.get(char, 0) + 1
    return count

text = str(input("Enter text: "))
frequency = letter_frequency_counter(text)
for letter, freq in frequency.items():
    print(f"'{letter}': {freq}")