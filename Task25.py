words = input("Input some words :")
print(f"\nYour words: \n{words}")

words_list = words.split()
long_word = 0

for i in range(1, len(words_list)):
    if len(words_list[long_word]) < len(words_list[i]):
        long_word = (i)

print(f"\nThe longest word is: \n{words_list[long_word]}")
