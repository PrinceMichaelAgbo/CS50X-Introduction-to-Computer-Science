# ----------------------------------------------------------
# --------          CS50 Final Project              --------
# ----------------------------------------------------------

# ----------------------------------------------------------
#Name:Prince Michael Agbo
#Title: Snakes and Ladders
#Number of Players: 2
#IDE: IDLE
#Location: International student from Nigeria studying in the USA.
#
#
#
#
# ----------------------------------------------------------

import turtle
import random
import time

WIDTH = 10
HEIGHT = 10

snake1 = [97,85,75,67,53,49]
snake2 = [63,57,45,35,27,13]
ladder1 = [39,42,59,62,79,82]
ladder2 = [4,16,26,34,48,52]


def valid_input(player_num):
    """
    This function ensures that the players enter the valid input of "r" to roll the die
    """
    player_input = input("Player "+str(player_num)+ " enter r to roll the die: ")
    player_input = player_input.lower()
    
    while player_input != "r":
        print("Invalid input")
        player_input = input("Player "+str(player_num)+" enter r to roll the die: ")
        player_input = player_input.lower()    

def winner(position, player):
    """
    This function checks if a player has gotten to the 100th square and has thus won the game
    """
    if position == 100:
        print("Congratulations,",player + ", you have won.")
        return True
    else:
        return False

def create_dictionary():
    """
    This function creates a dictionary that maps a numerical position (from 1 to 1000
    to an x,y axis location so that squares can be easily referenced with numbers (from 1 to 100)
    instead of x,y axis positions
    """
    d = {}
    for y in range(HEIGHT):
        if (y % 2) != 0:
            pos = (10*y)+10
        else:
            pos =((10*y)-9)+10 
        for x in range(WIDTH):
            xy_tuple = (x,y)
            d[pos] = xy_tuple
            if (y % 2) != 0:
                pos = pos - 1
            else:
                pos = pos + 1
    
    return d
            

def write_num(x,y,t,pos):
    """
    This function writes the square number in the middle of
    square
    """
    moveturtle(x+0.5,y+0.5,t)
    t.write(pos)
    moveturtle(x,y,t)

def moveturtle(x,y,t):
    """
       This function moves the turtle to the coordinates (x,y)
       without leaving a line trail.
    """
    t.penup()
    t.goto(x,y)
    t.pendown()

