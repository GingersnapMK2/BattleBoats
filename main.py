'''Ryan Hogan
1/29/2021
Task Project "Battleboats"
'''
import random
import time
import copy
#from colorama import Fore, Back, Style   



def wincheck(input_board, refernce_board, playername):
  tick = 0
  boats = 0
  points = 0
  for x in refernce_board:
    boats = boats + refernce_board[tick].count("◼") + refernce_board[tick].count("☒") + refernce_board[tick].count("▣")
    tick = tick + 1
  tick = 0
  for x in input_board:
    points = points + input_board[tick].count("☒") + input_board[tick].count("⨉")
    tick = tick + 1
  if points == boats:
    print(Fore.GREEN + playername + " wins!" + Style.RESET_ALL)
    return True
    

def colorprint(input_board):
  printout = copy.deepcopy(input_board)
  tick = 0
  letters = ["A","B","C","D","E","F","G"]
  numbers = ["1","2","3","4","5","6","7"]
  for x in printout:
    tick2 = 0
    for x in printout:
      if printout[tick][tick2] in letters:
        printout[tick][tick2] = Style.BRIGHT + Fore.BLUE + printout[tick][tick2] + Style.RESET_ALL
      if printout[tick][tick2] in numbers:
        printout[tick][tick2] = Style.BRIGHT + Fore.BLUE + printout[tick][tick2] + Style.RESET_ALL
      if printout[tick][tick2] == ("☒"):
        printout[tick][tick2] = Fore.RED + printout[tick][tick2] + Style.RESET_ALL
      if printout[tick][tick2] == ("▣"):
        printout[tick][tick2] = Style.BRIGHT + Fore.WHITE + printout[tick][tick2]+ Style.RESET_ALL
      if printout[tick][tick2] == ("◼"):
        printout[tick][tick2] = Style.DIM + printout[tick][tick2] + Style.RESET_ALL
      if printout[tick][tick2] == ("⨉"):
        printout[tick][tick2] = Fore.RED + printout[tick][tick2] + Style.RESET_ALL
      if printout[tick][tick2] == ("▢"):
        printout[tick][tick2] = Style.BRIGHT + Fore.WHITE + printout[tick][tick2]+ Style.RESET_ALL
      if printout[tick][tick2] == ("✛"):
        printout[tick][tick2] = Style.DIM + printout[tick][tick2] + Style.RESET_ALL
      tick2 = tick2 + 1
    tick = tick + 1
  tick = 0
  tick = 0
  for x in printout:
    print(*printout[tick], sep=" ")
    tick = tick + 1


