vowel=['a','e','i','o','u']

while True:
    sen=input()
    if sen == '#':
        break

    vowel_cnt = 0
    sen=sen.lower()

    for char in sen:
        if char in vowel:
            vowel_cnt += 1
            
    print(vowel_cnt)