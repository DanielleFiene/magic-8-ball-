# Importing the random module
import random

# Name variable with the name of the person asking a question
name = 'Daantje'
# Question to ask
question = 'Is Floki the best dog ever?'
# Answer from magic 8-ball
answer = ''
# Variable that generates a random number between 1 and 10 with a function call
random_number = random.randint(1, 10)

# Elif statement
if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
elif random_number == 10:
  answer = 'Stay where you are'
else:
  answer = 'Error'

# Checking if name is empty
if name == '':
  print('Please give Magic 8-ball a name to tell you your fortune')
elif question == '':
  # Checking if question is empty
  print('The Magic 8-Ball cannot provide a fortune unless you ask it something.')
else:
  # Both name and question are provided
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer:", answer)