def filldraw_rectangle(x,y,width,height,t,color):   
    moveturtle(x,y,t)
    t.fillcolor(color)
    t.begin_fill()
    for draw in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def positions1(player1_pos,player2_pos,d,t,roll_num1):
    
    #if snake positions change and its tail is in first row, will need to include
    #if (player1_pos - roll_num1) != 0: before any code that involves (player1_pos - roll_num1)
        
    
    #to recolor last position
    if (player1_pos - roll_num1) not in snake1 and (player1_pos - roll_num1) not in snake2 and (player1_pos - roll_num1) not in ladder1 and (player1_pos - roll_num1) not in ladder2:
        if (player1_pos - roll_num1) != 0:
            filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"red")#recolor last position red if it was not a snake and not a ladder
            write_num(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],t,player1_pos-roll_num1)
    else:
        if (player1_pos - roll_num1) in snake1 or (player1_pos - roll_num1) in snake2:
            if (player1_pos - roll_num1) != 0:
                filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"green")#recolor last position green if it was a snake
                write_num(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],t,player1_pos-roll_num1)
        elif (player1_pos - roll_num1) in ladder1 or (player1_pos - roll_num1) in ladder2:
            if (player1_pos - roll_num1) != 0:
                filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"yellow")#recolor last position yellow if it was a ladder
                write_num(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],t,player1_pos-roll_num1)
        
    if player1_pos not in snake1 and player1_pos not in snake2 and player1_pos not in ladder1 and player1_pos not in ladder2:
        #if current position is not a snake body and not a ladder body, color current position white
        filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"white")
        write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos)                
    else:
        if player1_pos in snake1 or player1_pos in snake2: #if current position is snake body
            filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"green") #make current position green
            write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos)
            if (player1_pos - roll_num1) not in ladder1 and (player1_pos - roll_num1) not in ladder2 and (player1_pos - roll_num1) not in snake1 and (player1_pos - roll_num1) not in snake2:
                #if last position is not a ladder or snake body
                if (player1_pos - roll_num1) != player2_pos:#if last position is also not player 2 position
                    filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"red") #color last position red
                    write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
                else:#if last position is also player 2 position
                    filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"orange") #color last position orange
                    write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
            elif (player1_pos - roll_num1) in ladder1 or (player1_pos - roll_num1) in ladder2:
                #if last position is a ladder body
                if (player1_pos - roll_num1) != player2_pos:#if last position is also not player 2 position
                    filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"yellow") #color last position yellow
                    write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
                else:#if last position is also player 2 position
                    filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"orange") #color last position orange
                    write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
            elif (player1_pos - roll_num1) in snake1 or (player1_pos - roll_num1) not in snake2:
                #if last position is a snake body
                if (player1_pos - roll_num1) != player2_pos:#if last position is also not player 2 position
                    filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"green") #color last position yellow
                    write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
                else:#if last position is also player 2 position
                    filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"orange") #color last position orange
                    write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)

                
            if player1_pos in snake1: #if current position in snake1 body
                if player1_pos != snake1[5]:
                    print ("Player 1 has hit a snake and will slide down to", snake1[5])
                player1_pos = snake1[5] #slide down by updating current position to snake 1 tail
                filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"white")#color snake tail white
                write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos)
            elif player1_pos in snake2: #if current position in snake2 body
                if player1_pos != snake2[5]:
                    print ("Player 1 has hit a snake and will slide down to", snake2[5])
                player1_pos = snake2[5] #slide down by updating current position to snake 1 tail
                filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"white")#color snake tail white
                write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos)
        elif player1_pos in ladder1 or player1_pos in ladder2:#if current position is ladder body
            filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"yellow") #make current position yellow
            write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos)
            if (player1_pos - roll_num1) not in snake1 and (player1_pos - roll_num1) not in snake2 and (player1_pos - roll_num1) not in ladder1 and (player1_pos - roll_num1) not in ladder2:
                #if last position is not a snake or ladder body
                if (player1_pos - roll_num1) != player2_pos:#if last position is also not player 2 position
                    if (player1_pos - roll_num1) != 0:
                        filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"red") #color last position red
                        write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
                else:#if last position is also player 2 position
                    if (player1_pos - roll_num1) != 0:
                        filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"orange") #color last position orange
                        write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
            elif (player1_pos - roll_num1) in snake1 or (player1_pos - roll_num1) in snake2:
                #if last position is a snake body
                if (player1_pos - roll_num1) != player2_pos:#if last position is also not player 2 position
                    if (player1_pos - roll_num1) != 0:
                        filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"green") #color last position green
                        write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
                else:#if last position is also player 2 position
                    if (player1_pos - roll_num1) != 0:
                        filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"orange") #color last position orange
                        write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
            elif (player1_pos - roll_num1) in ladder1 or (player1_pos - roll_num1) in ladder2:
                #if last position is a ladder body
                if (player1_pos - roll_num1) != player2_pos:#if last position is also not player 2 position
                    if (player1_pos - roll_num1) != 0:
                        filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"yellow") #color last position yellow
                        write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
                else:#if last position is also player 2 position
                    if (player1_pos - roll_num1) != 0:
                        filldraw_rectangle(d[player1_pos - roll_num1][0],d[player1_pos - roll_num1][1],1,1,t,"orange") #color last position orange
                        write_num(d[player1_pos-roll_num1][0],d[player1_pos-roll_num1][1],t,player1_pos-roll_num1)
            
            
            if player1_pos in ladder1: #if current position in ladder1 body
                if player1_pos != ladder1[5]:
                    print ("Player 1 has hit a ladder and will climb up to", ladder1[5])
                player1_pos = ladder1[5] #climb up by updating current position to ladder 1 top
                filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"white")#color ladder 1 head white
                write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos)
            elif player1_pos in ladder2: #if current position in ladder2 body
                if player1_pos != ladder2[5]:
                    print ("Player 1 has hit a ladder and will climb up to", ladder2[5])
                player1_pos = ladder2[5] #climb up by updating current position to ladder 2 top
                filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"white")#color ladder 2 head white
                write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos) 

    if player2_pos == player1_pos or player2_pos == (player1_pos - roll_num1): #if player 2 is or was in the same position as player 1, make the current or past position orange
        if (player1_pos - roll_num1) != 0:
            filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"orange")
            write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos)                     
                
    return player1_pos
            
    

