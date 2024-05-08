import time

import random
import sys
import os

def clear():
   os.system('clear')


clear()

#The numbers and the code in the print statement add some colour to the program
print ("\033[1;36;38m                    Welcome to TIC TAC TOE                \033[0m \n")


#Choosing the mode
mode = (input("\033[1;37;38m Please enter a mode. \n 1. Start     \n 2. Instructions \n 3. Quit \033[0m \n"))

#Input check
while mode.isalpha()==True:
  mode= (input("Mode chosen is invalid, please try again: "))

mode = int(mode)


#Printing the mode chosen 
if mode ==1:
  print ("Mode chosen: Play\n")

elif mode ==2:
  clear()
  print ("\nMode chosen: \033[1;37;38mInstructions\033[0m")

#Quit option
def quit():
  if mode == 3:
    print ("Mode chosen: Quit \n\nThank you for using my program!")

    #End credits
    print ("\n\033[1;31;38m                           Credits          \033[0m")
    print ("\nProgrammer : Priyesh Patel \n\nRestart function provided by Gribouillis on https://www.daniweb.com/programming/software-development/code/260268/restart-your-python-program\n")
    
    exit ()


#Input check
if mode<=0 or mode>3:
  while True:
    mode= (input("Mode chosen is invalid, please try again: "))
    mode = int(mode)
    if mode>0 and mode<=3:
      break

quit()


#Restart program function
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


#Play again
#Input check

def play_again():
  print ("\nWould you like to return to the main menu?")
  print ("1. YES")
  print ("2. NO")
  option= (input("\033[1;37;38mInput the number of the option : \033[0m"))
  
  while option.isalpha()==True:
    option= (input("Option chosen is invalid, please try again: "))
    
  option = int(option)
  
  while option>2 or option<1 :
    option= (input("Option chosen is invalid, please try again: "))
    option= int(option)
    
  option = str(option)
  if option =="2":
    print("\n\nThanks for playing!")
    exit()
    
  else:
    restart_program()


#Number of players selection
def player():
    global player
    global difficulty
    
    player = (input("\n\n\033[1;37;38m PLAYERS:\033[0m \n 1. 1 Player     \n 2. 2 Player \n"))
    
    while player.isalpha()==True:
      player= (input("\nOption entered is invalid, try again: "))
      
    player = int(player)
    
    while player>2 or player<1 :
      player= (input("\nOption entered is invalid, try again: "))
      player=  int(player)
    
    player = int(player)
    
    if player ==1:
      AI_difficulty()
    
    else: 
      selection_symbol()
      

#Choosing AI difficulty if singleplayer is chosen

def AI_difficulty():
  global difficulty
  

  print ("\n\033[1;37;38m AI DIFFICULTY SELECTION\033[0m")
  print ("\n\033[1;37;38m 1. Easy\n 2. Hard\033[0m ")
  difficulty = input ("Input a number for the AI difficulty: ")
  
  while difficulty.isalpha()==True:
    difficulty= (input("\nOption entered is invalid, try again: "))
  
  difficulty= int(difficulty)
  
  while difficulty>4 or difficulty<1 :
      difficulty= (input("\nOption entered is invalid, try again: "))
      difficulty= int(difficulty)
      
  difficulty= int(difficulty)
  selection_symbol()

#Printing board  
def print_List1(): 
    print (*multiList1[0])
    print (*multiList1[1])
    print (*multiList1[2])


#Checking row and column on the board based on user input
def row_col():
  global user
  global pos
  global row
  global col
  global yes
  
  user= str(user)
  
  yes = 0
  
  #Checking if input is present in the first list (first row)
  for x in num_List:
    if user == num_List[pos]:
      row= 0
      col = pos
      yes = 1
        
    else:
      pos+=1
  
  #Checking if input is present in the second list (second row)
  if yes !=1 :   
    pos=0
    for x in num_List1:
      if user == num_List1[pos]:
        row= 1
        col = pos
        yes = 1
          
      else:
        pos+=1
  
  #Checking if input is present in the theid list (third row)
  if yes != 1:
    pos=0
    for x in num_List2:
      if user == num_List2[pos]:
        row= 2
        col = pos
        yes= 1
          
      else:
        pos+=1


#If player has won, the function check which player won based on who's turn it was before the game ended

