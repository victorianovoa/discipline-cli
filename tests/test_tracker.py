from src.tracker import add_registro

def test_add_valido():
    assert add_registro("treino", 60) == True

def test_valor_invalido():
    assert add_registro("treino", -10) == False

def test_jejum():
    assert add_registro("jejum", 16) == True