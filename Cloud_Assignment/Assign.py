import re
from collections import Counter

# Read the contents of the file (replace with your actual file path)
file_path = '/appllication/filtered.txt'
with open(file_path, "r") as file:
    text = file.read()

# Define a list of common stop words
stop_words = set(["i", "am", "and", "is", "my", "thr", "the", "a", "an", "in", "of", "to", "for", "with", "that", "this", "it", "on", "as", "by"])

# Use regular expression to find words and filter out stop words
filtered_words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in stop_words]

# Count the frequency of each word
word_counts = Counter(filtered_words)

# Order words by frequency (descending)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Display word frequency count
for word, count in sorted_word_counts:
    print(f"{word}: {count}")