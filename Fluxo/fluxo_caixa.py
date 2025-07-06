from datetime import datetime

class Transacao:
    def __init__(self, tipo, descricao, valor):
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.descricao = descricao
        self.valor = valor
        self.data = datetime.now()

class FluxoDeCaixa:
    def __init__(self):
        self.transacoes = []
        self.saldo = 0

    def registrar_transacao(self, tipo, descricao, valor):
        transacao = Transacao(tipo, descricao, valor)
        self.transacoes.append(transacao)
        if tipo == 'entrada':
            self.saldo += valor
        elif tipo == 'saida':
            self.saldo -= valor
        print(f"Transação registrada: {tipo.capitalize()} de R$ {valor:.2f} ({descricao}) em {transacao.data.strftime('%d/%m/%Y')}.")

    def obter_saldo(self):
        return self.saldo

    def gerar_relatorio(self, periodo=None):
        print("\n--- Relatório de Fluxo de Caixa ---")
        if periodo:
            print(f"Período: {periodo}") # Implementar lógica de filtro por período
        for transacao in self.transacoes:
            print(f"- [{transacao.data.strftime('%d/%m/%Y')}] {transacao.tipo.capitalize()}: R$ {transacao.valor:.2f} ({transacao.descricao})")
        print(f"\nSaldo Atual: R$ {self.saldo:.2f}")

# Exemplo de uso (pode ser movido para o módulo principal)
if __name__ == "__main__":
    fluxo = FluxoDeCaixa()
    fluxo.registrar_transacao('entrada', 'Pagamento Limpeza de Pele', 80.00)
    fluxo.registrar_transacao('saida', 'Custo Limpeza de Pele', 15.00)
    fluxo.registrar_transacao('saida', 'Aluguel', 1200.00)
    print(f"\nSaldo: R$ {fluxo.obter_saldo():.2f}")
    fluxo.gerar_relatorio()