cardnum=input("Enter your card number without spaces: ")
odds=[]
evens=[]
summ=0
digits2=[int(d) for d in str(cardnum)]
digits=digits2[::-1]#αντιστρεφουμε τα ψηφια οπως λεει ο αλγοριθμος του λουν


for x in range(0, len(cardnum)): 
    if x % 2 !=0: 
        odds.append(digits[x]) #οσα ειναι σε ζυγές θέσεις(περιττές μετα την αντιστροφη) με την κανονική μορφη
    else : 
        evens.append(digits[x]) #οσα ειναι σε περιττες θέσεις(ζυγες μετα την αντιστροφή) με την κανονική μορφη 

for i in range(len(odds)):
    odds[i]=odds[i]*2   #διπλασιαζουμε τους odds οπως λεει ο  αλγοριθμος του λουν 
for i in range(0,len(odds)):
    total=0#βοηθητικη μεταβλητη για τα διπλασιασμενα ψηφια που εχουν μηκος πανω απο 1 
    oddstr=str(odds[i])#χρησιμοποιουμε ενα string για να προσδιορισουμε το μηκος του ψηφιου 
    if len(oddstr)!=1:#αν ειναι διαφορο του ενα δηλαδη 2 και πανω, προσθέτουμε τα ψηφία του 
        for j in range (len(oddstr)):
           
           total+=int(oddstr[j])#εκχωρουμε το καθε ψηφιο και το προσθετουμε στην βοηθητικη total κανοντας το ακεραιο 
        odds[i]=total#εκχωρουμε την total στην θεση του διπλασιασμενου αριθμου που αποτελειται απο 2 ψηφια
  
summ=sum(odds)+sum(evens)#αθροισμα των διπλασιασμενων αριθμων και των αριθμων ενδιαμεσα 

if summ%10==0:#ελεγχουμε το αθροισμα mod 10 αν ισουται με το 0 ετσι ωστε να δουμε αν ειναι εγκυρη ή όχι (οπως λέει ο αλγοριθμος του Λουν)
    print("Card is valid")
else:
    print("Card is not valid")