def boatpick(player_board, boat_len): 
    #These series of programs set the placement of the boats, this one program handles any typle/size of boats allowing so that I dont have to make like 4 diffent programs(also allows for the picking of different boats to play with, but this prob wouldn't be implemented as something the user can choose)\
    def send_error(error):
      #Gives an error message and tells the code that a error has occored
      if error == False:
        print(
          "\n\nInvalid input, type the cordinates like (B3, E7, a2, c5)\nBoats must only go vertically or horizontally and must\nbe the correct size (number of tiles). Make sure there are no\nother boats in the way(shown as ■). Please try again.\n\n"
        )
        error = True
        return error
    placement = False
    error = False
    while placement == False:
        error = False
        #Selects which boat is being placed down based on the size
        if boat_len == 5:
            boat = "aircraft carrier"
        elif boat_len == 4:
            boat = "battelship"
        elif boat_len == 3:
            boat = "cruiser"
        elif boat_len == 2:
            boat = "patrol"
        #Asking user where they want to place their boat
        print("\n\n")
        colorprint(player_board)
        print("Where do you want to place your " + boat + "?(" +
              str(boat_len) + " slots)")
        boat1 = input("From: ")
        boat2 = input("To: ")
        #Makes inputs upercase
        boat1 = boat1.upper()
        boat2 = boat2.upper()
        #Boat start coordinates (input to useable coordinates) errors if not possible
        if len(boat1) + len(boat2) == 4:
          if boat1[1] in player_board[0]:
              boat1_x = boat1[1]
          else:
              send_error(error)
          boat1_y = 1
          for x in player_board:
              if boat1[0] in player_board[boat1_y]:
                  break
              else:
                  boat1_y = boat1_y + 1
                  if boat1_y > 7:
                      send_error(error)
                      break
          #Boat end coordinates (input to useable coordinates) errors if not possible
          if boat2[1] in player_board[0]:
              boat2_x = boat2[1]
          else:
              send_error(error)
          boat2_y = 1
          for x in player_board:
              if boat2[0] in player_board[boat2_y]:
                  break
              else:
                  boat2_y = boat2_y + 1
                  if boat2_y > 7:
                      send_error(error)
                      break
          #Turns y(s) into intergers (were seen as strings before)
          boat1_x = int(boat1_x)
          boat2_x = int(boat2_x)
          #Makes sure the boat is place corectly (not across axis, and the correct number of spaces)
          boat_var = int(boat_len) - 1
          boat_var_neg = boat_var * -1
          check = 1
          #This is mostly the same code 4 times just set to work in the up/down and left/right directions
          if error == False and (boat1_y <= 7) and (boat1_y >= 1) and (boat2_y <= 7) and (boat2_y >= 1):
            if (player_board[boat1_y][boat1_x] != "◼") and (player_board[boat2_y][boat2_x] != "◼"):
              if (boat1_y == boat2_y) and (boat1_x - boat2_x == boat_var
                                          or boat_var_neg):
                  if boat1_x > boat2_x:
                      axis = boat2_x
                      while boat1_x != axis:
                          #This makes sure no boat is in the way of the placement
                          if player_board[boat1_y][axis] == "◼":
                              send_error(error)
                              break
                          else:
                              check = check + 1
                              axis = axis + 1
                      #If no boat is found and all the spaces are empty then it starts to place down the boat
                      if check == boat_len:
                          axis = boat2_x
                          while axis < boat1_x + 1:
                              #Removes "X" on grid and places a boat ("◼")
                              player_board[boat1_y].pop(axis)
                              player_board[boat1_y].insert([axis][0], "◼")
                              axis = axis + 1
                          placement = True
                          break
                  elif boat1_x < boat2_x:
                      axis = boat1_x
                      while axis != boat2_x:
                          if player_board[boat1_y][axis] == "◼":
                              send_error(error)
                              break
                          else:
                              check = check + 1
                              axis = axis + 1
                      if check == boat_len:
                          axis = boat1_x
                          while axis < boat2_x + 1:
                              player_board[boat1_y].pop(axis)
                              player_board[boat1_y].insert([axis][0], "◼")
                              axis = axis + 1
                          placement = True
                          break
                      else:
                          send_error(error)
                  else:
                      send_error(error)
              elif (boat1_x == boat2_x) and (boat1_y - boat2_y == boat_var
                                            or boat_var_neg):
                  if boat1_y > boat2_y:
                      axis = boat2_y
                      while boat1_y != axis:
                          if player_board[axis][boat1_x] == "◼":
                              send_error(error)
                              break
                          else:
                              check = check + 1
                              axis = axis + 1
                      if check == boat_len:
                          axis = boat2_y
                          while axis < boat1_y + 1:
                              player_board[axis].pop(boat1_x)
                              player_board[axis].insert([boat1_x][0], "◼")
                              axis = axis + 1
                          placement = True
                          break
                  elif boat1_y < boat2_y:
                      axis = boat1_y
                      while boat2_y != axis:
                          if player_board[axis][boat1_x] == "◼":
                              send_error(error)
                              break
                          else:
                              check = check + 1
                              axis = axis + 1
                      if check == boat_len:
                          axis = boat1_y
                          while axis < boat2_y + 1:
                              player_board[axis].pop(boat1_x)
                              player_board[axis].insert([boat1_x][0], "◼")
                              axis = axis + 1
                          placement = True
                          break
                  else:
                      send_error(error)
              else:
                send_error(error)
            else:     
              send_error(error)
        else:
          send_error(error)


