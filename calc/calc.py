import re
import math
import speech_recognition as sr


class OpCalculator:
    def __init__(self):
        self.operations = {
            'addition': '+',
            'division': '/',
            'exponentiation': '**',
            'multiply': '*',
            'subtraction': '-',
            'root': 'sqrt',
        }

    def look_expression(self, expression):
        try:
            # If there are words, replace them with operators
            for word, operator in self.operations.items():
                expression = expression.replace(word, operator)

            # Evaluate the expression
            result = eval(expression)
            return result

        except Exception as e:
            return f"Error: {str(e)}"

    def voice_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("What would you like to calculate?: ")
            audio = r.listen(source)

        try:
            calculation = r.recognize_google(audio)
            return calculation
        except sr.UnknownValueError:
            return "Sorry I could not understand!"
        except sr.RequestError as e:
            return f"I am sorry, I could not get any results from Google Speech Recognition services; {e}"

    def run(self):
        print("Hello! Welcome to Op Calculator")
        while True:
            choice = input("Do you want to use your voice or use input? (yes/no): ")
            if choice == "yes":
                calculation = self.voice_input()
                if calculation == "Sorry I could not understand!" or calculation.startswith("I am sorry"):
                    print(calculation)
                    continue
                print(f"You said: {calculation}")
            elif choice == "no":
                calculation = input("What would you like to calculate?: ")
            else:
                print("Wrong choice. Please choose 'yes' or 'no'.")
                continue

            result = self.look_expression(calculation)
            print(f"Result: {result}")

            another_calculation = input("Would you like to do another calculation? (yes/no): ")
            if another_calculation != 'yes':
                print("Goodbye!")
                break

calculator = OpCalculator()
calculator.run()
