vowels = "aeiouAEIOU"
word = input("Enter your word: ").split(" ")

pig_latin = []


def translator():
    for each_word in range(len(word)):

        for letter in range(len(word[each_word])):

            if(word[each_word][0] in vowels):
                pig_latin_word = word[each_word] + "-way"
                pig_latin.append(pig_latin_word)
                break
            
            else:
                first_bit = word[each_word][:letter+1]
                pig_latin_word = word[each_word][letter+1:len(word[each_word])] + "-" + first_bit + "ay"
                pig_latin.append(pig_latin_word)
                break

            
    

        
if __name__ == "__main__":
    translator()
    for i in range(len(word)):
        print(pig_latin[i].capitalize(), end =" ")


