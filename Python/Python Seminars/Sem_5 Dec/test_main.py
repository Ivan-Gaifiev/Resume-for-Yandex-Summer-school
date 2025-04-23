import Seminar_5_Dec
import io
import pytest
P = "G"
def test_AddFunction():
    assert True

def test_adding_plice_number(monkeypatch):
     def monkey_input(promt=''):
        return "222"
     monkeypatch.setattr("builtins.input",monkey_input)



     mock_stdout = io.StringIO()
     monkeypatch.setattr("sys.stdout", mock_stdout)
     Seminar_5_Dec.sum()

     assert mock_stdout.getvalue() == '444\n'



