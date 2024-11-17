"""
My lab 7
"""

from time import sleep
from questions import TEXT, TRUE_RESPONDS

print('Вітаю вас в грі "Brain is power"')
print('Правило лише одне не використовувати інтернет джерела під час гри')
print('Якщо ви захочете повернутися назад то введіть 4')
print('Ну що приступимо')

STEP = 1
responds = []
while STEP < 7:
    print(TEXT[STEP - 1])
    respond = int(input('Введіть відповідь: '))
    if 0 < respond < 5:
        if respond == 4:
            try:
                responds.pop(-1)
                STEP -= 1
            except IndexError:
                print("Ви вже на першому запитанні")
        else:
            responds.append(respond)
            STEP += 1
    else:
        print('Введіть правильне значеня відповіді')

POINTS = 0
for n in range(6):
    if responds[n] == TRUE_RESPONDS[n]:
        POINTS += 2
print(f"Ви набрали {POINTS} балів")

def queue_bus(people):
    """
    queue people in bas
    """
    for person in people:
        print(f"{person} сів в автобус")
        sleep(5)

PEOPLE = ["Andrii", "Semen", "Nastia", "Stepan", "Sophia", "Roman", "Nazar", "Katia"]
queue_bus(PEOPLE)
