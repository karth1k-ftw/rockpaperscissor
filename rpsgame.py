import random

done = False
wins, losses, ties = 0,0,0

names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

while not done:
    choice = input('Please choose your next move (R,P,S) (Q to Quit): ').upper()
    cpu_choice = random.choice(['R', 'P', 'S'])
    if choice == cpu_choice:
        print(f"It's a  tie! You both chose {names[choice]}")
        ties += 1
    elif choice == 'R':
        if cpu_choice == 'P':
            print(f'CPU wins! You chose {names[choice]}, the CPU chose {names[cpu_choice]}.')
            losses += 1
        else:
            print(f'YOU WIN! You chose {names[choice]}, the CPU chose {names[cpu_choice]}.')
            wins += 1

    elif choice == 'P':
        if cpu_choice == 'S':
            print(f'CPU wins! You chose {names[choice]}, the CPU chose {names[cpu_choice]}.')
            losses += 1
        else:
            print(f'YOU WIN! You chose {names[choice]}, the CPU chose {names[cpu_choice]}.')
            wins += 1

    elif choice == 'S':
        if cpu_choice == 'R':
            print(f'CPU wins! You chose {names[choice]}, the CPU chose {names[cpu_choice]}.')
            losses += 1
        else:
            print(f'YOU WIN! You chose {names[choice]}, the CPU chose {names[cpu_choice]}.')
            wins += 1

    elif choice == 'Q':
        done = True
    else:
        print('Invalid Command')

    print(f'Current Stats: {wins} Wins, {losses} Losses, {ties} Ties')

