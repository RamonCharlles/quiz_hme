from Fluxo.procedimentos import GerenciadorProcedimentos
from Fluxo.fluxo_caixa import FluxoDeCaixa
from Fluxo.registros import GerenciadorRegistros

def main():
    gerenciador_procedimentos = GerenciadorProcedimentos()
    fluxo_de_caixa = FluxoDeCaixa()
    gerenciador_registros = GerenciadorRegistros(gerenciador_procedimentos)

    while True:
        print("\n--- Software de Gestão de Estética ---")
        print("1. Cadastrar Procedimento")
        print("2. Listar Procedimentos")
        print("3. Registrar Procedimento Realizado")
        print("4. Listar Registros de Procedimentos")
        print("5. Registrar Entrada de Caixa")
        print("6. Registrar Saída de Caixa (Custos Fixos, etc.)")
        print("7. Ver Saldo de Caixa")
        print("8. Gerar Relatório de Fluxo de Caixa")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do procedimento: ")
            preco = float(input("Preço: R$ "))
            custos = float(input("Custos diretos (opcional, padrão 0): R$ ") or 0)
            gerenciador_procedimentos.cadastrar_procedimento(nome, preco, custos)
        elif opcao == '2':
            gerenciador_procedimentos.listar_procedimentos()
        elif opcao == '3':
            nome_procedimento = input("Nome do procedimento realizado: ")
            valor_bruto = float(input("Valor bruto recebido: R$ "))
            registro = gerenciador_registros.registrar_procedimento_realizado(nome_procedimento, valor_bruto)
            if registro:
                fluxo_de_caixa.registrar_transacao('entrada', f'Pagamento {nome_procedimento}', valor_bruto)
                fluxo_de_caixa.registrar_transacao('saida', f'Custo Direto {nome_procedimento}', registro.custos_diretos)
        elif opcao == '4':
            gerenciador_registros.listar_registros()
        elif opcao == '5':
            descricao = input("Descrição da entrada: ")
            valor = float(input("Valor da entrada: R$ "))
            fluxo_de_caixa.registrar_transacao('entrada', descricao, valor)
        elif opcao == '6':
            descricao = input("Descrição da saída: ")
            valor = float(input("Valor da saída: R$ "))
            fluxo_de_caixa.registrar_transacao('saida', descricao, valor)
        elif opcao == '7':
            print(f"\nSaldo de Caixa Atual: R$ {fluxo_de_caixa.obter_saldo():.2f}")
        elif opcao == '8':
            fluxo_de_caixa.gerar_relatorio()
        elif opcao == '9':
            print("Saindo do software.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()