def win_check_player():
  if turn==0:
      print ("\n\033[1;37;38mPlayer\033[0m \033[1;36;38m1\033[0m\033[1;37;38m wins!!!\033[0m ")
      
  
  if turn==1: 
    print ("\n\033[1;37;38mPlayer\033[0m \033[1;31;38m2\033[0m\033[1;37;38m wins!!!\033[0m ")
 

#Checks to see if any of the players have won, 8 different possible ways to win

def win_check():
  global numbers
  
  if (multiList1[0][0]==multiList1[0][1]==multiList1[0][2]) or (multiList1[0][0]==multiList1[1][0]==multiList1[2][0]) or (multiList1[0][2]==multiList1[1][2]==multiList1[2][2]) or (multiList1[2][0]==multiList1[2][1]==multiList1[2][2]) or (multiList1[0][0]==multiList1[1][1]==multiList1[2][2]) or(multiList1[2][0]==multiList1[1][1]==multiList1[0][2]) or  (multiList1[1][0]==multiList1[1][1]==multiList1[1][2]) or(multiList1[0][1]==multiList1[1][1]==multiList1[2][1]) :
    
    clear()
    print_List1()
    win_check_player()
    play_again()
    
    
  #If list of numbers is empty, it is a tie   
  if len(numbers)==0:
    clear()
    print_List1
    print ("\n\033[1;37;38mIt's a TIE\033[0m")
      
    play_again()
    
    
multiList1 = [["  1", "  2", "  3 "],
              ["  4", "  5", "  6 "],

              ["  7", "  8", "  9"],

]


emoji_list1= ["  😀", "  🐼","  🍪", "  🍎", "  🍫", "  🤪", "  ❤️"]


#Symbol selection
#Input checking
def selection_symbol ():
  select_num= input("\n\n1. Traditional(X and O)\n2. Emoji\n")
  
  while select_num.isalpha()==True:
    select_num = input("\nPosition entered is invalid, try again: ")
    
  select_num= int(select_num)
  
  while select_num>2 or select_num<1 :
      select_num= (input("\nPosition entered is invalid, try again: "))
      select_num= int(select_num)
  
  
  if select_num==1:
    print ("Selected option: Traditional")
    traditional()
  
  elif player == 1:
    print ("Selected Option: Emoji")
    customize1()
    
  elif player==2:
    print ("Selected Option: Emoji")
    customize2()


#Assigns symbols to both players
def traditional():
  global player1_symbol
  global player2_symbol
  
  player1_symbol = "\033[1;36;38m  x\033[0m "
  
  print ("\nPlayer 1:",player1_symbol)
  
  player2_symbol = "\033[1;31;38m  O\033[0m"
  
  print ("Player 2:",player2_symbol)
  

#If singleplayer and emoji symbol is chosen player 1 gets to choose an emoji
#Input checking

def customize1():
  global player1_symbol
  global player2_symbol
  
  number_selection = ("  1", "  2", " 3", "  4", "  5", "  6", "  7")
  print (*number_selection)
  print(*emoji_list1)
  
  select = input("Player 1, please input a selection for your symbol  ")
  
  while select.isalpha()==True:
    select = input("\nPosition entered is invalid, try again: ")

  select= int(select)
  
  while select>7 or select<1 :
      select= (input("\nPosition entered is invalid, try again: "))
      select= int(select)

  
  select= int(select)
  select-=1
  player1_symbol = emoji_list1[select]
  
  emoji_list1.remove (emoji_list1[select])
  
  print ("Player 1:",player1_symbol)
  
  player2_symbol = "\033[1;31;38m  O\033[0m"
  
  print ("Player 2:",player2_symbol)
  
 
  
#Emoji selection if multiplayer (2 players) is selected
#Input checking

def customize2():
  global player1_symbol
  global player2_symbol
  
  number_selection = ("  1", "  2", "  3", "  4", "  5", "  6", "  7")
  
  print ("\n",*number_selection)
  print (*emoji_list1)
  
  select = input("Player 1, please input a selection for your symbol: ")
  
  while select.isalpha()==True:
    select = input("\nPosition entered is invalid, try again: ")

  select = int(select)
  
  while select>7 or select<1 :
      select= (input("\nPosition entered is invalid, try again: "))
      select= int(select)
  
  select= int(select)
  select-=1
  player1_symbol = emoji_list1[select]
  
  emoji_list1.remove (emoji_list1[select])
  
  print ("\n",*emoji_list1)
  
  select = input("Player 2, please input a selection for your symbol: ")
  
  while select.isalpha()==True:
    select = input("\nPosition entered is invalid, try again: ")
  
  select= int(select)
  
  while select>6 or select<1 :
      select= (input("\nPosition entered is invalid, try again: "))
      select= int(select)

  select= int(select)
  select-=1
  player2_symbol = emoji_list1[select]
  