def positions2(player2_pos,player1_pos,d,t, roll_num2):
        
    #to recolor last position
    if (player2_pos - roll_num2) not in snake1 and (player2_pos - roll_num2) not in snake2 and (player2_pos - roll_num2) not in ladder1 and (player2_pos - roll_num2) not in ladder2:
        if (player2_pos - roll_num2) != 0:
            filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"red")#recolor last position red if it was not a snake and not a ladder
            write_num(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],t,player2_pos-roll_num2)
    else:
        if (player2_pos - roll_num2) in snake1 or (player2_pos - roll_num2) in snake2:
            if (player2_pos - roll_num2) != 0:
                filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"green")#recolor last position green if it was a snake
                write_num(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],t,player2_pos-roll_num2)
        elif (player2_pos - roll_num2) in ladder1 or (player2_pos - roll_num2) in ladder2:
            if (player2_pos - roll_num2) != 0:
                filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"yellow")#recolor last position yellow if it was a ladder
                write_num(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],t,player2_pos-roll_num2)
        
    if player2_pos not in snake1 and player2_pos not in snake2 and player2_pos not in ladder1 and player2_pos not in ladder2:
        #if current position is not a snake body and not a ladder body, color current position orange
        filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"orange")
        write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos)                
    else:
        if player2_pos in snake1 or player2_pos in snake2: #if current position is snake body
            filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"green") #make current position green
            write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos)
            if (player2_pos - roll_num2) not in ladder1 and (player2_pos - roll_num2) not in ladder2 and (player2_pos - roll_num2) not in snake1 and (player2_pos - roll_num2) not in snake2:
                #if last position is not a ladder or snake body
                if (player2_pos - roll_num2) != player1_pos:#if last position is also not player 1 position
                    filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"red") #color last position red
                    write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
                else:#if last position is also player 1 position
                    filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"white") #color last position white
                    write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
            elif (player2_pos - roll_num2) in ladder1 or (player2_pos - roll_num2) in ladder2:
                #if last position is a ladder body
                if (player2_pos - roll_num2) != player1_pos:#if last position is also not player 1 position
                    filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"yellow") #color last position yellow
                    write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
                else:#if last position is also player 1 position
                    filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"white") #color last position white
                    write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
            elif (player2_pos - roll_num2) in snake1 or (player2_pos - roll_num2) in snake2:
                #if last position is a snake body
                if (player2_pos - roll_num2) != player1_pos:#if last position is also not player 1 position
                    filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"green") #color last position green
                    write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
                else:#if last position is also player 1 position
                    filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"white") #color last position white
                    write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)                                        

            
            if player2_pos in snake1: #if current position in snake1 body
                if player2_pos != snake1[5]:
                    print ("Player 2 has hit a snake and will slide down to", snake1[5])
                player2_pos = snake1[5] #slide down by updating current position to snake 1 tail
                filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"orange")#color snake tail orange
                write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos)
            elif player2_pos in snake2: #if current position in snake2 body
                if player2_pos != snake2[5]:
                    print ("Player 2 has hit a snake and will slide down to", snake2[5])
                player2_pos = snake2[5] #slide down by updating current position to snake 1 tail
                filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"orange")#color snake tail orange
                write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos)
        elif player2_pos in ladder1 or player2_pos in ladder2:#if current position is ladder body
            filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"yellow") #make current position yellow
            write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos)
            if (player2_pos - roll_num2) not in ladder1 and (player2_pos - roll_num2) not in ladder2 and (player2_pos - roll_num2) not in snake1 and (player2_pos - roll_num2) not in snake2:
                #if last position is not a snake or ladder body
                if (player2_pos - roll_num2) != player1_pos:#if last position is also not player 1 position
                    if (player2_pos - roll_num2) != 0:
                        filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"red") #color last position red
                        write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
                else:#if last position is also player 1 position
                    if (player2_pos - roll_num2) != 0:
                        filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"white") #color last position white
                        write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
            elif (player2_pos - roll_num2) in snake1 or (player2_pos - roll_num2) in snake2:
                #if last position is a snake body
                if (player2_pos - roll_num2) != player1_pos:#if last position is also not player 1 position
                    if (player2_pos - roll_num2) != 0:
                        filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"green") #color last position green
                        write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
                else:#if last position is also player 1 position
                    if (player2_pos - roll_num2) != 0:
                        filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"white") #color last position white
                        write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
            elif (player2_pos - roll_num2) in ladder1 or (player2_pos - roll_num2) in ladder2:
                #if last position is a ladder body
                if (player2_pos - roll_num2) != player1_pos:#if last position is also not player 1 position
                    if (player2_pos - roll_num2) != 0:
                        filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"yellow") #color last position yellow
                        write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)
                else:#if last position is also player 1 position
                    if (player2_pos - roll_num2) != 0:
                        filldraw_rectangle(d[player2_pos - roll_num2][0],d[player2_pos - roll_num2][1],1,1,t,"white") #color last position white
                        write_num(d[player2_pos-roll_num2][0],d[player2_pos-roll_num2][1],t,player2_pos-roll_num2)

            if player2_pos in ladder1: #if current position in ladder1 body
                if player2_pos != ladder1[5]:
                    print ("Player 2 has hit a ladder and will climb up to", ladder1[5])
                player2_pos = ladder1[5] #climb up by updating current position to ladder 1 top
                filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"orange")#color ladder 1 head orange
                write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos)
            elif player2_pos in ladder2: #if current position in ladder2 body
                if player2_pos != ladder2[5]:
                    print ("Player 2 has hit a ladder and will climb up to", ladder2[5])
                player2_pos = ladder2[5] #climb up by updating current position to ladder 2 top
                filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"orange")#color ladder 2 head orange
                write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos) 

    if player1_pos == player2_pos or player1_pos == (player2_pos - roll_num2):#if player 1 is or was in the same position as player 2, make the current or past position white
        if (player2_pos - roll_num2) != 0:
            filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"white")
            write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos)

    return player2_pos
    
