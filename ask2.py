f = open("testpy.txt", "r")
data=f.read()
numofwords =len(data.split())
#χωρίζουμε το κείμενο σε λέξεις
words=data.split()
#ενα string με τα συμφωνα εκτος των κακων 
consonants = "bdghjlmnpqstvwxyz"
for i in words:
    words3 = list(i)
    bad=0
    good=0
    #ελεγχουμε τα γραμματα αν ειναι καλα ή κακα
    for j in words3:
        if j=="c" or j=="f" or j=="k" or j=="r":
            bad +=1
        elif j in consonants:
            good+=1
    if bad> good:
        print("bad word !",i)
    elif bad< good:
       print("good word!",i)
f.close()   
