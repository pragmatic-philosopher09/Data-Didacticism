
file = open("C:\\Users\\hp\\Data Didacticism\\Python Skills\\poem.txt","r+")

word_count = {}
for line in file:
    for word in line.split(' '):
        if word.isalpha() == False:
            if word[-1]=="\n":
                word_count[word[:-2]] = word_count.get(word[:-2],0)+1
            else:
                word_count[word[:-2].lower()] = word_count.get(word[:-2],0)+1

        else:
            word_count[word.lower()] = word_count.get(word,0)+1



 
max_occurence_word = max(word_count, key=word_count.get)
max_occurence_freq = word_count[max_occurence_word]

print(f"WORD WITH MAX. OCCURENCE ==> {max_occurence_word}")
            
print(word_count)

print("Words with max occurances are: ")
for word, count in word_count.items():
    if count==max_occurence_freq:
        print(word)
