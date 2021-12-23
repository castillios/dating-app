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

USER_PROF = []


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

    USER_PROF.append(user_profile)

    return 'Profile created'


def del_prof():
    USER_PROF.pop(0)


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


def main_menu():
    title = "PenPal"
    spacer_1 = '@' * 20
    menu = f"\n{spacer_1:^20}\n{title:^20}\n{spacer_1:^20}\n\n{'browse (b)':^20}\n{'matches (m)':^20}\n{'my profile (p)':^20}\n{'create profile (c)':^20}\n{'quit (q)':^20}\n\n{spacer_1}\n"

    return menu


def user_input(msg:str=''):
    user_in = input(msg)
    user_in = user_in.lower()
    return user_in

if __name__ == "__main__":
    # me = create_profile()
    # print(me)
    print(main_menu())
    while True:
        option = user_input('Test: ')
        if option == 'q':
            print()
            print()
            print('Quitting...')
            break

        if option == 'b':
            print('not implemented')
        elif option == 'm':
            print('not implemented')
        elif option == 'p':
            if len(USER_PROF) == 0:
                while True:
                    create_true = user_input('No existing profile. Create new profile? (y/n)\n')
                    if create_true == 'y':
                        user = create_profile()
                        break
                    elif create_true == 'n':
                        break
                    else:
                        print("Invalid input! Type 'y' or 'n'.")
            else:
                display_profile(USER_PROF[0])
        elif option == 'c':
            if len(USER_PROF) >= 1:
                print("A user profile already exists. Create a new one? (y/n)")
                print("WARNING: This will delete the existing profile!")
                test = user_input()
            else:
                new_user = create_profile()

    