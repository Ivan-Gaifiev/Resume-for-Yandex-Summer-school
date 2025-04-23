import Machine_elements as m_e
import Interaction_and_file as i_f


class Enigma:
    """
    A class representing the Enigma machine.
    It can encrypt text using rotors, a reflector, and a connection panel.

    Attributes:
        counts (list): Keeps track of rotor rotations.
        rotors (list): A list of Rotor objects.
        reflector (Reflector): Reflector object for letter reflection.
        conn_panel (Conn_panel): Connection panel for swapping letters.
    """

    def __init__(self):
        """
        Initializes the Enigma machine with default settings.
        """
        self.counts = [0, 0, 0]
        self.rotors = []
        self.reflector = None
        self.conn_panel = None

    def setup_machine(self):
        """
        Sets up the Enigma machine components: rotors, reflector, and connection panel.
        Reads configurations and user settings.
        """
        try:
            rot_sett = i_f.set_rotor_cmd()
            if len(rot_sett) != 3:
                raise ValueError("Rotor settings must include exactly 3 characters.")
            rot_sett = rot_sett.upper()  # Ensure uppercase for uniformity

            conn_panel_settings = i_f.set_panel_cmd()
            self.conn_panel = m_e.Conn_panel(conn_panel_settings)

            rotor1_config, rotor2_config, rotor3_config, reflector_config = i_f.get_configurations()
            rotor1 = m_e.Rotor(rotor1_config[0], rotor1_config[1])
            rotor2 = m_e.Rotor(rotor2_config[0], rotor2_config[1])
            rotor3 = m_e.Rotor(rotor3_config[0], rotor3_config[1])
            self.reflector = m_e.Reflector(reflector_config)
            self.rotors = [rotor1, rotor2, rotor3]

            for rotor in self.rotors:
                rotor.change_rot_sett(rot_sett, self.rotors)
        except ValueError as e:
            print(f"Error during setup: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error during setup: {e}")
            raise

    def encrypt(self):
        """
        Encrypts a user-provided text.

        Returns:
            str: The encrypted text.
        """
        try:
            text_to_encrypt = i_f.my_text_cmd()
            if not text_to_encrypt:
                raise ValueError("No text provided for encryption.")
            text_to_encrypt = text_to_encrypt.upper()  # Convert to uppercase

            encrypted_text = ''
            for letter in text_to_encrypt:
                if letter not in m_e.alphabet_rus:
                    raise ValueError(f"Invalid character '{letter}' detected. Only Russian letters and spaces are allowed.")

                letter = self.conn_panel.lett_to_conn(letter)
                letter = self.forward_through_rotors(letter)
                letter = self.reflector.reflecting(self.reflector.get_mapping(), letter)
                letter = self.backward_through_rotors(letter)
                letter = self.conn_panel.lett_to_conn(letter)
                encrypted_text += letter

            return encrypted_text
        except ValueError as e:
            print(f"Encryption error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error during encryption: {e}")
            raise

    def forward_through_rotors(self, letter):
        """
        Passes a letter through all rotors in the forward direction.

        Args:
            letter (str): The letter to process.

        Returns:
            str: The processed letter.
        """
        for rotor in self.rotors:
            letter = rotor.rotors_forward(letter, self.rotors, self.counts)
        return letter

    def backward_through_rotors(self, letter):
        """
        Passes a letter through all rotors in the reverse direction.

        Args:
            letter (str): The letter to process.

        Returns:
            str: The processed letter.
        """
        for rotor in reversed(self.rotors):
            letter = rotor.back_signal(letter, self.rotors)
        return letter
