ascii_file = open("two_cities_ascii.txt", "r")

ascii_file = ascii_file.read()
#κάνω την κατάλληλη επεξεργασία ώστε να  μείνει κείμενο με μόνο γράμματα και τον κενό χαρακτήρα 
whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ascii_text = ''.join(filter(whitelist.__contains__, ascii_file))

ascii_words = ascii_text.split()

words_len = [None] * len(ascii_words)

x = 0
#φτιάχνω λιστα με τα μηκη των λεξεων 
while x < len(ascii_words): 
    words_len[x] = len(ascii_words[x])
    x = x+1
#αφαιρώ τα ζευγάρια με άθροισμα γραμμάτων 20 επαναληπτικά μέχρι να μην υπάρχουν άλλα
no_more = False

while not(no_more): 
    sum = 0
    sum_counter = 0
    i = 0
    
    
    while i < len(words_len):
        if i == 0:
            sum += words_len[i]
            i += 1
            
            
        elif sum + words_len[i] == 20:
            del words_len[i-1:i+1]
            del ascii_words[i-1:i+1]
            sum = 0
            sum_counter += 1
            i -= 1
            
    
        elif  sum == 0:
            sum += words_len[i]
            i += 1 
                

        elif sum + words_len[i] != 20:
            sum = words_len[i]
            i += 1
            

    if sum_counter == 0:
        no_more = True

#φτιάχνω λεξικό που δείχνει (αριθμος γραμματων, αριθμος λεξεων με τοσα γραμματα)
counts = {}
for n in words_len:
    counts[n] = counts.get(n, 0) + 1
#το ταξινομώ
stats = sorted(counts.items())
print(stats)









        
        











