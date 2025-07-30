# pig latin is a made up language:
# rules of the language:
"""
* if a word starts with a vowel, then at the end of the word we add the "yay " string to it
* if a word starts with a consonant or consonant clusted like 'ch' or ' 'gr', then that consonant or consonant cluster is moved to the end
of the word and added am 'ay' sting after it

"""

def main():
    print("Enter the English message to translate into pig latin:")
    message = input()
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
    message_list = message.split()
    pig_latin = [] # contains the pig latins words
    
    for word in message_list:

        # separate the non letters at the start of the word
        prefix_non_letters = ""

        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]


        # separate the non letters at the end of the word
        suffix_non_letters = ""
        while len(word) > 0 and not word[-1].isalpha():   # if the suffix of the word is not a letter then run the program. It has to contain at least a charater as well to run the statement
            suffix_non_letters = word[-1] + suffix_non_letters
            word = word[:-1]

        # keep track of the word been upper or title. if lower when we convert it to lower it will stay that way
        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower()  # word is converted to lower to been able to know with the vowels that are in lower case. 
                            # After having added the pig latin acent and change the world we will be typecasting the word to how it was with the vars
                            # was_upper and was_title or if not leave it as it lower if it was lower
                            # then we add the prefix and the suffix to the word and that would make it pretty ready to return the string by joining it.



        # step of adding latin pig accent to the word                            
        if word[0] not in VOWELS:
            stored_beginning_str = ""                     
            while len(word) > 0 and word[0] not in VOWELS:
                stored_beginning_str += word[0]
                word = word[1:]
            if was_upper:
                word = word.upper()
            if was_title:
                word = word.title()
            final_word_result = prefix_non_letters + word + stored_beginning_str + 'ay' + suffix_non_letters
        else:
            final_word_result = prefix_non_letters + word + 'yay' + suffix_non_letters
        word = final_word_result
        pig_latin.append(word)
    print(' '.join(pig_latin))


if __name__ == "__main__":
    main()

    



