from src.weather import recomendacao_clima


def test_recomendacao_clima_calor():
    resultado = recomendacao_clima(35)

    assert "hidratação" in resultado.lower()


def test_recomendacao_clima_frio():
    resultado = recomendacao_clima(10)

    assert "intenso" in resultado.lower()


def test_recomendacao_clima_equilibrado():
    resultado = recomendacao_clima(24)

    assert "moderado" in resultado.lower()