"""
Task 2 to my lab 7
"""

from time import sleep

def queue_bus(people):
    """
    queue people in bas
    """
    for person in people:
        print(f"{person} сів в автобус")
        sleep(5)

PEOPLE = ["Andrii", "Semen", "Nastia", "Stepan", "Sophia", "Roman", "Nazar", "Katia"]
queue_bus(PEOPLE)
