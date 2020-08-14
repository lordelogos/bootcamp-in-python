def longestStr(arr):
    return max(arr, key= len)


N = int(input('Enter length of wordlist: '))
wordlist = []
for i in range(N):
    word = input('Enter word: ')
    wordlist.append(word)


print('The longest word in your list is ' + longestStr(wordlist))
