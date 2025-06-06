def match_words(words):
    ctr=0
    list=[]
    for word in words:
        len(word) > 1 and word[0]==word[-1]
        ctr=ctr+1
        list.append(word)
        print("words with first and last letter same\n",list)
        return ctr
count=match_words(["abc","fgr","hiii","ghhhh"])
print("letters with first and last word same are",count)