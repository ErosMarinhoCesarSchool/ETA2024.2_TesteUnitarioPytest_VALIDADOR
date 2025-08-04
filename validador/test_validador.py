import pytest
from validador import Validador

@pytest.fixture
def validador():
    return Validador()

# ----------------------------
# Testes de CPF
# ----------------------------

@pytest.mark.parametrize("cpf_valido", [
    "529.982.247-25",
    "52998224725",
])
def test_validar_cpf_valido(validador, cpf_valido):
    assert validador.validar_cpf(cpf_valido) is True

@pytest.mark.parametrize("cpf_invalido", [
    "123.456.789-00",
    "11111111111",
    "5299822472",       # Menos dígitos
    "529982247252",     # Mais dígitos
])
def test_validar_cpf_invalido(validador, cpf_invalido):
    assert validador.validar_cpf(cpf_invalido) is False

@pytest.mark.parametrize("entrada_invalida", [12345678901, None, True])
def test_validar_cpf_tipo_invalido(validador, entrada_invalida):
    with pytest.raises(ValueError):
        validador.validar_cpf(entrada_invalida)

# ----------------------------
# Testes de CNPJ
# ----------------------------

@pytest.mark.parametrize("cnpj_valido", [
    "04.252.011/0001-10",
    "04252011000110"
])
def test_validar_cnpj_valido(validador, cnpj_valido):
    assert validador.validar_cnpj(cnpj_valido) is True

@pytest.mark.parametrize("cnpj_invalido", [
    "00.000.000/0000-00",
    "11111111111111",
    "0425201100011",     # Menos dígitos
    "042520110001100",   # Mais dígitos
])
def test_validar_cnpj_invalido(validador, cnpj_invalido):
    assert validador.validar_cnpj(cnpj_invalido) is False

@pytest.mark.parametrize("entrada_invalida", [12345678000199, [], None])
def test_validar_cnpj_tipo_invalido(validador, entrada_invalida):
    with pytest.raises(ValueError):
        validador.validar_cnpj(entrada_invalida)

# ----------------------------
# Testes de CEP
# ----------------------------

@pytest.mark.parametrize("cep_valido", [
    "01001-000",
    "01001000"
])
def test_validar_cep_valido(validador, cep_valido):
    assert validador.validar_cep(cep_valido) is True

@pytest.mark.parametrize("cep_invalido", [
    "ABCDE000",      # Letras
    "0100100",       # Menos dígitos
    "010010000",     # Mais dígitos
])
def test_validar_cep_invalido(validador, cep_invalido):
    assert validador.validar_cep(cep_invalido) is False

@pytest.mark.parametrize("entrada_invalida", [12345678, {}, None])
def test_validar_cep_tipo_invalido(validador, entrada_invalida):
    with pytest.raises(ValueError):
        validador.validar_cep(entrada_invalida)
