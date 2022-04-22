from collections import namedtuple
import csv


Profile = namedtuple("Profile", ['name', 'age', 'occupation', 'tagline'])
# future: implement bio as a dictionary {'likes':[], 'dislikes':[]...}

# keeps track of index when browsing thru profiles; by default is 0
DEFAULT_IN = 0

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


def create_profile() -> bool:
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

    return True


def del_prof():
    USER_PROF.pop(0)


def edit_prof(prof:Profile):
    menu = f"\n{'@' * 20}\n{'EDIT MENU':^20}\n{'Edit name (n)':^20}\n{'Edit age (a)':^20}\n{'Edit occupation (o)'}\n{'Edit tagline (t)':^20}"
    # temp_profile
    # implement edit photo option later on** 
    while True:

        print(menu)
        print('@' * 20)
        print()

        user_in = user_input('Select an option. Type \'q\' to quit: ')
        
        print()
        print('@' * 20)
        print()
        
        if user_in == 'q':
            break
        elif user_in == 'n':
            print(f"{'EDIT NAME':^20}")
            print()
            new_name = input('Enter new name: ')
            print('@' * 20)
            prof = prof._replace(name=new_name)
        elif user_in == 'a':
            print(f"{'EDIT AGE':^20}")
            new_age = int(input('Enter new age: '))
            prof = prof._replace(age=new_age)
        elif user_in == 'o':
            print(f"{'EDIT OCCUPATION':^20}")
            new_occ = input('Enter new occupation: ')
            prof = prof._replace(occupation=new_occ)
        elif user_in == 't':
            print(f"{'EDIT TAGLINE':^20}")
            new_tag = input('Enter new tagline: ')
            prof = prof._replace(tagline=new_tag)
        else:
            print('Invalid option! Try again.')

    return prof



def no_profile():
    user = False
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
    elif len(USER_PROF) == 1:
        user = True
    return user 
        
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


def spacer():
    for i in range(10):
        print()


def switch_prof(prof_library:list, idx):
    """Iterates through a list of profiles given user input."""
    if idx == (len(prof_library) - 1):
        idx = DEFAULT_IN
    else:
        idx += 1
    
    display_profile(prof_library[idx])

    return idx

def swipe(idx):
    swipe_idx = switch_prof(PRESETS, idx)
    return swipe_idx


def main_menu():
    title = "PenPal"
    spacer_1 = '@' * 20
    menu = f"\n{spacer_1:^20}\n{title:^20}\n{spacer_1:^20}\n\n{'browse (b)':^20}\n{'matches (m)':^20}\n{'my profile (p)':^20}\n{'create profile (c)':^20}\n{'quit (q)':^20}\n\n{spacer_1}\n"

    return menu


def prof_menu():
    print(f"options:\n{'edit profile (e)':^20}\n{'return to menu (q)':^20}")


def user_input(msg:str=''):
    user_in = input(msg)
    user_in = user_in.lower()
    return user_in

if __name__ == "__main__":
    option = None
    while True:
        if option == 'q':
            spacer()
            print('Quitting application')
            break

        print(main_menu())
        option = user_input('Test: ')

        if option == 'b':
            check = no_profile()
            if check:
                display_profile(PRESETS[DEFAULT_IN])
                cur_in = DEFAULT_IN

                while True:
                    user_in = user_input('DEBUG: type n to swipe (q to exit)\n')
                    if user_in == 'q':
                        option = 'q'
                        break
                    
                    cur_in = swipe(cur_in)
            else:
                spacer()
                print("No existing profile. Returning to menu...")

        elif option == 'm':
            print('not implemented')

        elif option == 'p':
            check = no_profile()
            if check:
                while True:
                    display_profile(USER_PROF[0])
                    prof_menu()
                    user_in = user_input('Pick a menu option: ')
                    if user_in == 'q':
                        break
                    elif user_in == 'e':
                        edited = edit_prof(USER_PROF[0])
                        USER_PROF[0] = edited
                    else:
                        print('Invalid Input! Try again.\n')
                spacer()
            else:
                print("No existing profile. Returning to menu...")
                
        elif option == 'c':
            if len(USER_PROF) >= 1:
                print("A user profile already exists. Create a new one? (y/n)")
                print("WARNING: This will delete the existing profile!")
                while True:
                    new = user_input()
                    if new == 'y':
                        del_prof()
                        create_profile()
                        print('DEBUG:', USER_PROF)
                        break
                    elif new == 'n':
                        spacer()
                        print('Returning to menu...')
                        break
                    else:
                        print("Invalid input! Type 'y' or 'n'.")
            else:
                create_profile()
