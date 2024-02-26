
English_to_French={"hello": "bonjour", "my name edwige":"je m'appelle Edwige",
                    "et j'aime les prunes de mon pays": "and i like plums from my country"}

word = input("Enter a word in English: \n")

#translate word using dictionary
translate_word = English_to_French.get(word)

# check if the word was found in the dictionary
if translate_word is None:
   print(f" {word} is not in my memory.") 
else:
   print(f"The translation of {word} in french is \n {translate_word }") 
