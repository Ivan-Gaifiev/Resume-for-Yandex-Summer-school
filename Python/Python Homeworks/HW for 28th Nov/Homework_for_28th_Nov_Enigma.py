import Machine_work as m_w
import Machine_elements as m_e


def main():
    """
    Main function to run the Enigma machine simulation.

    - Sets up the machine configuration.
    - Encrypts the provided input text.
    - Handles input errors and ensures proper uppercase formatting.
    """
    try:
        machine = m_w.Enigma()  # Initialize the Enigma machine
        machine.setup_machine()  # Setup machine configuration (rotors, reflector, and connecting panel)

        # Perform encryption
        res_word = machine.encrypt()

        print("Encrypted text:", res_word)  # Print the encrypted result
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except FileNotFoundError:
        print("Error: Configuration file not found. Ensure 'Machine configuration.txt' is present.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
