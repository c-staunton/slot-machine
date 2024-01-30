#project idea from Tech with Tim on Youtube - www.youtube.com/watch?v=th4OBktqK1I&t=130s
import random

def balance():
    balance_input = input('How much would you like to add to your balance? $')
    balance = int(balance_input)
    print(f'You balance is ${balance}')
    return balance

def random_slot_letter():
    letters = ["A", "B", "C", "D"]
    display_letters = []
    for num in range(9):
        random_item = random.choice(letters)
        display_letters.append(random_item)
    return display_letters

def slot_machine_interface():
    letter_display = random_slot_letter()
    print(f'{letter_display[0]}|{letter_display[1]}|{letter_display[2]}')
    print(f'{letter_display[3]}|{letter_display[4]}|{letter_display[5]}')
    print(f'{letter_display[6]}|{letter_display[7]}|{letter_display[8]}')
    return letter_display

def all_same_letter(letters):
    all_same = True
    for letter in letters:
        if letter != letters[0]:
            all_same = False
    return all_same

def main():
    play_balance = balance()
    continue_status = True
    bet_win_amount = 0
    while continue_status:
        line_input_check = True
        amount_input_check = True
        play_input = input("Would you like to play(q to quit, enter to continue)")
        if play_input == '':
            while line_input_check:
                bet_number_of_lines = int(input("How many lines would you like to bet on? "))
                if bet_number_of_lines in range(1,4):
                    line_input_check = False
            while amount_input_check:
                bet_amount = int(input("How much would you like to put on these lines? $"))
                if bet_amount < play_balance:
                    amount_input_check = False
            slot_machine = slot_machine_interface()
            line1 = slot_machine[0:3]
            line2 = slot_machine[3:6]
            line3 = slot_machine[6:9]
            if bet_number_of_lines == 1:
                if all_same_letter(line1):
                    bet_win_amount = (bet_amount * 2) - bet_amount
                    play_balance += bet_win_amount
                else:
                    play_balance -= bet_amount
            elif bet_number_of_lines == 2:
                if all_same_letter(line1) == True and all_same_letter(line2) == True:
                    bet_win_amount = (bet_amount * 4) - bet_amount
                    play_balance += bet_win_amount
                elif all_same_letter(line1) == True or all_same_letter(line2) == True:
                    bet_win_amount = (bet_amount * 2) - bet_amount
                    play_balance += bet_win_amount
                else:
                    play_balance -= bet_amount
            elif bet_number_of_lines == 3:
                if all_same_letter(line1) == True and all_same_letter(line2) == True and all_same_letter(line3) == True:
                    bet_win_amount = (bet_amount * 6) - bet_amount
                    play_balance += bet_win_amount
                elif (all_same_letter(line1) == True and all_same_letter(line2) == True) or (all_same_letter(line1) == True and all_same_letter(line3) == True) or (all_same_letter(line2) == True and all_same_letter(line3) == True):
                    bet_win_amount = (bet_amount * 4) - bet_amount
                    play_balance += bet_win_amount
                elif all_same_letter(line1) == True or all_same_letter(line2) == True or all_same_letter(line3) == True:
                    bet_win_amount = (bet_amount * 2) - bet_amount
                    play_balance += bet_win_amount
                else: 
                    play_balance -= bet_amount
            print(f'Your new balance is ${play_balance}')
        elif play_input == 'q':
            print(f'Your exiting balance is ${play_balance}')
            exit()

if __name__ == '__main__':
    main()