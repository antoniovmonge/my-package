from termcolor import colored

def whats_my_name():
    
    return 'Hello my name is Toni_2'

def who_am_i():
    
    name = whats_my_name()
    
    # cannot be tested since the function returns None implicitly
    print(colored(name, 'yellow'))