def track_player1(player1_pos, d, t, player2_pos):
    """
    This function controls and tracks player 1
    """
    valid_input(1)
    roll_num = die_roll()
    player1_pos = player1_pos + roll_num
    print("Player 1 rolls",roll_num,end="")
    if player1_pos <= 100:
        print(" and moves to box",player1_pos)
    else:
        print(", which makes the next position greater than 100")
        player1_pos = player1_pos - roll_num
        if player2_pos == player1_pos:#accounting for bounceback, if player2 was in same position as player1 before player1 bounces back from 100
            filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"orange")
        else: #else color it red (will be colored white if player1 bounces back to same position)
            filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"red")
            write_num(d[player1_pos][0],d[player1_pos][1],t,player1_pos)
        player1_pos = 100 - ((player1_pos + roll_num) - 100)
        print("Player 1 bounces back to", player1_pos)
    return (player1_pos, roll_num)
    
def track_player2(player2_pos, d, t, player1_pos):
    """
    This function controls and tracks player 2
    """
    valid_input(2)
    roll_num = die_roll()
    player2_pos = player2_pos + roll_num
    print("Player 2 rolls",roll_num, end="")
    if player2_pos <= 100:
        print(" and moves to box",player2_pos)
    else:
        print(", which makes the next position greater than 100")
        player2_pos = player2_pos - roll_num
        if player1_pos == player2_pos:#accounting for bounceback, if player1 was in same position as player2 before player2 bounces back from 100
            filldraw_rectangle(d[player1_pos][0],d[player1_pos][1],1,1,t,"white")
        filldraw_rectangle(d[player2_pos][0],d[player2_pos][1],1,1,t,"red")
        write_num(d[player2_pos][0],d[player2_pos][1],t,player2_pos)
        player2_pos = 100 - ((player2_pos + roll_num) - 100)
        print("Player 2 bounces back to", player2_pos)
    return (player2_pos, roll_num)
    