#If easy AI mode is chosen
def AI_easy():
  global turn
  global user
  
  #Program picks random number from the list of availalble numbers (list name; numbers) and assigns it 
  
  if turn ==1:
    time.sleep(1)
    user= random.choice(numbers)


#Program randomly picks which player starts the game  
player_turn = ["\033[1;36;38m1\033[0m ", "\033[1;31;38m2\033[0m"]

start = random.choice([0,1])

player_turn_txt= ("\nPlayer "+player_turn [start]+" turn")



num_List0 = ["1", "2", "3"]
num_List1 = ["4", "5", "6"]
num_List2 = ["7", "8", "9"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


numbers2 = ["1", "2", "3"]
numbers3= ["4", "5", "6"]
numbers4 = ["7", "8", "9"]


numbers5  = ["1", "4", "7"]
numbers6 = ["2", "5", "8"]
numbers7  = ["3", "6", "9"]

numbers8 = ["1", "5", "9"]
numbers9= ["3", "5", "7"]


#Adds user selection to the lists so that the computer opponent can choose a position to pick (if playing singleplayer)

def user_in_list():
  global user
  global num1
  global num
  global numbers
  global numbers2
  global numbers3
  global numbers4
  global numbers5
  global numbers6
  global numbers7
  
  #Checks if the number inputed is present in the lists
  for num in range (len(numbers5)):
      if numbers5[num] == user:
        numbers5[num] = num1
          
  if user in numbers6:
    for num in range (len(numbers6)):
      if numbers6[num] == user:
        numbers6[num] = num1
        
  if user in numbers7:
    for num in range (len(numbers7)):
      if numbers7[num] == user:
          numbers7[num] = num1
          
  if user in numbers8:
    for num in range (len(numbers8)):
      if numbers8[num] == user:
        numbers8[num] = num1
          
  if user in numbers9:
    for num in range (len(numbers9)):
      if numbers9[num] == user:
        numbers9[num] = num1
          
  if user in numbers2:
    user = int(user)
    numbers2 [user-1] = num1
      
  elif user in numbers3:
    user = int(user)
    numbers3 [user-4] = num1
      
  elif user in numbers4:
    user = int(user)
    numbers4 [user-7] = num1

  
      
#Computer checking for next move
#Useful for blocking opponents move
#Also useful for helping itself win due to the fact that the program does not check which symbol is in which position, but instead checks what spaces are occupied by any symbol
def medium_row():
  global position
  global user
  global bye
  global yes
  global ok
  
  ok =0
  position = 0
  
  #All different number lists

  if yes == 0:
    bye = numbers2
  elif yes ==1:
    bye = numbers3
  elif yes==2:
    bye = numbers4
  elif yes==3:
    bye = numbers5
  elif yes==4:
    bye = numbers6
  elif yes==5:
    bye = numbers7
  elif yes == 6:
    bye = numbers8
  elif yes == 7:
    bye = numbers9
  
  #If computer goes first, for strategic reasons, it will go to the bottom right corner  
  if turns == 0:
    if multiList1[2][2].isalpha==False:
      user= 9
      time.sleep(2.5)
      user= str(user)
      ok+=1
      
  #If the computer goes second, for strategic reasons, it will go to the middle 
  if turns == 1:
    if multiList1[1][1].isalpha==False:
      user= 5
      time.sleep(2.5)
      user= str(user)
      ok+=1
      
  #Checks if user is about to win and tries to block it
  for j in range (len(bye)-1):
    #If the first 2 positions beside each other are equal to each other (ex. 4 and 5), the computer will place the move in the empty third spot
    if bye[position]== bye[position+1] and ok==0:
      if position ==0:
        if (bye[position+2].isalpha ())== False:
          user= bye[position+2]
          time.sleep (1.5)
          user= str(user)
          ok+=1
          break
        
        else:
          position+=1
          
      
      #The if statement is if the last 2 positions of a row are equal to each other (ex. 5 and 6) 
      
      position +=1
      if position == 2:
        position = 0
        #Reverses the list
        bye = list(reversed(bye))
        
        #Uses same code as if the first 2 positions 
        
        #The last 2 positions of the row are now the first 2 positions
    
        #Checks if the position is not already taken(isalpha is used because the computer symbol is represented as an "o")
        if (bye[position+2].isalpha ())== False:
          user= bye[position+2]
          time.sleep (1.5)
          user= str(user)
          ok+=1
          break
    
        else:
          position+=1
    
         
    position = 0
    #Checks if the first and third position of a row are the same (ex.1 and 3). If yes, the computer will put it's move between the two. 
    if bye[position]== bye[position+2]:
      if (bye[position+1].isalpha ())== False:
        user= bye[position+1]
        time.sleep (1.5)
        user= str(user)
        ok+=1
        break
        
    else:
      position+=1

 
#Function is called if the user has picked the mode "Hard"   

def medium_AI():
  global position
  global user
  global bye
  global yes
  global ok

  position = 0
  
  yes= 0
  medium_row()
  
  #Adds a yes (goes to next list) if the medium_row function comes out if an ok==0
  for num in range(100):
    if ok == 0 and yes<7:
      yes+=1
      medium_row()
  
  #If after all the checks of the list, the computer see's no strategic moves, it will ramdomly select a position
  if ok==0:
    AI_easy()
  
  
num1= " "  
num2 = " "
count= 0
pos = 0
turn = start
turn_count = 1
turns=0


#MODE PLAY
#Prints player turn
#Calls in other functions presented above
#Takes in user input
#Input checking
if mode == 1:
  player()
  clear()  
  
  print ("\nPlayer 1:",player1_symbol)
  print ("Player 2:",player2_symbol)
  print (" ")
  
  print_List1()


  for num in range(1000):
    count+=1
    
    num_List = ["1", "2", "3"]
    
    if count>1:
      player_turn_txt= ("\nPlayer "+player_turn [turn]+" turn")
      
    #Print which player's turn it is
    print (player_turn_txt)
    
    
    #If singleplayer is chosen and the turn is = 0, it is player 1 turn
    #Input check
    if player==1 and turn==0:
      user = (input("\nPlease enter number: "))
      
      while user.isalpha()==True:
        user = input("\nNumber entered is invalid, try again: ")
    
      user= int(user)
    
    #If multiplayer is chosen, players take turns choosing positions  
    elif player == 2:
      user = (input("\nPlease enter number: "))
      
      while user.isalpha()==True:
        user = input("\nNumber entered is invalid, try again: ")
      
      user = int(user)
    
    #If singleplayer is chosen and turn = 1, it is the computers turn to make a move  
    elif player == 1 and turn==1:
      print("Please wait...")
      #Checks if hard difficulty was selected
      if difficulty == 2:
        medium_AI()
      
      else:
        AI_easy()

    col = 0
    user = str(user)
  
    user= int(user)
    
    #Input check
    while user>9 or user<1 :
      user= (input("\nPosition entered is invalid, try again: "))
      user= int(user)
        
    user= int(user)
      
    pos = 0
    user = str (user)
    
    #Function to check what row and column of the multilist the inputed position is in
    row_col()
    
    row = int(row)
    col= int(col)
    
    #Input check
    while user not in numbers:
        user= int(input("\nPosition entered is occupied, try again: "))
        pos = 0
        row_col()
      

    #Switching the number for the emoji based on the player turn
    row = int(row)
    
    if user in numbers:
      numbers.remove (user)
  
    if turn == 0:
      num = player1_symbol
      num1 = "X"
      
    else:
      num = player2_symbol
      num1 = "O"
    
    position = multiList1[row][col]
    multiList1[row][col]=num
    
    #Function to check which lists the number is in
    user_in_list()
    
    clear()
    
    print ("\nPlayer 1:",player1_symbol)
    print ("Player 2:",player2_symbol)
    print (" ")
      
    print_List1()
      
    #Function to check the board to see if anyone has won
    win_check()
    
    #Changes the turn to the next player
    if turn==1:
      turn-=1
      turn_count+=1
    
    elif turn==0:
      turn +=1
      turn_count+=1
      
    turns+=1
    

#Instructions
if mode==2:
  print ("\n\n\n1. The game is played on a grid that's 3 squares by 3 squares. \n\n2. You are X (or your chosen emoji), your friend (or the computer) is O (or the emoji chosen). Players take turns putting their marks in empty spots.\n\n3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n")
  
  play_again()