from collections import namedtuple
import csv

Profile = namedtuple("Profile", ['name', 'age', 'occupation', 'tagline'])
# future: implement bio as a dictionary {'likes':[], 'dislikes':[]...}

"""
PRESETS
---
randomly generated profiles AKA chatbots
***placeholder, will add randomly generated profiles later***

- idea for randomly generated taglines: either generate a statement or an action phrase (I love long walks vs. Looking for adventure)

"""

PRESETS = [
    Profile('Lucas', 22, 'Student', 'I love long walks!'),
    Profile('Maribel', 20, 'Barista', 'Looking for adventure!')
]

MATCHES = []

user_profile = None

def create_profile() -> Profile:
    user_name = input('Enter your name:\n')

    while True:
        try:
            user_age = int(input('Enter your age (18+):\n'))
            if user_age >= 18:
                break
        except:
            print('\nError! Enter an integer.\n')

    user_occupation = input('Enter your occupation:\n')
    user_tagline = input('Write a sentence that makes you, you! Enter a tagline:\n')

    user_profile = Profile(user_name, user_age, user_occupation, user_tagline)

    return user_profile

# 'graphical' user interface
def display_profile(prof:Profile):
    x = 'PROFILE'
    face = ascii_face()

    print(f"\n{x:@^20}")
 
    print(f"\n\n{face}\n\n")

    
    print(prof.name)
    print(f"{prof.age} * {prof.occupation}")
    print('-' * 20)
    print(f"\"{prof.tagline}\"")
    print('-' * 20)
    print('@' * 20)
    print()
    

# temporarily hardcoded
def ascii_face():
    hair = "/\\/\\/\\"
    eyes = 'o    u'
    nose = 'v'
    mouth = '--/'

    face = f"{hair:^20}\n{eyes:^20}\n{nose:^20}\n{mouth:^20}"
    return face

if __name__ == "__main__":
    # me = create_profile()
    # print(me)
    display_profile(PRESETS[1])
    