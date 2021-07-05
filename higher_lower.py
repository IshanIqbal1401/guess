from data  import data
from logo_higher_lower import logo, vs
import random
def data_generator():
     return random.choice(data)
def format(account):
    name=account['name']
    follower=account['follower_count']
    bio=account['description']
    country=account['country']
    return f'{name}  has {follower} million followers, HE/SHE is {bio} from {country}'

def check_answer(compare_a,compare_b,user_guess):
     if compare_a['follower_count']>compare_b['follower_count']:
          if user_guess=='a':
               return True
          else:
               return False
     if compare_b['follower_count']>compare_a['follower_count']:
          if user_guess=='b':
               return True
          else:
               return False
def play():     
     print(logo)
     score=0
     game_continue=True
     compare_a=data_generator()
     compare_b=data_generator()
     while game_continue:
          compare_a=compare_b
          compare_b=data_generator()
          if compare_a==compare_b:
               compare_b=data_generator()
          print('compare A: '+format(compare_a))
          print(vs)
          print('compare B: '+ format(compare_b))
          user_guess=input('Which of them has a higher follower count? A or B : ').lower()
          answer=check_answer(compare_a,compare_b,user_guess)
          print(f' The answer is {answer} Score becomes {score}')
          if answer==True:
               score+=1
          else:
               game_continue = False
               print(f"Sorry, that's wrong. Final score: {score}")
         
def user():
     play()
     user_msg=input('Do u Want to play again? : ')
     if user_msg=='yes':
          play()
     else:
          print('Do play Again!')
user()

            






     



    

        
