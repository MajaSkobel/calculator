import logging
import math

logging.basicConfig(level=logging.DEBUG)

def add(numbers):
    return sum(numbers) 
def subtract(x_1,x_2):
    return x_1-x_2 
def multiply(numbers):
    return math.prod(numbers)
def divide(x_1,x_2):
    return x_1/x_2 

action = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

if __name__ == "__main__":
    action_input = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if not action_input in range(1,5,1):
            logging.error("Wprowadzono niepoprawny input")
            exit(1)
    if action_input == 2 or action_input == 4:
        x_1 = float(input("Podaj pierwszy składnik: "))
        x_2 = float(input("Podaj drugi składnik: "))
        logging.info(f"Wykonuję działanie {action[action_input]} z wartościami {x_1} i {x_2}.")
        print("Wynik to:", action[action_input](x_1,x_2))
    else:
        user_input = input("Podaj składniki oddzielone przecinkami: ")
        numbers_in_string = user_input.split(",")
        numbers = [float(num) for num in numbers_in_string]
        logging.info(f"Wykonuję działanie {action[action_input]} z wartościami {numbers}.")
        print("Wynik to:", action[action_input](numbers))