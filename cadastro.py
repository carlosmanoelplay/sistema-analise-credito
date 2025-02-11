# Importações necessárias
from PyQt5 import uic, QtWidgets
import mysql.connector

# Configurar a conexão com o banco de dados
try:
    conexao = mysql.connector.connect(
        #banco de dados temporiamente offline
        host='127.0.0.1',
        user='dev',
        password='nova_senha_forte',
        database='lcxSpoting_creditos'
    )
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
    exit()

# Função para inserir dados no banco de dados
def inserir_dados():
    try:
        # Coletar dados da interface
        nome = cadastro.lineNOME.text()
        cpf = cadastro.lineCPF.text()
        renda = cadastro.lineRendaBruta.text()
        idade = cadastro.lineIdade.text()
        situacao = cadastro.lineSitucao.text()  # Agora preenchido pelo programa

        # Validar os dados
        if not nome or not cpf or not renda or not idade:
            print("Preencha todos os campos obrigatórios.")
            cadastro.Resposta.setText("Preencha todos os campos obrigatórios.")
            return

        try:
            renda = float(renda)
            idade = int(idade)
        except ValueError:
            print("Renda ou idade inválidos.")
            cadastro.Resposta.setText("Renda ou idade inválidos.")
            return

        # Executar o comando SQL
        cursor = conexao.cursor()
        comando_SQL = 'INSERT INTO clientes (nome, cpf, renda, idade, situacao) VALUES (%s, %s, %s, %s, %s)'
        dados = (nome, cpf, renda, idade, situacao)
        cursor.execute(comando_SQL, dados)

        # Confirmar e fechar conexão
        conexao.commit()
        cursor.close()
        print("Dados inseridos com sucesso!")

        # Limpar os campos da interface
        cadastro.lineNOME.setText('')
        cadastro.lineCPF.setText('')
        cadastro.lineRendaBruta.setText('')
        cadastro.lineIdade.setText('')
        cadastro.lineSitucao.setText('')
        cadastro.Resposta.setText("Dados salvos com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao executar SQL: {err}")
        cadastro.Resposta.setText("Erro ao salvar os dados no banco de dados.")

# Função para análise de crédito
def analise():
    try:
        # Coletar e validar os campos necessários
        renda = cadastro.lineRendaBruta.text()
        idade = cadastro.lineIdade.text()

        try:
            renda = float(renda)
            idade = int(idade)
        except ValueError:
            print("Renda ou idade inválidos.")
            cadastro.Resposta.setText("Renda ou idade inválidos.")
            return

        # Fazer a análise de crédito e preencher o campo "situação"
        if renda >= 3500 and idade >= 21:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        # Atualizar o campo "situação" automaticamente
        cadastro.lineSitucao.setText(situacao)

        # Exibir resultado na interface
        cadastro.Resposta.setText(f"Análise realizada: {situacao}")

    except Exception as e:
        print(f"Erro na análise: {e}")
        cadastro.Resposta.setText("Erro na análise.")
  

def relatorio():
    relatorio.show()

    cursor = conexao.cursor()
    comando_SQL = 'select * from clientes'
    cursor.execute(comando_SQL)
    leitura_clientes = cursor.fetchall()

    relatorio.tabelaClientes.setRowCount(len(leitura_clientes))
    relatorio.tabelaClientes.setColumnCount(6)

    for i in range (0, len(leitura_clientes)):
        for j in range(0, 6):
                    relatorio.tabelaClientes.setItem(i,j, QtWidgets.QTableWidgetItem(str(leitura_clientes[i][j])))
numero_ID_geral = 0
def editar_dados():
    global numero_ID_geral
    dados = relatorio.tabelaClientes.currentRow()
    
    if dados == -1:  # Nenhuma linha selecionada
        print("Nenhum cliente selecionado.")
        relatorio.mensagemErro.setText("Nenhum cliente selecionado.")  # Supondo que tenha um QLabel para mensagens
        return

    cursor = conexao.cursor()
    cursor.execute('SELECT id FROM clientes')
    leitura_clientes = cursor.fetchall()

    if not leitura_clientes or dados >= len(leitura_clientes):  # Verifica se há registros e se o índice é válido
        print("Erro ao buscar cliente. Nenhum cliente encontrado com esse índice.")
        relatorio.mensagemErro.setText("Erro ao buscar cliente.")
        return

    id_ativo = leitura_clientes[dados][0]

    # Buscar os dados do cliente pelo ID
    cursor.execute('SELECT * FROM clientes WHERE id = %s', (id_ativo,))
    leitura_clientes = cursor.fetchall()

    if not leitura_clientes:  # Garante que pelo menos um registro foi encontrado
        print(f"Nenhum cliente encontrado com ID {id_ativo}.")
        relatorio.mensagemErro.setText("Nenhum cliente encontrado.")
        return

    # Exibir os dados na interface de edição
    editar.show()
    numero_ID_geral = id_ativo

    editar.alterarID.setText(str(leitura_clientes[0][0]))
    editar.alterarNOME.setText(str(leitura_clientes[0][1]))
    editar.alterarCPF.setText(str(leitura_clientes[0][2]))
    editar.alterarRendaBruta.setText(str(leitura_clientes[0][4]))
    editar.alterarIDADE.setText(str(leitura_clientes[0][3]))
    editar.alterarSituacao.setText(str(leitura_clientes[0][5]))

def alteracao_de_dados():
    global numero_ID_geral
    id = editar.alterarID.text()
    nome = editar.alterarNOME.text()
    cpf = editar.alterarCPF.text()
    idade = editar.alterarIDADE.text()
    renda = editar.alterarRendaBruta.text()
    situacao = editar.alterarSituacao.text()

    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET id = '{}', nome = '{}', cpf = '{}', idade = '{}', renda = '{}', situacao = '{}' WHERE id = {}"
    .format(id, nome, cpf, idade, renda, situacao, numero_ID_geral))
    
    editar.close()
    relatorio.close()
    cadastro.show()
    conexao.commit()

def excluir_dados():
    excluir = relatorio.tabelaClientes.currentRow()
    relatorio.tabelaClientes.removeRow(excluir)

    if excluir == -1:  # Nenhuma linha selecionada
        print("Nenhum cliente selecionado.")
        relatorio.mensagemErro.setText("Nenhum cliente selecionado.")  # Supondo que tenha um QLabel para mensagens
        return

    cursor = conexao.cursor()
    cursor.execute('SELECT id FROM clientes')
    leitura_clientes = cursor.fetchall()

    if not leitura_clientes or excluir >= len(leitura_clientes):  # Verifica se há registros e se o índice é válido
        print("Erro ao buscar cliente. Nenhum cliente encontrado com esse índice.")
        relatorio.mensagemErro.setText("Erro ao buscar cliente.")
        return

    id_ativo = leitura_clientes[excluir][0]

    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_ativo,))
    conexao.commit()


# Configurar a aplicação PyQt5
app = QtWidgets.QApplication([])
cadastro = uic.loadUi('cadastro.ui')

# Conectar os botões aos métodos
cadastro.salvar.clicked.connect(inserir_dados)
cadastro.pre_analize.clicked.connect(analise)
cadastro.relatorio.clicked.connect(relatorio)

relatorio = uic.loadUi('relatorio.ui')
relatorio.Editar.clicked.connect(editar_dados)
relatorio.Excluir.clicked.connect(excluir_dados)


editar = uic.loadUi('editar.ui') 
editar.btnalterar.clicked.connect(alteracao_de_dados)


# Exibir a interface
cadastro.show()
app.exec()