def ai_boatpick(ai_board, boat_len):
    #This program is basicly the same as boatpick execpt that the cordinates are randomly generated instead of user inputed.
    placement = False
    while placement == False:
        way = random.randint(0, 1)
        boat_var = boat_len - 1
        boat_var_neg = boat_var * -1
        boat1_x = 0
        boat1_y = 0
        boat2_x = 0
        boat2_y = 0
        check = 1
        if way == 0:
            boat1_x = random.randint(1, 7)
            boat2_x = boat1_x
            while True:
                way2 = random.randint(0, 1)
                boat1_y = random.randint(1, 7)
                if way2 == 0:
                  boat2_y = boat1_y + boat_var
                  if boat2_y > 1 and boat2_y < 7:
                    break
                elif way2 == 1:
                  boat2_y = boat1_y - boat_var
                  if boat2_y > 1 and boat2_y < 7:
                    break
        elif way == 1:
            boat1_y = random.randint(1, 7)
            boat2_y = boat1_y
            while True:
                way2 = random.randint(0, 1)
                boat1_x = random.randint(1, 7)
                if way2 == 0:
                  boat2_x = boat1_x + boat_var
                  if boat2_x > 1 and boat2_x < 7:
                    break
                elif way2 == 1:
                  boat2_x = boat1_x - boat_var
                  if boat2_x > 1 and boat2_x < 7:
                    break
        if (ai_board[boat1_y][boat1_x] != "◼") and (ai_board[boat2_y][boat2_x] != "◼"):
          if (boat1_y == boat2_y):
            if boat1_x > boat2_x :
                  axis = boat2_x
                  while boat1_x != axis:
                      if ai_board[boat1_y][axis] == "◼":
                          break
                      else:
                          check = check + 1
                          axis = axis + 1
                  if check == boat_len:
                      axis = boat2_x
                      while axis < boat1_x + 1:
                          ai_board[boat1_y].pop(axis)
                          ai_board[boat1_y].insert([axis][0], "◼")
                          axis = axis + 1
                      placement = True
                      break
            elif boat1_x < boat2_x :
                  axis = boat1_x
                  while axis != boat2_x:
                      if ai_board[boat1_y][axis] == "◼":
                          break
                      else:
                          check = check + 1
                          axis = axis + 1
                  if check == boat_len:
                      axis = boat1_x
                      while axis < boat2_x + 1:
                          ai_board[boat1_y].pop(axis)
                          ai_board[boat1_y].insert([axis][0], "◼")
                          axis = axis + 1
                      placement = True
                      break
          elif (boat1_x == boat2_x):
              if boat1_y > boat2_y:
                  axis = boat2_y
                  while boat1_y != axis:
                      if ai_board[axis][boat1_x] == "◼":
                          break
                      else:
                          check = check + 1
                          axis = axis + 1
                  if check == boat_len:
                      axis = boat2_y
                      while axis < boat1_y + 1:
                          ai_board[axis].pop(boat1_x)
                          ai_board[axis].insert([boat1_x][0], "◼")
                          axis = axis + 1
                      placement = True
                      break
              elif boat1_y < boat2_y:
                  axis = boat1_y
                  while boat2_y != axis:
                      if ai_board[axis][boat1_x] == "◼":
                          break
                      else:
                          check = check + 1
                          axis = axis + 1
                  if check == boat_len:
                      axis = boat1_y
                      while axis < boat2_y + 1:
                          ai_board[axis].pop(boat1_x)
                          ai_board[axis].insert([boat1_x][0], "◼")
                          axis = axis + 1
                      placement = True
                      break


