from game_data import data
from art import logo, vs
from random import choice
from os import system

should_end = False
score = 0
a_dict = choice(data)
b_dict = choice(data)

def a_vs_b(a_data, b_data):
  print(f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}.")
  print(vs)
  print(f"Against B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}.")

def compare(a_data, b_data):
  if a_data["follower_count"] > b_data["follower_count"]:
    return "a"
  else:
    return "b"

def total_score(score):
  print(logo)
  print(f"Sorry, that's wrong, final score: {score}.")

while not should_end:
  print(logo)

  if score > 0:
    print(f"You're right! Current score: {score}.")

  if a_dict == b_dict:
    a_dict = choice(data)
    b_dict = choice(data)

  a_vs_b(a_dict, b_dict)
  make_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  if make_choice == (compare(a_dict, b_dict)):
    score += 1
  else:
    should_end = True
  system("clear")  

  a_dict = b_dict
  b_dict = choice(data)
  
total_score(score)  
