import random
def main():
    file = open("words.txt", "r")
    wordList=[word for word in file]
    numPassGenerated=int(input("Number of passwords to generate: "))
    numWordsPerPass=int(input("Number of words per password: "))
    passes=[]
    print("\n")
    for x in range (0, numPassGenerated):
        newPass=""
        for y in range (0, numWordsPerPass):
            newPass+=str(wordList[random.randrange(len(wordList))])+str(random.randrange(10))+"-"
        print(newPass.replace("\n","")[:-1])

if __name__ == "__main__":
    main()