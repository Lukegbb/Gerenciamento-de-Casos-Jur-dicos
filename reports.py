from database import buscar_casos

def gerar_relatorio():
    casos = buscar_casos()
    
    if casos:
        print("\n=== Relatório de Casos Jurídicos ===")
        for caso in casos:
            print(f"ID: {caso[0]}, Número: {caso[1]}, Cliente: {caso[2]}, Status: {caso[4]}")
        print("\nTotal de casos: ", len(casos))
    else:
        print("Nenhum caso encontrado.")
