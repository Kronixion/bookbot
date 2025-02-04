def count_characers(text):
    character_frequency_counter = {}
    for character in text:
        lower_character = character.lower()
        if lower_character in character_frequency_counter:
            character_frequency_counter[lower_character] += 1
        else:
            character_frequency_counter[lower_character] = 1
    return character_frequency_counter

def count_words(text):
    word_counter = 0
    for word in text.split():
        word_counter += 1
    return word_counter

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        counted_characters = count_characers(file_contents)
        for character_key in counted_characters:
            if ord(character_key) >= 97 and ord(character_key) <= 122:
                print(f"The '{character_key}' character was found {counted_characters[character_key]} times")

main()