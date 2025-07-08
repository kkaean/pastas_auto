import os 
diretorio = r""
for i in range(7, 40):
    nome_do_arquivo = f"exercicio{i}.py"
    caminho_completo = os.path.join(diretorio, nome_do_arquivo)
    open(caminho_completo, "w").close()
