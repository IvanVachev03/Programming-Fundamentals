from tkinter import *
import random

root = Tk()
root.title('Rock–Paper–Scissors')
root.geometry('500x400')

options = ['Rock', 'Paper', 'Scissors']

your_points = 0
computer_points = 0

final_result = f"Result:  You - {your_points},         Computer - {computer_points}"

def choice(player_choice, your_points, computer_points):
    global button_rock
    global button_paper
    global button_scissors
    global final_result

    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        result_1 = "Draw"
        result_2 = f"Your choice is {player_choice}"
        result_3 = f"Computer choice is {computer_choice}"

    elif (player_choice == 'Rock' and computer_choice == 'Scissors') \
            or  (player_choice == 'Paper' and computer_choice == 'Rock') or\
            (player_choice == 'Scissors' and computer_choice == 'Paper'):
        your_points += 1
        result_1 = "You WIN"
        result_2 = f"Your choice is {player_choice}"
        result_3 = f"Computer choice is {computer_choice}"

    elif (player_choice == 'Rock' and computer_choice == 'Paper') \
            or  (player_choice == 'Paper' and computer_choice == 'Scissors') or\
            (player_choice == 'Scissors' and computer_choice == 'Rock'):
        computer_points += 1
        result_1 = "You LOSE"
        result_2 = f"Your choice is {player_choice}"
        result_3 = f"Computer choice is {computer_choice}"


    final_result = f"Result:  You - {your_points}         Computer - {computer_points}"

    if your_points > computer_points:
        label_final_result = Label(root, text=final_result, padx=70, pady=10, background='green')
    elif your_points < computer_points:
        label_final_result = Label(root, text=final_result, padx=70, pady=10, background='red')
    if your_points == computer_points:
        label_final_result = Label(root, text=final_result, padx=70, pady=10, background='yellow')

    if result_1 == "You WIN":
        label_result_1 = Label(root, text=result_1, padx=70, pady=10, background='green', font='blue')
        label_result_2 = Label(root, text=result_2, padx=70, pady=10, background='green', font='blue')
        label_result_3 = Label(root, text=result_3, padx=70, pady=10, background='green', font='blue')
    elif result_1 == "You LOSE":
        label_result_1 = Label(root, text=result_1, padx=70, pady=10, background='red', font='blue')
        label_result_2 = Label(root, text=result_2, padx=70, pady=10, background='red', font='blue')
        label_result_3 = Label(root, text=result_3, padx=70, pady=10, background='red', font='blue')
    else:
        label_result_1 = Label(root, text=result_1, padx=70, pady=10, background='yellow', font='blue')
        label_result_2 = Label(root, text=result_2, padx=70, pady=10, background='yellow', font='blue')
        label_result_3 = Label(root, text=result_3, padx=70, pady=10, background='yellow', font='blue')

    label_final_result.grid(row=1, column=0, columnspan=3, sticky=E+W)
    label_result_1.grid(row=2, column=0, columnspan=3, sticky=E+W)
    label_result_2.grid(row=3, column=0, columnspan=3, sticky=E+W)
    label_result_3.grid(row=4, column=0, columnspan=3, sticky=E+W)


    button_rock = Button(root, text='Rock', padx=30, pady=10, command=lambda:
    choice('Rock', your_points, computer_points))
    button_paper = Button(root, text='Paper', padx=30, pady=10, command=lambda:
    choice('Paper', your_points, computer_points))
    button_scissors = Button(root, text='Scissors', padx=30, pady=10, command=lambda:
    choice('Scissors', your_points, computer_points))

    button_rock.grid(row=0, column=0)
    button_paper.grid(row=0, column=1)
    button_scissors.grid(row=0, column=2)

button_rock = Button(root, text='Rock', padx=30, pady=10, command=lambda:
choice('Rock', your_points, computer_points))
button_paper = Button(root, text='Paper', padx=30, pady=10, command=lambda:
choice('Paper', your_points, computer_points))
button_scissors = Button(root, text='Scissors', padx=30, pady=10, command=lambda:
choice('Scissors', your_points, computer_points))
label_final_result = Label(root, text=final_result, padx=70, pady=10, background='yellow')


button_rock.grid(row=0, column=0)
button_paper.grid(row=0, column=1)
button_scissors.grid(row=0, column=2)
label_final_result.grid(row=1, column=0, columnspan=3, sticky=E+W)

root.mainloop()
