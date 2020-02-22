f = open("testpy.txt", "r")
data=f.read()
#σπαμε το κειμενο σε λεξεις συμφωνα με τα κενα που μεσολαβουν μεταξυ των λεξεων
numofwords =len(data.split())
#εισαιγουμε τις λεξεις 
words=data.split()
#ταξινομηση της λιστας συμφωνα με το μηκος της
lst = sorted(words, key=len)
#την αντιστρεφουμε
lst=lst[::-1]
vowels = ("A","a","e","E","I","i","O","o","U","u","Y","y")
for i in range(0,5):
    wv=""
    j=lst[i]
    for x in j:
        #ελεγχουμε αν καποιο γραμμα στις πρωτες πεντε μεγαλυτερες λεξεις
        #ειναι φωνηεν και το εκχωρουμε σε μια νεα μεταβλητη οπου
        #μετα την αφαιρεση των φωνηεντων εκχωρουμε την μεταβλητη αυτη
        #στην θεση της λεξης 
        if x not in vowels:
            wv+=x#Wv(without vowels)
          
    lst[i]=wv
reverse=lst[0:5]#κραταμε τις 5 μεγαλυτερες λεξεις χωρις φωνηεντα
newWords = [word[::-1] for word in reverse]#και εδω τις αντιστρεφουμε
print(newWords)

 
