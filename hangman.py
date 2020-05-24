import random
def start_Game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_list)
    word_in_list = list(word)
    empty_list = list("-" * len(word))
    count = 0
    ans = ""
    already_entered_list = list()
    while count < 8:
        print()
        print("".join(empty_list))
        input_letter = input("Input a letter:")
        count1 = 0
        if len(input_letter) == 1:
            if ord(input_letter) >= 97 and ord(input_letter) <= 122:
                if input_letter in already_entered_list:
                    print("You already typed this letter")
                else:
                    already_entered_list.append(input_letter)
                    if input_letter in word_in_list:
                        if input_letter in empty_list:
                            print("You already typed this letter")
                        else:
                            for i in word_in_list:
                                count1 += 1
                                if i == input_letter:
                                    empty_list[count1 - 1] = input_letter
                            ans = "".join(empty_list)
                    else:
                        print("No such letter in the word")
                        count += 1
                    if ans == word:
                        print(ans)
                        break
            else:
                print("It is not an ASCII lowercase letter")
        else:
            print("You should input a single letter")

    if word == "".join(empty_list):
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")

def ask_user():
    print("H A N G M A N")
    user_input = input('Type "play" to play the game, "exit" to quit:')
    while True:
        if user_input == 'play':
            start_Game()
            user_input = input('Type "play" to play the game, "exit" to quit:')
        elif user_input == 'exit':
            break
        else:
            user_input = input('Type "play" to play the game, "exit" to quit:')
ask_user()