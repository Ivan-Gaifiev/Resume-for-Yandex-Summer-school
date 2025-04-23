import sys


def set_rotor_cmd():
    """
    Gets the initial rotor settings either from the command line or user input.

    Returns:
        str: A string representing the rotor settings (e.g., "AAA" or "БАА").

    Raises:
        ValueError: If the number of parameters in the command line is invalid.
    """
    try:
        if len(sys.argv) == 1:
            rotors_settings = input("Enter states for three rotors (format: AAA/БАА...): ").upper()
            if len(rotors_settings) != 3:
                raise ValueError("Rotor settings must be exactly 3 characters!")
        elif len(sys.argv) == 4:
            rotors_settings = str(sys.argv[1]).upper()
            if len(rotors_settings) != 3:
                raise ValueError("Rotor settings must be exactly 3 characters!")
        else:
            raise ValueError("Only 3 parameters are allowed in the command line!")
        return rotors_settings
    except Exception as e:
        print(f"Error in rotor settings: {e}")
        raise


def set_panel_cmd():
    """
    Sets the connecting panel configuration by swapping pairs of letters.

    Returns:
        dict: A dictionary where keys are letters and values are their swapped counterparts.

    Raises:
        ValueError: If the number of parameters in the command line is invalid.
    """
    try:
        conn_panel_d = {}
        if len(sys.argv) == 1:
            conn_panel = input("Enter settings for the connecting panel (format: AБ/БВ...): ").upper()
        elif len(sys.argv) == 4:
            conn_panel = str(sys.argv[2]).upper()
        else:
            raise ValueError("Only 3 parameters are allowed in the command line!")

        if len(conn_panel) % 2 != 0:
            raise ValueError("Connecting panel settings must be in pairs of two letters (e.g., AББВ).")

        for i in range(0, len(conn_panel), 2):
            conn_panel_d[conn_panel[i]] = conn_panel[i + 1]
            conn_panel_d[conn_panel[i + 1]] = conn_panel[i]  # Ensure bidirectional mapping
        return conn_panel_d
    except Exception as e:
        print(f"Error in connecting panel settings: {e}")
        raise


def my_text_cmd():
    """
    Gets the text to encrypt/decrypt from the command line or user input.

    Returns:
        str: The text to process, converted to uppercase.

    Raises:
        ValueError: If the text is empty or contains invalid characters.
    """
    try:
        if len(sys.argv) == 4:
            text_to_encrypt = str(sys.argv[3]).upper()
        else:
            text_to_encrypt = input("Enter your text: ").upper()

        if not text_to_encrypt:
            raise ValueError("Text cannot be empty!")

        return text_to_encrypt
    except Exception as e:
        print(f"Error in text input: {e}")
        raise


def get_configurations():
    """
    Reads rotor and reflector configurations from a file.

    Returns:
        tuple: Rotor and reflector configurations.
               - rotor1 (list): Entrance and exit wiring for rotor 1.
               - rotor2 (list): Entrance and exit wiring for rotor 2.
               - rotor3 (list): Entrance and exit wiring for rotor 3.
               - reflector (dict): Reflector mapping.

    Raises:
        IOError: If the file cannot be opened.
        ValueError: If the file content is invalid.
    """
    try:
        with open("Machine configuration.txt", 'r', encoding="utf-8") as f:
            reflector = {}
            rotor1, rotor2, rotor3 = [], [], []
            lines = f.readlines()

            # Validate the configuration file structure
            if len(lines) < 8:
                raise ValueError("Configuration file has insufficient data!")

            rotor1.append([lines[2][17:][i] for i in range(len(lines[2][17:])) if i % 2 == 0])
            rotor1.append([lines[3][13:][i] for i in range(len(lines[3][13:])) if i % 2 == 0])

            rotor2.append(rotor1[0])  # Reuse rotor1 entrance
            rotor2.append([lines[5][14:][i] for i in range(len(lines[5][14:])) if i % 2 == 0])

            rotor3.append(rotor1[0])  # Reuse rotor1 entrance
            rotor3.append([lines[7][13:][i] for i in range(len(lines[7][13:])) if i % 2 == 0])

            reflector = dict(zip(rotor1[0], reversed(rotor1[0])))

            # Check rotor lengths
            if len(rotor1[0]) != len(rotor1[1]) or len(rotor2[0]) != len(rotor2[1]) or len(rotor3[0]) != len(rotor3[1]):
                raise ValueError("Rotor configurations must have matching entrance and exit lengths.")

            return rotor1, rotor2, rotor3, reflector
    except FileNotFoundError:
        print("Configuration file 'Machine configuration.txt' not found!")
        raise
    except ValueError as e:
        print(f"Error in configuration file: {e}")
        raise
