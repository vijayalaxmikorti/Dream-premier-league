#A match of DPL is going on. Team Aravali has a made score of 195 for 7 in 20 overs and the opponent Team Shivalik is doing some analytics to find out what they need to do to win. You are the Data Scientist of the Team Shivalik and you have been asked to help them.


#Problem 1
#Team Shivalik has stored the runs made by Team Aravali players in the following dictionary.
aravali ={ "Dhoni":25, "Virat":31, "Pollard":11, "Rohit": 0, "Maxwell":12, "Sachin":59, "Sehwag":12 }
#Get the list of all players in Team Aravali
print(list(aravali.keys()))


#Problem 2
#By mistake, the runs made by Rohit was recorded as 0. Your next task is to figure out how many runs were made by Rohit and update the dictionary
# We know the total runs
total_runs = 195

# Sum of runs made by the players from Team Aravali
runs_according_to_aravali_dict = sum(aravali.values())

# Runs made by Rohit
rohit_runs = total_runs - runs_according_to_aravali_dict

# Print runs scored by Rohit
print(f'The actual runs made by Rohit is {rohit_runs}')

# Update the dictionary with correct value of runs
aravali['Rohit'] = rohit_runs
print(aravali)

#Problem 3
# our next task is to find out who scored the second highest runs in Team Aravali
# Your code below
aravali_copy = aravali.copy()
aravali_copy
max_runs = max(list(aravali_copy.values()))
max_run_index = list(aravali_copy.values()).index(max_runs)
print(max_run_index)
aravali_players = list(aravali_copy.keys())
print(aravali_players)
highest_run_scorer = aravali_players[max_run_index]
aravali_copy.pop(highest_run_scorer)
print(aravali_copy)
max_runs = max(list(aravali_copy.values()))
max_run_index = list(aravali_copy.values()).index(max_runs)
print(max_run_index)
aravali_players = list(aravali_copy.keys())
print(aravali_players)
print(f'The second highest scorer from Team Aravali is {aravali_players[max_run_index]}')

#Problem 4
#Just out of curiosity, you want to find out the unique runs made by Team Aravali players.
run_set = set(list(aravali.values()))
run_set

#Problem 5
#Team Shivalik has 6 fixed players and 5 slots for players who are playing good currently. Create two collections using appropriate data structure to write this 6 fixed and 5 mutable players. You can choose any player you want.
#Available Players in the squad :
#['Vijay', 'Lasith', 'Dravid', 'Smith', 'Ambati', 'Hardik', 'Sushant', 'Mandeep', 'Harbhajan', 'Yuvraj', 'Jadeja','Rajeev','Amrit']
fixed = ('Vijay', 'Lasith', 'Dravid', 'Smith', 'Ambati','Hardik')
mutable = [ 'Sushant', 'Mandeep', 'Harbhajan', 'Yuvraj', 'Jadeja']
print(fixed)
print(mutable)
print(f'{fixed},{mutable}')
print(fixed,mutable,sep=",")
print(fixed,',',mutable)

#Problem 6
#Try changing fixed player and mutable player
# Change fixed player
fixed[0] = 'Risabh' #error object does not support
# Change mutable player
mutable[0] = 'Rajeev'
mutable

#Problem 7
#Find out the runrate required for Team Shivalik to win (for 20 overs)
total_runs = 195
required_runrate = (total_runs+1)/20
print(required_runrate)

#Problem 8                
#You have just received a secret message form your informant stating that some players of the other team are into match fixing. You have to decode a message and inform authorities about it.
#You received a string "skdlfjnvuerhw qefnnaosfu qrhviudhfv wuirhv adknlkxjcier vafuvhkajn iuvhsf vasuif KJSHFKJ aeuihvasf akjfhiufe" and index of "i" are going to be "no balls".
#Find the first and last no ball from the string.

#First no ball
message = "skibhiko"
first_no_ball_number = message.index('i') + 1
print(f'The first no ball will be delivered at the number {first_no_ball_number}')

# Last no ball
reverse_message = message[::-1]

# Find the first occurrence in this reversed message
no_ball_number = reverse_message.index('i') 
print(no_ball_number)

# Print the first and last ball numbers
message_length = len(message)
last_no_ball_number = message_length - no_ball_number
print(f'The last no ball will be delivered at the delivery number {last_no_ball_number}')

#Problem 9
#You have given the information about fixing to the authorities and they are going to verify it during the match. But still you have to work on your strategy.
#It is in your hands to automate the decision on who goes on 4th position for batting depending on following criteria:
#if runs made by Team Shivalik is less than 50, Smith will play
#if runs are between 51 to 100 then Sir Jadeja will go
#if runs are above 100 then Hardik will play

shivalik_runs = int(input())
print(shivalik_runs)
if shivalik_runs > 0 and shivalik_runs < 50 :
  print("Smith will go")
elif shivalik_runs >=50 and shivalik_runs < 100 :
  print("Sir Jadeja will go")
elif shivalik_runs >=100:
  print("Send Hardik to bat")
else:
  print("Invalid runs")
