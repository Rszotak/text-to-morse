# The purpose of this program is to take in user generated text
# and convert it into morse code. As an extension, add in a
# way to convert the morse code into sound locally

from morse_dict import morse_dict

user_input = input("Please provide a statement to conver:\n")

period_split = user_input.split('.')
