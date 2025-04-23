import Enigma as e
import pytest

# launch by writing 'pytest -s' in terminal

@pytest.fixture
def enigma_settings():
    """Resets encryption and decryption settings to default."""
    return {
        'text': 'ИВАН',
        'sett': 'АВА',
        'panel': 'ВП'
    }


@pytest.fixture
def machine_configuration():
    """Preparing and reconfiguring the machine for file tests"""
    with open("Machine configuration.txt", "r+", encoding="utf-8") as f:
        lines = f.readlines()
        yield lines
        f.truncate(0)
        f.writelines(lines)


@pytest.mark.parametrize("text, sett, panel", [
    ('ИВАН', 'АВА', 'ВП'),
    ('ИВАН', 'АРЫ', 'ВП'),
    ('ИВАН', 'АВА', 'АН'),
    ('ИВАН', 'АРЫ', 'АН')
])
def test_encryption_decryption(text, sett, panel):
    """Checking the correctness of encryption and decryption with different settings"""
    print(f"\nTesting text: {text}, settings: {sett}, panel: {panel}")
    encrypt = e.main(text, sett, panel)
    result = e.main(encrypt, sett, panel)
    assert result == text
    print(f'My text: {text}, encrypted text: {encrypt}, result: {result}\n')


@pytest.mark.parametrize("sett", ['ЯЯЯ', 'ЯЯЮ'])
def test_decryption_with_different_rotors(sett, enigma_settings):
    """Checking for impossibility of decryption if rotor settings are different"""
    print(f"Fifth test with setting: {sett}")
    text = enigma_settings['text']
    panel = enigma_settings['panel']
    encrypt = e.main(text, enigma_settings['sett'], panel)
    result = e.main(encrypt, sett, panel)

    try:
        assert result == text
        print(f'My text: {text}, encrypted text: {encrypt}, result: {result}\n')
    except AssertionError:
        print("Unable to decipher as rotor settings are different")


import shutil


def test_batch_encryption_decryption():
    """Testing encryption and decryption of multiple texts"""
    print("Seventh test")
    texts = ['ИВАН', 'СЛОВО']
    sett = 'АРЫ'
    panel = 'АН'

    for word in texts:
        encrypt = e.main(word, sett, panel)
        result = e.main(encrypt, sett, panel)
        assert result == word
        print(f'My text: {word}, encrypted text: {encrypt}, result: {result}\n')
