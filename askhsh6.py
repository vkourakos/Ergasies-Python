from random import randrange
def chess_board():
    board = [ [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "] ]
    return board


def random_start_quinn(board):
    a = True
    qloc = [None] * 2
    while a:
        x = randrange(8)
        y = randrange(8)
        if board[x][y] == " ":
            board [x][y] = "Q"
            qloc[0], qloc[1] = x, y
            a = False
    return qloc 

def random_start_bishop(board):
    a = True
    bloc = [None] * 2
    while a:
        x = randrange(8)
        y = randrange(8)
        if board[x][y] == " ":
            board [x][y] = "B"
            bloc[0], bloc[1] = x, y
            a = False
    return bloc

def random_start_rook(board):
    a = True
    rloc = [None] * 2
    while a:
        x = randrange(8)
        y = randrange(8)
        if board[x][y] == " ":
            board [x][y] = "R"
            rloc[0], rloc[1] = x, y
            a = False
    return rloc

def rook_points(qloc, bloc, rloc):
    r_points = 0
    if rloc[0] == qloc[0]:
        if rloc[0] == bloc[0]:
            if (rloc[1] > bloc[1] and rloc[1] < qloc[1]) or (rloc[1] < bloc[1] and rloc[1] > qloc[1]):
                r_points = 1
                return r_points
            elif (rloc[1] < bloc[1] and rloc[1] < qloc[1]):
                if qloc[1] < bloc[1]:
                    r_points = 1
                    return r_points
                else:
                    r_points = 0
                    return r_points
            elif (rloc[1] > bloc[1] and rloc[1] > qloc[1]):
                if qloc[1] > bloc[1]:
                    r_points = 1
                    return r_points
                else:
                    r_points = 0
                    return r_points
        else:
            r_points = 1
            return r_points
    elif rloc[0] != qloc[0] and rloc[1] == qloc[1]:
        if rloc[1] == bloc[1]:
            if (rloc[0] > bloc[0] and rloc[0] < qloc[0]) or (rloc[0] < bloc[0] and rloc[0] > qloc[0]):
                r_points = 1
                return r_points
            elif (rloc[0] < bloc[0] and rloc[0] < qloc[0]):
                if qloc[0] < bloc[0]:
                    r_points = 1
                    return r_points
                else:
                    r_points = 0
                    return r_points
            elif (rloc[0] > bloc[0] and rloc[0] > qloc[0]):
                if qloc[0] > bloc[0]:
                    r_points = 1
                    return r_points
                else:
                    r_points = 0
                    return r_points
        else:
            r_points = 1
            return r_points 
    else:
        r_points = 0
        return r_points


def bishop_points(qloc, bloc, rloc):
    b_points = 0
    if bloc[0] == qloc[0]:
        b_points = 0
        return b_points
    elif bloc[0] != qloc[0] and bloc[1] == qloc[1]:
        b_points = 0
        return b_points
    elif qloc[0] > bloc[0] and qloc[1] > bloc[1]:  
        if qloc[1] - qloc[0] == bloc[1] - bloc[0]:
            if (rloc[0] > bloc[0] and rloc[1] > bloc[1]) and (rloc[1] - rloc[0] == bloc[1] - bloc[0]):
                if qloc[0] < rloc[0] and qloc[1] < rloc[1]:
                    b_points = 1
                    return b_points
                else:
                    b_points = 0
                    return b_points
            else:
                b_points = 1
                return b_points
        else:
            b_points = 0
            return b_points
    elif qloc[0] < bloc[0] and qloc[1] < bloc[1]:
        if qloc[1] - qloc[0] == bloc[1] - bloc[0]:
            if (rloc[0] < bloc[0] and rloc[1] < bloc[1]) and (rloc[1] - rloc[0] == bloc[1] - bloc[0]):
                if qloc[0] > rloc[0] and qloc[1] > rloc[1]:
                    b_points = 1
                    return b_points
                else:
                    b_points = 0
                    return b_points
            else:
                b_points = 1
                return b_points
        else:
            b_points = 0
            return b_points
    elif qloc[0] > bloc[0] and qloc[1] < bloc[1]:  
        if qloc[1] + qloc[0] == bloc[1] + bloc[0]:
            if (rloc[0] > bloc[0] and rloc[1] < bloc[1]) and (rloc[1] + rloc[0] == bloc[1] + bloc[0]):
                if qloc[0] < rloc[0] and qloc[1] > rloc[1]:
                    b_points = 1
                    return b_points
                else:
                    b_points = 0
                    return b_points
            else:
                b_points = 1
                return b_points
        else:
            b_points = 0
            return b_points
    elif qloc[0] < bloc[0] and qloc[1] > bloc[1]:  
        if qloc[1] + qloc[0] == bloc[1] + bloc[0]:
            if (rloc[0] < bloc[0] and rloc[1] > bloc[1]) and (rloc[1] + rloc[0] == bloc[1] + bloc[0]):
                if qloc[0] > rloc[0] and qloc[1] < rloc[1]:
                    b_points = 1
                    return b_points
                else:
                    b_points = 0
                    return b_points
            else:
                b_points = 1
                return b_points
        else:
            b_points = 0
            return b_points   

def quinn_points(qloc, bloc, rloc): 
    q_points = 0
    if qloc[0] == rloc[0]:
        if qloc[0] == bloc[0]:
            if (qloc[1] > rloc[1] and qloc[1] < bloc[1]) or (qloc[1] < rloc[1] and qloc[1] > bloc[1]):
                q_points = 2
                return q_points
            elif (qloc[1] < rloc[1] and qloc[1] < bloc[1]) or (qloc[1] > rloc[1] and qloc[1] > bloc[1]):
                q_points = 1
                return q_points
        else:
            q_points += 1
            if qloc[1] == bloc[1]:
                q_points += 1
                return q_points
            elif (qloc[1] + qloc[0] == bloc[1] + bloc[0]) or (qloc[1] - qloc[0] == bloc[1] - bloc[0]):
                q_points += 1
                return q_points
            else:
                return q_points                    
    elif qloc[0] == bloc[0]:
        q_points = 1            
        if qloc[1] == rloc[1]:
            q_points += 1
            return q_points
        elif  (qloc[1] + qloc[0] == rloc[1] + rloc[0]) or (qloc[1] - qloc[0] == rloc[1] - rloc[0]):
            q_points += 1
            return q_points
        else:
            return q_points

    elif qloc[1] == rloc[1]:
        if qloc[1] == bloc[1]:
            if (qloc[0] > rloc[0] and qloc[0] < bloc[0]) or (qloc[0] < rloc[0] and qloc[0] > bloc[0]):
                q_points = 2
                return q_points
            elif (qloc[0] < rloc[0] and qloc[0] < bloc[0]) or (qloc[0] > rloc[0] and qloc[0] > bloc[0]):
                q_points = 1
                return q_points
        else:
            q_points += 1
            if  (qloc[1] + qloc[0] == bloc[1] + bloc[0]) or (qloc[1] - qloc[0] == bloc[1] - bloc[0]):
                q_points += 1
                return q_points
            else:
                return q_points                    
    elif qloc[1] == bloc[1]:
        q_points = 1            
        if  (qloc[1] + qloc[0] == rloc[1] + rloc[0]) or (qloc[1] - qloc[0] == rloc[1] - rloc[0]):
            q_points += 1
            return q_points
        else:
            return q_points
    elif (qloc[1] - qloc[0] == bloc[1] - bloc[0]):
        if (qloc[1] - qloc[0] == rloc[1] - rloc[0]):
            if ((qloc[0] < bloc[0] and qloc[1] < bloc[1]) and (qloc[0] < rloc[0] and qloc[1] < rloc[1])) or ((qloc[0] > bloc[0] and qloc[1] > bloc[1]) and (qloc[0] > rloc[0] and qloc[1] > rloc[1])):
                q_points = 1
                return q_points
            else:
                q_points = 2
                return q_points
        else:
            q_points = 1
            if (qloc[1] + qloc[0] == rloc[1] + rloc[0]):
                q_points +=1
                return q_points
            else:
                return q_points
    elif (qloc[1] - qloc[0] == rloc[1] - rloc[0]):
        q_points = 1
        if (qloc[1] + qloc[0] == bloc[1] + bloc[0]):
            q_points +=1
            return q_points
        else:
            return q_points            
    elif (qloc[1] + qloc[0] == bloc[1] + bloc[0]):
        if (qloc[1] + qloc[0] == rloc[1] + rloc[0]):
            if ((qloc[0] > bloc[0] and qloc[1] < bloc[1]) and (qloc[0] > rloc[0] and qloc[1] < rloc[1])) or ((qloc[0] < bloc[0] and qloc[1] > bloc[1]) and (qloc[0] < rloc[0] and qloc[1] > rloc[1])):
                q_points = 1
                return q_points
            else:
                q_points = 2
                return q_points
        else:
            q_points = 1
            if (qloc[1] + qloc[0] == rloc[1] + rloc[0]):
                q_points +=1
                return q_points
            else:
                return q_points
    elif (qloc[1] + qloc[0] == rloc[1] + rloc[0]):
        q_points = 1
        return q_points
    else:
        q_points = 0
        return q_points   




def play_game():
    points = [0, 0]
    board = chess_board()
    qloc =  random_start_quinn(board)
    bloc =  random_start_bishop(board)
    rloc =  random_start_rook(board)
    white_points = rook_points(qloc, bloc, rloc) + bishop_points(qloc, bloc, rloc)
    black_points = quinn_points(qloc, bloc, rloc)
    points[0] = white_points
    points[1] = black_points
    return points



final_points = [0, 0]
for i in range (100):
    points = play_game()
    final_points[0] += points[0]
    final_points[1] += points[1] 
print ("Μετά από 100 παιχνίδια ο λευκός έχει " + str(final_points[0]) + " πόντους και ο μαύρος " + str(final_points[1]) + " πόντους.")    

                        


                
        


            
    
    
    
    
    
    
    
    
    
    
    
    
    



                                   


            

            
            







    
    
