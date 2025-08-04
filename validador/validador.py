import re

class Validador:

    def _limpar_texto(self, texto):
        if not isinstance(texto, str):
            raise ValueError("Entrada deve ser uma string.")
        return re.sub(r'\D', '', texto)

    def validar_cpf(self, texto):
        cpf = self._limpar_texto(texto)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False

        def calcular_dv(cpf_parcial):
            soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(len(cpf_parcial)+1, 1, -1)))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        dv1 = calcular_dv(cpf[:9])
        dv2 = calcular_dv(cpf[:9] + dv1)
        return cpf.endswith(dv1 + dv2)

    def validar_cnpj(self, texto):
        cnpj = self._limpar_texto(texto)
        if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
            return False

        def calcular_dv(cnpj_parcial, pesos):
            soma = sum(int(digito) * peso for digito, peso in zip(cnpj_parcial, pesos))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos2 = [6] + pesos1

        dv1 = calcular_dv(cnpj[:12], pesos1)
        dv2 = calcular_dv(cnpj[:12] + dv1, pesos2)
        return cnpj.endswith(dv1 + dv2)

    def validar_cep(self, texto):
        cep = self._limpar_texto(texto)
        return len(cep) == 8 and cep.isdigit()
