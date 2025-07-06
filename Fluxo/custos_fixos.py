from datetime import datetime

class CustoFixo:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class GerenciadorCustosFixos:
    def __init__(self):
        self.custos_fixos = {}

    def cadastrar_custo_fixo(self, nome, valor):
        if nome not in self.custos_fixos:
            self.custos_fixos[nome] = CustoFixo(nome, valor)
            print(f"Custo fixo '{nome}' cadastrado com valor de R$ {valor:.2f}.")
        else:
            print(f"Custo fixo '{nome}' já existe.")

    def obter_custo_fixo(self, nome):
        return self.custos_fixos.get(nome)

    def listar_custos_fixos(self):
        if self.custos_fixos:
            print("\n--- Lista de Custos Fixos ---")
            for nome, custo in self.custos_fixos.items():
                print(f"- {nome}: R$ {custo.valor:.2f}")
        else:
            print("Nenhum custo fixo cadastrado.")

    def registrar_pagamento_custo_fixo(self, fluxo_de_caixa, nome_custo):
        custo = self.obter_custo_fixo(nome_custo)
        if custo:
            fluxo_de_caixa.registrar_transacao('saida', f'Pagamento Custo Fixo: {custo.nome}', custo.valor)
            print(f"Pagamento de R$ {custo.valor:.2f} referente a '{custo.nome}' registrado no fluxo de caixa.")
        else:
            print(f"Custo fixo '{nome_custo}' não encontrado.")

# Exemplo de uso (pode ser movido para o módulo principal)
if __name__ == "__main__":
    gerenciador_custos = GerenciadorCustosFixos()
    gerenciador_custos.cadastrar_custo_fixo("Energia", 300.00)
    gerenciador_custos.cadastrar_custo_fixo("Salários", 3000.00)
    gerenciador_custos.listar_custos_fixos()

    # Para registrar um pagamento, precisaríamos de uma instância de FluxoDeCaixa
    # (isso seria feito no módulo principal)