def die_roll():
    """
    This function rolls the die
    """
    roll = random.randint(1,6)
    return roll



def setup(x, y, w, h, t):
    """
       This function setups the game board for snakes and ladders.
    """
    filldraw_rectangle(x,y,w,h,t,"red")
    
    for y in range(10):
        if (y % 2) != 0:
            pos = (10*y)+10
        else:
            pos =((10*y)-9)+10            
        for x in range(10):
            filldraw_rectangle(x,y,1,1,t,"red")
            if pos in snake1 or pos in snake2:                
                filldraw_rectangle(x,y,1,1,t,"green")
            if pos in ladder1 or pos in ladder2:                
                filldraw_rectangle(x,y,1,1,t,"yellow")
            write_num(x,y,t,pos)                     
            if (y % 2) != 0:
                pos = pos - 1
            else:
                pos = pos + 1

def the_game(t):
    """
    This function controls the playing of the game, how it starts and when it stops.
    """
    d = create_dictionary()
    stopplay = False
    player1_pos = 0
    player2_pos = 0
    while stopplay == False:
        tuple_pos1_rollnum = track_player1(player1_pos, d, t, player2_pos)
        player1_pos = tuple_pos1_rollnum[0]
        roll_num1 = tuple_pos1_rollnum[1]
        stopplay = winner (player1_pos,"player 1")
        player1_pos = positions1(player1_pos,player2_pos,d,t,roll_num1)
        if stopplay == False:            
            tuple_pos2_rollnum = track_player2(player2_pos, d, t, player1_pos)
            player2_pos = tuple_pos2_rollnum[0]
            roll_num2 = tuple_pos2_rollnum[1]
            stopplay = winner (player2_pos,"player 2")
            player2_pos = positions2(player2_pos,player1_pos,d,t,roll_num2)
        
    print("That's the end of the game.")

def intro_instructions():
    """
    This function prints out the instructions on how the game works
    """
    print("The board will be updated after each move.")
    print("Watch both the board and the python prompt after each move.")
    print("Player 1 is white and player 2 is orange")
    print("Green boxes are snakes and yellow boxes are ladders.")
    print("If you hit any part of the snake(not just the head), you will slide down to the snakes tail")
    print("If you hit any part of the ladder(not just the bottom), you will climb to the ladder's top")
    print("May the luckiest player win")

def create_board_window():
    """
    This function creates a window with a canvas
    """
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, WIDTH+1, HEIGHT+1)
    t = turtle.Turtle()
    t.pensize(1)
    t.speed(0)
    t.hideturtle()
    return (wn, t)

def main():
    intro_instructions()
    
    wn_turtle_tuple = create_board_window()
    wn = wn_turtle_tuple[0]
    t = wn_turtle_tuple[1]
    
    setup(0, 0, WIDTH, HEIGHT, t)
    
    the_game(t)
    
    wn.exitonclick()
   
    
   
if __name__ == '__main__':
    main()

