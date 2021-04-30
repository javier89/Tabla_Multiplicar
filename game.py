import random

class BaseGame:
    # Longitud en la que se centre el mensaje
    message_lenght = 60

    description = ""
    
    def __init__(self, points_to_win, n_lives=3):
        """
            Clase de juego base Args:point_to_win(int):
            los puntos que necesitara terminar el juego el
            n_lives(int): El numero de vidas que tiene el estudiante.
            Por defecto es 3.
        """
        
        self.points_to_win = points_to_win
        self.points = 0
        self.lives = n_lives

    def get_numeric_input(sel, message=""):
        while True:
            # Obtener la entrada del usuario
            user_input = input(message)
            # Si la entrada es numerica, devuelva 
            # Si no es asi, imprima un mensaje y repita
            if user_input.isnumeric():
                return int(user_input)
            else:
                print("La entrada debe ser numerica")
                continue
    def print_welcome_message(self):
        print("Juego de Multiplicar de Python".center(self.message_lenght))

    def print_lose_message(self):
        print(" Lo siento has perdido todas tus vidas".center(self.message_lenght))

    def print_win_message(self):
        print(f"Felicidades alcanzaste {self.points}".center(self.message_lenght))

    def print_current_lives(self):
        print(f"Actualmente tienes {self.lives} lives\n")

    def print_current_score(self):
        print(f"\nTu puntuaje es {self.points}")

    def print_description(self):
        print("\n\n" + self.description.center(self.message_lenght )+ "\n")

    # Metodo de ejecucion basico
    def run(self):
        self.print_welcome_message()
        
        self.print_description()


class RandomMultiplicacion(BaseGame):
    
    description = "En este juego debes responder correctamente a la multiplicacion aleatoria \n Ganas si llegas a 5 puntos, o pierdes si pierdes todas tus vidas"

    def __init__(self):

        # La cantidad de puntos necesarios para ganar son 5
        super().__init__(5)

    def get_random_numbers(self):

        first_number = random.randint(1, 10)
        second_number = random.randint(1, 10)

        return first_number, second_number

    def run(self):
        
        # Llamando a la clase para imprimir los mensajede bienvenida
        super().run()

        while self.lives > 0 and self.points_to_win > self.points:
            # Obtiene dos numeros aleatorios
            number1, number2 = self.get_random_numbers()

            operation = f"{number1} X {number2}: "

            # Pide al usuario que responda esa operacion 
            # Evitar Errores de Valor
            user_answer = self.get_numeric_input(message = operation)

            if user_answer == number1 * number2:
                print("\n Tu respuesta es correcta \n")

                # Agrega un punto
                self.points += 1
            else:
                print("\n Lo siento, tu respuesta es incorrecta \n")

                # Resta un punto
                self.points -= 1

            self.print_current_score()
            self.print_current_lives()

        # Solo se ejecuta cuan el juego termina
        # y ninguna de las condiciones en cierta
        else:
            # Imprime el mensaje final

            if self.points >= self.points_to_win:
                self.print_win_message()
            else:
                self.print_lose_message()

class TableMultiplicar(BaseGame):

    description = "En este juego debes resolver correctamente la tabla de multiplicar completa \n Ganas si resuelves 2 tablas"

    def __init__(self):

        # Necesito completar 2 mesas para ganar
        super().__init__(2)

    def run(self):
        
        super().run()
        
        while self.lives > 0 and self.points_to_win > self.points:
            # Obtiene dos numeros aleatorio
            number = random.randint(1, 10)

            for i in range(1, 10):
                if self.lives <= 0:
                    # Asegurate de que el juego no pueda continuar
                    # Si el usuario agota las vidas
                    self.points = 0
                    break
                
                operation = f"{number} X {i}: "
                user_answer = self.get_numeric_input(message=operation)

                if user_answer == number * i:
                    print("Estupendo! Tu respuesta es correcta")
                else:
                    print("Lo siento, tu respuesta no es correcta")
                    self.lives -= 1
            self.points += 1

        # Solo se ejecuta cuando el juego termina 
        # y ninguna de las condiciones es cierta
        else:

            # Imprime el mensaje final 
            if self.points >= self.points_to_win:
                self.print_win_message()
            else:
                self.print_lose_message()

if __name__ == "__main__":
    print("select Game mode")

    choice = input("[1],[2]")

    if choice == "1":
        game = RandomMultiplicacion()
    elif choice == "2":
        game = TableMultiplicar()
    else:
        print("Por favor seleccione un modo de juego valido")
        exit()
    
    game.run()