def hitormiss(ai_board, player_board):
  landed = False
  while landed != True:
    print("\n\n")
    colorprint(player_board)
    print("Where do you want to shoot?")
    shot = input("Shoot at: ")
    shot = shot.upper()
    try:
      if shot[1] in player_board[0]:
          shot_x = shot[1]
      else: 
          print("\n\nInvalid input, type the cordinate like (B3, E7, a2, c5)\n\n")
      shot_y = 1
      for x in player_board:
        if shot[0] in player_board[shot_y]:
          break
        else:
          shot_y = shot_y + 1
          if shot_y > 7:
            print("\n\nInvalid input, type the cordinate like (B3, E7, a2, c5)\n\n")
            break
      hitop =  ["◼","☒","▣"]
      missop = ["✛","⨉","▢"]
      listop = ["☒" ,"▣" ,"⨉" ,"▢"]
      shot_x = int(shot_x)
      if ai_board[shot_y][shot_x] in hitop:
        if player_board[shot_y][shot_x] == "◼":
          player_board[shot_y].pop(shot_x)
          player_board[shot_y].insert([shot_x][0], "☒")
          print("\nYOU HIT!\n")
          landed = False
          break
        elif player_board[shot_y][shot_x] == "✛":
          player_board[shot_y].pop(shot_x)
          player_board[shot_y].insert([shot_x][0], "⨉")
          print("\nYOU HIT!\n")
          landed = False
          break
        elif player_board[shot_y][shot_x] in listop:
          print("You already shot here before, try again!")
      elif ai_board[shot_y][shot_x] in missop:
        if player_board[shot_y][shot_x] == "◼":
          player_board[shot_y].pop(shot_x)
          player_board[shot_y].insert([shot_x][0], "▣")  
          print("\nYOU MISSED!\n")
          landed = False
          break
        elif player_board[shot_y][shot_x] == "✛":
          player_board[shot_y].pop(shot_x)
          player_board[shot_y].insert([shot_x][0], "▢")
          print("\nYOU MISSED!\n")
          landed = False
          break
        elif player_board[shot_y][shot_x] in listop:
          print("You already shot here before, try again!")
      else:
        print("\n\nInvalid input, type the cordinate like (B3, E7, a2, c5)\n\n")
    except:
      print("\n\nInvalid input, type the cordinate like (B3, E7, a2, c5)\n\n")


def ai_hitormiss(ai_board, player_board, ai_chache):
  move = 0
  hitormiss = 0
  ontarget = 1
  direction = 2
  lastshot = 3
  nextmove = 4
  landed = False
  hitop =  ["◼","☒","▣"]
  missop = ["✛","⨉","▢"]
  while landed == False:
    roll = random.randint(1,3)
    shot_x = random.randint(1, 7)
    shot_y = random.randint(1, 7)
    if roll == 1:
      hit = False
      while hit == False:
        shot_x = random.randint(1, 7)
        shot_y = random.randint(1, 7)
        if player_board[shot_y][shot_x] in hitop:
          break
    if player_board[shot_y][shot_x] in hitop:
      if ai_board[shot_y][shot_x] == "◼":
          ai_board[shot_y].pop(shot_x)
          ai_board[shot_y].insert([shot_x][0], "☒")
          print("\nAI HIT!\n")
          ai_chache[hitormiss].append(True)
          ai_chache[ontarget] = True
          ai_chache[lastshot].append(shot_x)
          ai_chache[lastshot].append(shot_y)
          landed = False
          break
      elif ai_board[shot_y][shot_x] == "✛":
          ai_board[shot_y].pop(shot_x)
          ai_board[shot_y].insert([shot_x][0], "⨉")
          print("\nAI HIT!\n")
          ai_chache[hitormiss].append(True)
          ai_chache[ontarget] = True
          ai_chache[lastshot].append(shot_x)
          ai_chache[lastshot].append(shot_y)
          landed = False
          break
    elif player_board[shot_y][shot_x] in missop:
        if ai_board[shot_y][shot_x] == "◼":
          ai_board[shot_y].pop(shot_x)
          ai_board[shot_y].insert([shot_x][0], "▣")  
          print("\nAI MISSED!\n")
          ai_chache[hitormiss].append(False)
          ai_chache[lastshot].append(shot_x)
          ai_chache[lastshot].append(shot_y)
          landed = False
          break
        elif ai_board[shot_y][shot_x] == "✛":
          ai_board[shot_y].pop(shot_x)
          ai_board[shot_y].insert([shot_x][0], "▢")
          print("\nAI MISSED!\n")
          ai_chache[hitormiss].append(False)
          ai_chache[lastshot].append(shot_x)
          ai_chache[lastshot].append(shot_y)
          landed = False
          break


