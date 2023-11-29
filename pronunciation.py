# import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")

# while 1:
#     print("Enter the word you want to speak it out by computer")
#     s = input()
#     speaker.speak(s)

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Set the initial rate (you can adjust this value)
initial_rate = 0
speaker.Rate = initial_rate

while True:
    print("Enter the word you want to speak it out by the computer:")
    s = input()

    # Increase the rate by a certain amount (you can adjust this value)
    speaker.Rate = initial_rate + 2

    # Speak the input
    speaker.speak(s)

    # Reset the rate to the initial value
    speaker.Rate = initial_rate
