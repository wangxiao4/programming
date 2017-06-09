import _6_11_RandomCharacter

number_of_chars=175
chars_per_line=25
for i in range(number_of_chars):
    if i%chars_per_line==0:
        print()
    print(_6_11_RandomCharacter.getRandomLowerCaseLetter(),end="")