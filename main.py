from collections import namedtuple
import csv

Profile = namedtuple("Profile", ['name', 'age', 'occupation', 'tagline'])
# keeps track of index when browsing thru profiles; by default is 0
DEFAULT_IN = 0
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
    

# temporarily hardcoded//make a dictionary for facial features
def ascii_face():
    hair = "/\\/\\/\\"
    eyes = 'o    u'
    nose = 'v'
    mouth = '--/'

    face = f"{hair:^20}\n{eyes:^20}\n{nose:^20}\n{mouth:^20}"
    return face

def switch_prof(prof_library:list, idx):
    """Iterates through a list of profiles given user input."""
    if idx == (len(prof_library) - 1):
        idx = DEFAULT_IN
    else:
        idx += 1
    
    display_profile(prof_library[idx])

    return idx


def swipe(user_in, idx):
    idx = switch_prof(PRESETS, cur_in)
    return idx
 


if __name__ == "__main__":
    # me = create_profile()
    # print(me)
    # display_profile(PRESETS[1])
    display_profile(PRESETS[DEFAULT_IN])
    user_in = input('DEBUG: type n to swipe (\'q\' to exit)')
    cur_in = DEFAULT_IN

    while True:
        user_in = user_in.lower()
        if user_in == 'quit':
            print('quitting application...')
            break
        cur_in = swipe(PRESETS, cur_in)

        user_in = input('DEBUG: type n to swipe (quit to exit)')


    