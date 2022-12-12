import random
# Computer
comp_wins=0

# User or player
player_wins=0

# User Input
def choose():
    user_choice=input(" Choose Rock, Paper,Scissor :  ")
    if user_choice in  ["Rock","rock","R","r"]:
        user_choice="r"
    elif user_choice in  ["Paper","paper","P","p"]:
        user_choice="p"
    elif user_choice in  ["Scissor","scissor","S","s"]:
        user_choice="s"
    else:
        print("Invalid Choice")
        choose()
    return user_choice  
  
# computer choice
def comp_choose():
     comp_choice=random.randint(1,3)
     if comp_choice==1:
         comp_choice="r"
     elif comp_choice==2:
         comp_choice="p"
     else :
         comp_choice="s"
         
     return comp_choice    
         
# game logic         
         
while True:
    print("")     
    user_choice=choose()       
    comp_choice=comp_choose()          
    if user_choice=="r":
        if comp_choose=="r":
            print("You choose Rock 🧱 . Computer choose Rock 🧱. Match Tied.")
        elif comp_choose=="p":
            print("You choose Rock 🧱. Computer choose Paper 📃. computer wins.")
            comp_wins+=1
        else:     
            print("You choose Rock 🧱. Computer choose scissor ✂️. Player wins.")
            player_wins+=1
         
    elif user_choice=="p":
          if comp_choose=="r":
             print("You choose Paper 📃. Computer choose Rock 🧱. Player Wins.")
             player_wins+=1     
          elif comp_choose=="p":
             print("You choose Paper 📃. Computer choose Paper 📃. Match Tied .")
          else:     
             print("You choose Paper 📃. Computer choose scissor ✂️. computer wins.")
             comp_wins+=1
                         
    else:
         if comp_choose=="r":
            print("You choose scissor ✂️. Computer choose Rock 🧱. computer wins..")
            comp_wins+=1 
         elif comp_choose=="p":
            print("You choose scissor ✂️. Computer choose Paper 📃. Player wins.")
            player_wins+=1  
         else:     
            print("You choose scissor ✂️. Computer choose scissor ✂️. Match Tied.")        
    
    print("")         
    print("Player Wins :" +str(player_wins))     
    print("Computer  Wins :" +str(comp_wins))   
    print("")
  
    user_choice=input("Do you wnt to play again?(y/n)")
    if user_choice in ["Yes","yes","y","Y"]:
        pass
    elif user_choice in ["No","no","n","N"]:
        print("Thanks For Playing")
        break
    else:
        print("Thanks For Playing")




