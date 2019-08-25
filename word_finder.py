#import permutations module and timer
import time
from itertools import permutations

#define counter and empty lists
ctr = 0
wordCombo = []
wordLet = []
longCtr = 0
filterWords = []
finalList = []
comboPerms = []
allPerms = []

#removes duplicates from list
def noRepeats(x):
  return list(dict.fromkeys(x))

#function to convert list to string
def convert(list):
    s = [str(i) for i in list]
    res = str(", ".join(s))
    print(res)

#convert list of letters into strings
def convertLet(list):
    s = [str(i) for i in list]
    res = str("".join(s))
    print(res)

#function to remove 2 and 1 letter words
def removeShortPerms(wordss):
    return [i for i in wordss if len(i) >= 3]

#get user input
userLet = input("Enter letters(up to 8):")
start_time = time.time()
userLen = len(userLet)
if userLen > 8:
    print("Too many letters!\n")
    exit()

#open words doc and split words into list
with open("everyword.rtf") as f:
    words = f.read().split()
words = [x.lower() for x in words]
wordsLen = len(words)

#find all permutations of user input
perms = [''.join(p) for p in permutations(userLet)]
permsLen = len(perms)

print("\nLoading permutations...")
#print("All permutations: ", perms)

#filter out words longer than the user-submitted letters(or too short)
for z in range(0, wordsLen):
    if 3 <= len(words[z]) <= userLen:
        filterWords.append(words[z])
filterLen = len(filterWords)

#create smaller permutations
def shorterPerms(num):
    newPerms = []
    for y in range(0, permsLen):
        miniPerm = perms[y]
        miniPerm = miniPerm[num : : ]
        newPerms.append(miniPerm)
    return newPerms

#add all perm lists depending on number of letters
if userLen == 1:
    allPerms = perms

if userLen == 2:
    allPerms = perms

if userLen == 3:
    allPerms = perms

if userLen == 4:
    for i in range(1, userLen):
        comboPerms+= list(dict.fromkeys(shorterPerms(i)))
    allPerms = perms + comboPerms

if userLen == 5:
    for i in range(1, userLen):
        comboPerms+= list(dict.fromkeys(shorterPerms(i)))
    print(comboPerms)
    allPerms = perms + comboPerms

if userLen == 6:
    for i in range(1, userLen):
        comboPerms+= list(dict.fromkeys(shorterPerms(i)))
    allPerms = perms + comboPerms

if userLen == 7:
    for i in range(1, userLen):
        comboPerms+= list(dict.fromkeys(shorterPerms(i)))
    allPerms = perms + comboPerms

if userLen == 8:
    for i in range(1, userLen):
        comboPerms+= list(dict.fromkeys(shorterPerms(i)))
    allPerms = perms + comboPerms

allPerms = list(dict.fromkeys(allPerms))
allPerms = removeShortPerms(allPerms)
allPermsLen = len(allPerms)

#find match with perms from word doc
print("Finding matches...\n")
for x in range(0, allPermsLen):
    for y in range(0, filterLen):
        if allPerms[x] == filterWords[y]:
            finalList.append(allPerms[x])

finalWords = str(convert(noRepeats(finalList)))
print("\n")
print ("My program took", time.time() - start_time, "seconds to run\n")