def tutorial(layout):
    #The tutorial
    player_board = copy.deepcopy(layout)
    ai_board = copy.deepcopy(layout)
    print("\n\n")
    print("Ok lets start with the basics:")
    print(
        "To start you must place down your ships.\nIn this program you set your placement by\nputting down the cordinates like this:"
    )
    print("B4, E1, g3, d6, ect.\n")
    print("Lets see an example of placing a ship down:\n")
    boat_len = 5
    ai_boatpick(ai_board, boat_len)
    boatpick(player_board, boat_len)
    print("\n\nGood job! You just placed a boat down,\nguessing where your opponent ship is works the same way\nexecpt you only have to put down one cordinate.\nYou cannot see the opponent ships are.\nEach guess tells you if it hit or missed, if will also\nmark it down on your board.\nTry it out:\n")
    hitormiss(ai_board, player_board)
    print("\nHeres what your board looks like after the guess:\n")
    colorprint(player_board)
    print("\nPlaying the game is as simple as just putting\nthe cordinates down!")
    input("\nHit enter to go to the title screen:")
    print("\n\n")


def gameconfig(layout):
  #Here you can easily customize the player vs ai settings
  ai_chache = [[False],False,"",[0,0],[0,0]]
  player_board = copy.deepcopy(layout)
  ai_board = copy.deepcopy(layout)
  boat_len = 4
  boatpick(player_board, boat_len)
  ai_boatpick(ai_board, boat_len)
  boat_len = 3
  boatpick(player_board, boat_len)
  ai_boatpick(ai_board, boat_len)
  boat_len = 2
  boatpick(player_board, boat_len)
  ai_boatpick(ai_board, boat_len)
  boat_len = 2
  boatpick(player_board, boat_len)
  ai_boatpick(ai_board, boat_len)
  win = False
  while True:
    hitormiss(ai_board, player_board)
    win = wincheck(player_board, ai_board, "PLAYER")
    if win == True:
      break
    ai_hitormiss(ai_board, player_board, ai_chache)
    win = wincheck(ai_board, player_board, "AI")
    if win == True:
      break


def gameconfig2(layout):
  ai_chache = [[False],False,"",[0,0],[0,0]]
  ai_chache2 = [[False],False,"",[0,0],[0,0]]
  ai_board = copy.deepcopy(layout)
  ai_board2 = copy.deepcopy(layout)
  boat_len = 4
  ai_boatpick(ai_board, boat_len)
  ai_boatpick(ai_board2, boat_len)
  boat_len = 3
  ai_boatpick(ai_board, boat_len)
  ai_boatpick(ai_board2, boat_len)
  boat_len = 2
  ai_boatpick(ai_board, boat_len)
  ai_boatpick(ai_board2, boat_len)
  boat_len = 2
  ai_boatpick(ai_board, boat_len)
  ai_boatpick(ai_board2, boat_len)
  while True:
    ai_hitormiss(ai_board, ai_board2,ai_chache)
    print("AI-1 Board:")
    colorprint(ai_board)
    win = wincheck(ai_board, ai_board2, "AI-1")
    time.sleep(.7)
    if win == True:
      time.sleep(2)
      break
    ai_hitormiss(ai_board2, ai_board, ai_chache2)
    print("AI-2 Board:")
    colorprint(ai_board2)
    win = wincheck(ai_board2, ai_board, "AI-2")
    time.sleep(.7)
    if win == True:
      time.sleep(1)
      break




print("Welcome to Battleboats!")
print("-----------------------")
while True:
    #Main program
    layout = [
        [" ", "1", "2", "3", "4", "5", "6", "7"],
        ["A", "✛", "✛", "✛", "✛", "✛", "✛", "✛"],
        ["B", "✛", "✛", "✛", "✛", "✛", "✛", "✛"],
        ["C", "✛", "✛", "✛", "✛", "✛", "✛", "✛"],
        ["D", "✛", "✛", "✛", "✛", "✛", "✛", "✛"],
        ["E", "✛", "✛", "✛", "✛", "✛", "✛", "✛"],
        ["F", "✛", "✛", "✛", "✛", "✛", "✛", "✛"],
        ["G", "✛", "✛", "✛", "✛", "✛", "✛", "✛"],
    ]

    ai_chache = [[False],False,"",[0,0]]
    options = input("\n\n(Pick a number)\nWhat would you like to do:\n1.Tutorial:\n2.Player vs AI:\n3.AI vs AI:\n\n")
    print("\n\n")
    if options == "1":
      tutorial(layout)
    elif options == "2":     
      gameconfig(layout)
    elif options == "3":
      gameconfig2(layout)
    else:
        print("Type the number of the opion you choose") 