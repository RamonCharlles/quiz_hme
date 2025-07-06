class Procedimento:
    def __init__(self, nome, preco, custos_diretos=0):
        self.nome = nome
        self.preco = preco
        self.custos_diretos = custos_diretos

    def calcular_lucratividade(self):
        return self.preco - self.custos_diretos

class GerenciadorProcedimentos:
    def __init__(self):
        self.procedimentos = {}

    def cadastrar_procedimento(self, nome, preco, custos_diretos=0):
        if nome not in self.procedimentos:
            self.procedimentos[nome] = Procedimento(nome, preco, custos_diretos)
            print(f"Procedimento '{nome}' cadastrado com sucesso.")
        else:
            print(f"Procedimento '{nome}' já existe.")

    def obter_procedimento(self, nome):
        return self.procedimentos.get(nome)

    def listar_procedimentos(self):
        if self.procedimentos:
            print("\n--- Lista de Procedimentos ---")
            for nome, proc in self.procedimentos.items():
                print(f"- {nome}: Preço R$ {proc.preco:.2f}, Custos Diretos R$ {proc.custos_diretos:.2f}")
        else:
            print("Nenhum procedimento cadastrado.")

# Exemplo de uso (pode ser movido para o módulo principal)
if __name__ == "__main__":
    gerenciador_proc = GerenciadorProcedimentos()
    gerenciador_proc.cadastrar_procedimento("Limpeza de Pele", 80.00, 15.00)
    gerenciador_proc.cadastrar_procedimento("Massagem Relaxante", 120.00, 25.00)
    gerenciador_proc.listar_procedimentos()
    limpeza = gerenciador_proc.obter_procedimento("Limpeza de Pele")
    if limpeza:
        print(f"\nLucratividade da {limpeza.nome}: R$ {limpeza.calcular_lucratividade():.2f}")