alphabet_rus = [" ", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С",
                "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ы", "Ъ", "Э", "Ю", "Я"]  # 34 symbols

class Rotor:
    """
    Represents a rotor in the Enigma machine. Each rotor transforms letters based on its wiring configuration.
    """

    def __init__(self, entrance, exit):
        """
        Initializes the rotor with its entrance and exit configurations.

        Args:
            entrance (list): The input wiring of the rotor.
            exit (list): The output wiring of the rotor.
        """
        self.__entrance = entrance
        self.__exit = exit

    def get_entrance(self):
        """Returns the rotor's entrance wiring."""
        return self.__entrance

    def get_exit(self):
        """Returns the rotor's exit wiring."""
        return self.__exit

    def set_entrance(self, new_entrance):
        """Updates the rotor's entrance wiring."""
        self.__entrance = new_entrance

    def set_exit(self, new_exit):
        """Updates the rotor's exit wiring."""
        self.__exit = new_exit

    def change_rot_sett(self, init_sett, rotors):
        """
        Adjusts the rotor's position based on initial settings.

        Args:
            init_sett (list): List of initial rotor positions.
            rotors (list): List of Rotor objects.
        """
        try:
            if len(init_sett) != len(rotors):
                raise ValueError("Rotor settings must match the number of rotors.")

            for i in range(len(init_sett)):
                ind = alphabet_rus.index(init_sett[i].upper())  # Ensure uppercase
                entrance_len = len(rotors[i].get_entrance())
                exit_len = len(rotors[i].get_exit())

                ind = ind % entrance_len  # Ensure index wraps within range

                entrance_data = rotors[i].get_entrance()
                exit_data = rotors[i].get_exit()

                rotors[i].set_entrance([*entrance_data[ind:], *entrance_data[:ind]])
                rotors[i].set_exit([*exit_data[ind:], *exit_data[:ind]])
            return rotors
        except ValueError as e:
            print(f"Error in rotor settings: {e}")
            raise

    def rotors_forward(self, letter, rotors, counts):
        """
        Processes a letter through the rotors in the forward direction.

        Args:
            letter (str): The input letter.
            rotors (list): List of Rotor objects.
            counts (list): Keeps track of rotor rotations.

        Returns:
            str: The letter after processing through all rotors.
        """
        try:
            if letter not in alphabet_rus:
                raise ValueError(f"Invalid letter '{letter}' not in allowed alphabet.")

            for i in range(len(rotors)):
                entrance_data = rotors[i].get_entrance()
                exit_data = rotors[i].get_exit()

                letter = exit_data[entrance_data.index(letter)]

                if i == 0:  # Rotor 1 rotation
                    rotors[0].set_exit([*rotors[0].get_exit()[1:], rotors[0].get_exit()[0]])
                    counts[0] += 1
                    if counts[0] == len(alphabet_rus):
                        counts[0] = 0
                        rotors[1].set_exit([*rotors[1].get_exit()[1:], rotors[1].get_exit()[0]])
                        counts[1] += 1

                elif i == 1:  # Rotor 2 rotation
                    if counts[1] == len(alphabet_rus):
                        counts[1] = 0
                        rotors[2].set_exit([*rotors[2].get_exit()[1:], rotors[2].get_exit()[0]])
                        counts[2] += 1
            return letter
        except ValueError as e:
            print(f"Error during forward processing: {e}")
            raise

    def back_signal(self, letter, rotors):
        """
        Processes a letter through the rotors in the reverse direction.

        Args:
            letter (str): The input letter.
            rotors (list): List of Rotor objects.

        Returns:
            str: The letter after processing through all rotors in reverse.
        """
        try:
            for i in range(2, -1, -1):  # Process rotors in reverse order
                entrance_data = rotors[i].get_entrance()
                exit_data = rotors[i].get_exit()

                letter = entrance_data[exit_data.index(letter)]
            return letter
        except ValueError as e:
            print(f"Error during reverse processing: {e}")
            raise


class Reflector:
    """
    Represents the reflector in the Enigma machine.
    Reflects letters symmetrically to create a reversible encryption.
    """

    def __init__(self, mapping):
        """
        Initializes the reflector with a specific mapping.

        Args:
            mapping (dict): A dictionary mapping letters to their reflected counterparts.
        """
        self.__mapping = mapping

    def get_mapping(self):
        """Returns the reflector's mapping."""
        return self.__mapping

    def reflecting(self, reflect, letter):
        """
        Reflects a letter using the reflector's mapping.

        Args:
            reflect (dict): The reflector's mapping.
            letter (str): The input letter.

        Returns:
            str: The reflected letter.
        """
        try:
            return reflect[letter]
        except KeyError:
            print(f"Error: Letter '{letter}' not found in reflector mapping.")
            raise


class Conn_panel:
    """
    Represents the connection panel in the Enigma machine.
    Allows swapping letters before and after rotor processing.
    """

    def __init__(self, settings):
        """
        Initializes the connection panel with specific settings.

        Args:
            settings (dict): A dictionary defining letter swaps.
        """
        self.__settings = settings

    def lett_to_conn(self, letter):
        """
        Swaps a letter using the connection panel's settings.

        Args:
            letter (str): The input letter.

        Returns:
            str: The swapped letter, or the original letter if no swap exists.
        """
        try:
            letter = letter.upper()  # Ensure uppercase
            return self.__settings.get(letter, letter)  # Return swapped letter if exists
        except Exception as e:
            print(f"Error during connection panel processing: {e}")
            raise
