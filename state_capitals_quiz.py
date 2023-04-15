import random

state_capitals = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", 
"Arkansas": "Little Rock", "California": "Sacramento", "Colorado": "Denver",
"Connecticut": "Hartford", "Delaware": "Dover", "Florida": "Tallahassee",
"Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise", "Illinois": "Springfield",
"Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka", "Kentucky": "Frankfort",
"Lousiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis", "Massachusetts": "Boston",
"Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson", "Missouri": "Jefferson City",
"Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord",
"New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany", "North Carolina": "Raleigh",
"North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem",
"Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia",
"South Dakota": "Pierre", "Tennesse": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City",
"Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston",
"Wisconsin": "Madison", "Wyoming": "Chayenne"}

def quiz(dict): 

    print("United States State Capitals Quiz")

    question = input("Do you want to play? Type 'yes' to start or 'no' to exit.\n").lower()

    if question != "yes":
        quit()

    if question == "exit":
        quit()

    print("Great, let's start.")
    print("To exit the game, type 'exit'.")

    score = 0

    items = list(dict.items())
    random.shuffle(items)
    
    for state, capital in state_capitals.items():
        answer = input(f"What's the capital of {state}?\n")
        if answer.lower() == capital.lower():
            print("That's correct.")
            score += 1
        elif answer.lower() == "exit":
            break
        else:
            print("That's incorrect.")
            print(f"The correct answer is {capital}.")

    print(f"You guessed {score} state capitals correct.")

quiz(state_capitals)