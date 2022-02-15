
import random


def game_table():
    table =  [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]    #φτιάχνω τον πίνακα
    return table          
    
def player():
    player = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "0", "0", "0", "0", "0", "0", "0", "0", "0", "O", "O", "O", "O", "O", "O", "O", "O", "O"]          
    # μικρά καπάκια : o, μεσαία καπάκια: 0, μεγάλα καπάκια: O
    return player

def get_random_cap(caps):
    return random.choice(caps)  #διαλέγω τυχαίο καπάκι 
    
    

def get_av_loc(cap, tab):  #εντοπίζω διαθέσιμες τοποθεσίες για να βάλω το καπάκι
    l = [None] * 9
    index = 0
    index2 = 0
    if cap == "o":
        for x in tab:
            if x == " ":
                l[index] = index2
                index += 1
            index2 += 1        
        av_loc = []
        for val in l:
            if val != None :
                av_loc.append(val)
        return av_loc
    
    elif cap == "0":
        for x in tab:
            if x == " " or x == "o":
                l[index] = index2
                index += 1
            index2 += 1        
        av_loc = []
        for val in l:
            if val != None :
                av_loc.append(val)
        return av_loc

    else:
        for x in tab:
            if x == " " or x == "o" or x == "0":
                l[index] = index2
                index += 1
            index2 += 1        
        av_loc = []
        for val in l:
            if val != None :
                av_loc.append(val)
        return av_loc    

def check_hor(tab): #ελέγχω για τριάδα οριζόντια
    win = False
    if (tab[0] == "o" and tab[0] == tab[1] and tab[1] == tab[2]) or (tab[0] == "0" and tab[0] == tab[1] and tab[1] == tab[2]) or (tab[0] == "O" and tab[0] == tab[1] and tab[1] == tab[2]) or  (tab[3] == "o" and tab[3] == tab[4] and tab[4] == tab[5]) or (tab[3] == "0" and tab[3] == tab[4] and tab[4] == tab[5]) or (tab[3] == "O" and tab[3] == tab[4] and tab[4] == tab[5]) or  (tab[6] == "o" and tab[6] == tab[7] and tab[7] == tab[8]) or (tab[6] == "0" and tab[6] == tab[7] and tab[7] == tab[8]) or (tab[6] == "O" and tab[6] == tab[7] and tab[7] == tab[8]) or (tab[0] == "o" and tab[1] == "0" and tab[2] == "O") or (tab[0] == "O" and tab[1] == "0" and tab[2] == "o") or (tab[3] == "o" and tab[4] == "0" and tab[5] == "O") or (tab[3] == "O" and tab[4] == "0" and tab[5] == "o") or (tab[6] == "o" and tab[7] == "0" and tab[8] == "O") or (tab[6] == "O" and tab[7] == "0" and tab[8] == "o"):
        win = True

    return win

def check_ver(tab): #ελέγχω για τριάδα κάθετα
    win = False
    if (tab[0] == "o" and tab[0] == tab[3] and tab[3] == tab[6]) or (tab[0] == "0" and tab[0] == tab[3] and tab[3] == tab[6]) or (tab[0] == "O" and tab[0] == tab[3] and tab[3] == tab[6]) or  (tab[1] == "o" and tab[1] == tab[4] and tab[4] == tab[7]) or (tab[1] == "0" and tab[1] == tab[4] and tab[4] == tab[7]) or (tab[1] == "O" and tab[1] == tab[4] and tab[4] == tab[7]) or  (tab[2] == "o" and tab[2] == tab[5] and tab[5] == tab[8]) or (tab[2] == "0" and tab[2] == tab[5] and tab[5] == tab[8]) or (tab[2] == "O" and tab[2] == tab[5] and tab[5] == tab[8]) or (tab[0] == "o" and tab[1] == "0" and tab[2] == "O") or (tab[0] == "O" and tab[1] == "0" and tab[2] == "o") or (tab[3] == "o" and tab[4] == "0" and tab[5] == "O") or (tab[3] == "O" and tab[4] == "0" and tab[5] == "o") or (tab[6] == "o" and tab[7] == "0" and tab[8] == "O") or (tab[6] == "O" and tab[7] == "0" and tab[8] == "o"):
        win = True

    return win

def check_diag(tab): #ελέγχω για τριάδα διαγώνια
    win = False
    if (tab[0] == "o" and tab[0] == tab[4] and tab[4] == tab[8]) or (tab[0] == "0" and tab[0] == tab[4] and tab[4] == tab[8]) or (tab[0] == "O" and tab[0] == tab[4] and tab[4] == tab[8]) or  (tab[2] == "o" and tab[2] == tab[4] and tab[4] == tab[6]) or (tab[2] == "0" and tab[2] == tab[4] and tab[4] == tab[6]) or (tab[2] == "O" and tab[2] == tab[4] and tab[4] == tab[6]) or (tab[0] == "o" and tab[4] == "0" and tab[8] == "O") or (tab[0] == "O" and tab[4] == "0" and tab[8] == "o") or (tab[2] == "o" and tab[4] == "0" and tab[6] == "O") or (tab[2] == "O" and tab[4] == "0" and tab[6] == "o"):
        win = True

    return win

def play_game():
    board = game_table()
    winner = False 
    steps = 0
    player_items = player() 
    while not(winner):
        player_cap = get_random_cap(player_items)
        player_items.remove(player_cap)
        pos_loc = get_av_loc(player_cap, board)
        if pos_loc != []:  
            loc = random.choice(pos_loc)
            board[loc] = player_cap
            steps += 1
            if check_hor(board) or check_ver(board) or check_diag(board):
                winner = True
    return steps


steps_count = 0
for i in range (100):
    steps_count += play_game()

print ("Ο μέσος όρος βημάτων για να λήξει το παιχνίδι είναι " + str(steps_count /100))



        



