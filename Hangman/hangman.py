import random
print("H A N G M A N")
print()
word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
check_word = word
word_in_list = list(word)
empty_list = list("-" * len(word))

count = 0
ans = ""
print("".join(empty_list))
while count < 8:
    input_letter = input("Input a letter:")
    count1 = 0
    if input_letter in word_in_list:
        for i in word_in_list:
            count1 += 1
            if i == input_letter:
                empty_list[count1-1] = input_letter
        ans = "".join(empty_list)
        print()
        print(ans)
    else:
        print("No such letter in the word")
        print()
        print("".join(empty_list))
    count += 1
print()
print("Thanks for playing!")
print("We'll see how well you did in the next stage")
