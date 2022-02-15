

ascii_file = open("two_cities_ascii.txt", "r")

ascii_file = ascii_file.read()
#συνάρτηση για μετατροπή ascii σε 7 bit binary
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(7 * ((len(bits) + 7) // 8))

binary = text_to_bits(ascii_file)

#συνάρτηση για εύρεση μεγαλύτερης ακολουθίας από 0
def max_con_zeros(number):
    max0 = 0
    curr = 0
    for c in number:
        if c == '0':
            curr += 1
        else:
            if curr > max0:
                max0 = curr
            curr = 0
    if curr > max0:
        max0 = curr
    return max0

#συνάρτηση για εύρεση μεγαλύτερης ακολουθίας από 0
def max_con_ones(number):
    max1 = 0
    curr2 = 0
    for d in number:
        if d == '1':
            curr2 += 1
        else:
            if curr2 > max1:
                max1 = curr2
            curr2 = 0
    if curr2 > max1:
        max1 = curr2
    return max1


print ("Η μεγαλύτερη ακολουθία από συνεχόμενα 0 είναι " + str(max_con_zeros(binary)) + " και η μεγαλύτερη ακολουθία από συνεχόμενα 1 είναι " + str(max_con_ones(binary)))



