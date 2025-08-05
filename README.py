import string
from collections import Counter

def analyze_text(text):
    # Remove punctuation for word analysis
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    words = clean_text.lower().split()
    
    # Count total words and characters
    total_words = len(words)
    total_characters = len(text)

    # Sentence count based on '.', '!' or '?'
    sentences = [s for s in text if s in '.!?']
    total_sentences = len(sentences)

    # Count word frequency
    word_counts = Counter(words)
    most_common_word, freq = word_counts.most_common(1)[0]

    # Display results
    print("---- Text Analysis ----")
    print(f"Total characters: {total_characters}")
    print(f"Total words: {total_words}")
    print(f"Total sentences: {total_sentences}")
    print(f"Most common word: '{most_common_word}' (appears {freq} times)")

# Example usage
user_input = input("Enter your text:\n")
analyze_text(user_input)
