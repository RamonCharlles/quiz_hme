from datetime import datetime
from Fluxo.procedimentos import GerenciadorProcedimentos

class RegistroProcedimento:
    def __init__(self, procedimento, valor_bruto, custos_diretos):
        self.procedimento = procedimento
        self.valor_bruto = valor_bruto
        self.custos_diretos = custos_diretos
        self.data = datetime.now()

    def calcular_lucro(self):
        return self.valor_bruto - self.custos_diretos

class GerenciadorRegistros:
    def __init__(self, gerenciador_procedimentos):
        self.registros = []
        self.gerenciador_procedimentos = gerenciador_procedimentos

    def registrar_procedimento_realizado(self, nome_procedimento, valor_bruto):
        proc = self.gerenciador_procedimentos.obter_procedimento(nome_procedimento)
        if proc:
            custos_diretos = proc.custos_diretos
            registro = RegistroProcedimento(proc, valor_bruto, custos_diretos)
            self.registros.append(registro)
            print(f"Registro de '{nome_procedimento}' realizado em {registro.data.strftime('%d/%m/%Y')}. Valor Bruto: R$ {valor_bruto:.2f}, Lucro: R$ {registro.calcular_lucro():.2f}")
            return registro
        else:
            print(f"Procedimento '{nome_procedimento}' não encontrado.")
            return None

    def listar_registros(self):
        if self.registros:
            print("\n--- Registros de Procedimentos Realizados ---")
            for registro in self.registros:
                print(f"- [{registro.data.strftime('%d/%m/%Y')}] {registro.procedimento.nome}: Bruto R$ {registro.valor_bruto:.2f}, Custos R$ {registro.custos_diretos:.2f}, Lucro R$ {registro.calcular_lucro():.2f}")
        else:
            print("Nenhum registro de procedimento realizado.")

# Exemplo de uso (pode ser movido para o módulo principal)
if __name__ == "__main__":
    gerenciador_proc = GerenciadorProcedimentos()
    gerenciador_proc.cadastrar_procedimento("Limpeza de Pele", 80.00, 15.00)
    gerenciador_reg = GerenciadorRegistros(gerenciador_proc)
    gerenciador_reg.registrar_procedimento_realizado("Limpeza de Pele", 80.00)
    gerenciador_reg.listar_registros()