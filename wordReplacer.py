#wordReplacer

def replace_words_with_emojis(text, emoji_dict):
    text = text.lower()
    for word, emoji in emoji_dict.items():
        text = text.replace(word, emoji)
    return text


emoji_dict = {
    "happy": "😄",
    "sad": "😢",
    "cat": "🐱",
    "dog": "🐶",
    "fire": "🔥",
    "love": "❤️",
    "sun": "☀️",
    "moon": "🌙",
    "star": "⭐",
    "food": "🍔"
}

text = str(input("Enter a sentence: "))

result = replace_words_with_emojis(text, emoji_dict)
print("Modified sentence:", result)