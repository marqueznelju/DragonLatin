sentence = input('Enter a Sentence -> ').lower()
words = sentence.split()

for i, word in enumerate(words):

    # if first letter is vowel
    if word[0] in 'aeiou':
        words[i] = words[i] + "aey"

    else: # Get vowel position.
        has_vowel = False

        for x, letter in enumerate(word):
            if letter in 'aeiou':
                words[i] = word[x:] + word[:x] + "aey"
                has_vowel = True
                break

        # If word doesn't have any vowel then postfix "aey"
        if(has_vowel == False):
            words[i] = words[i] + "aey"

pig_latin = ' '.join(words)
print("Pig latin -> ", pig_latin)
