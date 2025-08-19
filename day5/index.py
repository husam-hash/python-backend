text = "apple banana apple orange banana apple pear"


words = text.split()
unique_words = set(words)
print("Unique words:", unique_words)


word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord frequencies:")
for word, count in word_freq.items():
    print(f"{word}: {count}")



dict1 = {"apple": 3, "banana": 2, "cherry": 5}
dict2 = {"banana": 4, "cherry": 1, "date": 7}

merged_dict = {}

for key in set(dict1) | set(dict2):  
    if (v1 := dict1.get(key)) and (v2 := dict2.get(key)):
       
        merged_dict[key] = v1 + v2
    else:
      
        merged_dict[key] = v1 if v1 is not None else v2

print("\nMerged dictionary:")
print(merged_dict)
