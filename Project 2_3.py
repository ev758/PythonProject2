import sys

def output_roster(jersey_number_list, roster_dict):
    print('ROSTER')
    for x in range(0, len(jersey_number_list)):
        for key in roster_dict.keys():
            if (jersey_number_list[x] == key):
                print('Jersey number: ', jersey_number_list[x], ', Rating: ', roster_dict[key], sep="")
                break
    print('\n')

def add_player(roster_dict, jersey_number_list):
    try:
        print("Enter a new player's jersey number:", end="")
        jersey_number = int(input())
        if (jersey_number < 0 or jersey_number > 99):
            print('Jersey number must be 0-99, exiting menu')
            sys.exit()
            
        print("Enter the player's rating:", end="")
        rating = int(input())
        if (rating < 1 or rating > 9):
            print('Rating must be 1-9, exiting menu')
            sys.exit()
    except ValueError:
        print('Incorrect input, exiting menu')
        sys.exit()
    
    print('\n')
    roster_dict[jersey_number] = rating

    for key in roster_dict.keys():
        for x in range(0, len(jersey_number_list)):
            if key not in jersey_number_list:
                jersey_number_list.append(key)
    
    jersey_number_list.sort()

def delete_player(roster_dict):
    try:
        print('Enter a jersey number:', end="")
        jersey_number = int(input())
        if (jersey_number < 0 or jersey_number > 99):
            print('Jersey number must be 0-99, exiting menu')
            sys.exit()
    except ValueError:
        print('Incorrect input, exiting menu')
        sys.exit()
    
    print('\n')
    
    roster_dict.pop(jersey_number)

def update_player_rating(roster_dict):
    try:
        print('Enter a jersey number:', end="")
        jersey_number = int(input())
        if (jersey_number < 0 or jersey_number > 99):
            print('Jersey number must be 0-99, exiting menu')
            sys.exit()
        
        print('Enter a new rating for player:', end="")
        rating = int(input())
        if (rating < 1 or rating > 9):
            print('Rating must be 1-9, exiting menu')
            sys.exit()
    except ValueError:
        print('Incorrect input, exiting menu')
        sys.exit()
    
    print('\n')
    roster_dict[jersey_number] = rating

def output_players_above_a_rating(roster_dict):
    try:
        print("Enter a rating:", end="")
        rating = int(input())
        if (rating < 1 or rating > 9):
            print('Rating must be 1-9, exiting menu')
            sys.exit()
    except ValueError:
        print('Incorrect input, exiting menu')
        sys.exit()
    
    print('\n')
    print('ABOVE', rating)
    for key in roster_dict.keys():
        if (rating < roster_dict[key]):
            print('Jersey number: ', key, ', Rating: ', roster_dict[key], sep="")
    print('\n')

def main():
    roster_dict = {}
    jersey_number_list = []
    isTrue = True
    isTrue2 = True
    option = ''
    
    try:
        for x in range(1, 6):
            print("Enter player ", x, "'s jersey number:", sep="", end="")
            jersey_number = int(input())
            if (jersey_number < 0 or jersey_number > 99):
                print('Jersey number must be 0-99')
                sys.exit()
            
            print("Enter player ", x, "'s rating:", sep="", end="")
            rating = int(input())
            if (rating < 1 or rating > 9):
                print('Rating must be 1-9')
                sys.exit()
            
            print('\n')
            roster_dict[jersey_number] = rating
    except ValueError:
        print('Incorrect input')
        sys.exit()
    
    for key in roster_dict.keys():
        jersey_number_list.append(key)
    
    jersey_number_list.sort()
    
    print('ROSTER')
    for x in range(0, len(jersey_number_list)):
        for key in roster_dict.keys():
            if (jersey_number_list[x] == key):
                print('Jersey number: ', jersey_number_list[x], ', Rating: ', roster_dict[key], sep="")
                break
    print('\n')
    
    while (isTrue):
        print('MENU')
        print('a - Add player')
        print('d - Remove player')
        print('u - Update player rating')
        print('r - Output players above a rating')
        print('o - Output roster')
        print('q - Quit')
        
        option = input('Choose an option: ')
        print('\n')
        
        while (isTrue2):
            if (option == 'a'):
                add_player(roster_dict, jersey_number_list)
                break
            elif (option == 'd'):
                delete_player(roster_dict)
                break
            elif (option == 'u'):
                update_player_rating(roster_dict)
                break
            elif (option == 'r'):
                output_players_above_a_rating(roster_dict)
                break
            elif (option == 'o'):
                output_roster(jersey_number_list, roster_dict)
                break
            elif (option == 'q'):
                print('Exiting menu')
                sys.exit()
            else:
                print('Select an option from the menu')
                option = input()

main()