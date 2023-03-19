'''5.Write a function most frequent letters(s), that takes a string s and ignoring case
(so "A" and "a" are treated the same),returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.'''

'''word = 'we Attack at dawn'
letter = []
lettercount = [0]*26
final = ''
a = 0

word = word.lower()
word = word.replace(' ','')
finalword = ''

for x in word :

    letter.append(x)

unique = set(letter)
unique = list(unique)
unique.sort()

for y in unique :

    lettercount[a] = unique.count(y) 
    a+=1

for z in range(len(unique)) :

    final += str(unique[lettercount.index(max(lettercount))])
    lettercount[lettercount.index(max(lettercount))] = 0
print(final)'''


'''def most_frequent_letters(s):
    s = s.lower()
    letter_count = {}
    for c in s:
        if c.isalpha():
            letter_count[c] = letter_count.get(c, 0) + 1
    sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))
    return ''.join([l[0] for l in sorted_letters])'''
'''s = "We Attack at Dawn"
def most_frequent_letters(s):
    # Convert the input string to lowercase
    s = s.lower()
    
    # Create a dictionary to count the frequency of each letter
    freq_dict = {}
    for letter in s:
        if letter.isalpha():
            freq_dict[letter] = freq_dict.get(letter, 0) + 1
    
    # Sort the letters by frequency and then alphabetically
    sorted_letters = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    
    # Create the output string by concatenating the sorted letters
    output = ""
    for letter, freq in sorted_letters:
        output += letter * freq
    
    return output

print(most_frequent_letters(s))'''

char=''
charoccurence=[]
list=[]
char=input("Enter the charcter")
while char.lower()!='z':
    charoccurence.append(char)
    char=input("Enter the charcter")
list=[0]*len(charoccurence)
for i in range(len(charoccurence)):
    count=0
    if list[i]==0:
         for j in range(i+1,len(charoccurence)):
            if charoccurence[i]==charoccurence[j]:
                count+=1
                list[j]=1

print(charoccurence[i],count)


    



