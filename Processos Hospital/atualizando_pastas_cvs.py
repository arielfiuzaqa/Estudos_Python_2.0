# Criando uma atualização automatica de todas as pastas do wincvs
import subprocess
import os

# Diretório raiz onde as pastas do CVS estão localizadas 
diretorio_raiz = 'D:\\cvs'

def listar_pastas(diretorio):
    # Lista todos os subdiretórios em um diretório especificado
    pastas = [os.path.join(diretorio, nome) for nome in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, nome))]
    return pastas

def atualizar_pastas(pastas): 
    # Atualiza todas as pastas passadas como argumento
    for pasta in pastas:
        # Muda o diretório atual para a pasta
        os.chdir(pasta)
        # Comando para atualizar a pasta atual
        comando = "cvs update"
        try:
            # Executa o comando
            resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            # Imprime a saída do comando
            print(f"Atualizando {pasta}...")
            print(resultado.stdout)
        except subprocess.CalledProcessError as e:
            # Em caso de erro, imprime a saída de erro
            print(f"Erro ao atualizar {pasta}:")
            print(e.stderr)
            

if __name__ == "__main__":
    # Primeiro, lista todas as pastas no diretório raiz
    pastas = listar_pastas(diretorio_raiz)
    
    # Então, atualiza todas as pastas listadas
    atualizar_pastas(pastas)
