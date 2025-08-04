# ETA2024.2_TesteUnitarioPytest_VALIDADOR

# 📦 Validador de CPF, CNPJ e CEP com Pytest

Este projeto implementa uma classe `Validador` com métodos para validar:

- CPF
- CNPJ
- CEP

Inclui uma suíte de testes unitários usando `pytest` com cenários:
- Válidos (caminho feliz)
- Inválidos
- Casos de exceção (tipo errado)

## 🚀 Como usar

### 1. Instalar dependências
pip install -r requirements.txt

### 2. Executar testes
pytest -v

### 3. Ver cobertura de testes
pytest --cov=validador --cov-report=term-missing

🛠 Estrutura do Projeto
validador/
├── validador.py          # Código principal
├── test_validador.py     # Testes com pytest
├── requirements.txt      # Dependências
└── README.md             # Instruções

✅ Requisitos
-Python 3.8+
-pytest
-pytest-cov
