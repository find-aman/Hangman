import random
print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
check_word = word
word_in_list = list(word)
empty_list = list("-" * len(word))
count = 0
ans = ""
while count < 8:
    print()
    print("".join(empty_list))
    input_letter = input("Input a letter:")
    count1 = 0
    if input_letter in word_in_list:
        if input_letter in empty_list:
            print("No improvements")
            count += 1
        else:
            for i in word_in_list:
                count1 += 1
                if i == input_letter:
                    empty_list[count1-1] = input_letter
            ans = "".join(empty_list)
    else:
        print("No such letter in the word")
        count += 1
if word == "".join(empty_list):
    print("You guessed the word!")
    print("You survived!")
else:
    print("You are hanged!")
