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
