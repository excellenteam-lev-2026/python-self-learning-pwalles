import string

def count_words(text):
    new_text = [char for char in text if char.isalpha() or char == ' ']
    cleacn_text = ''.join(new_text)
    words= cleacn_text.split()
    len_word={word: len(word) for word in words}
    return len_word

if __name__ == "__main__":
    text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""
    print(count_words(text))