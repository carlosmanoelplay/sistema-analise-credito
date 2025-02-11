# Sistema de Análise de Crédito

## Descrição

Este projeto é um **sistema de cadastro de clientes** com uma funcionalidade de **análise de crédito**, onde você pode inserir, visualizar, editar e excluir dados de clientes. Ele também calcula automaticamente a situação do crédito com base na renda e idade do cliente.

A interface gráfica foi desenvolvida utilizando **PyQt5**, e os dados são armazenados em um **banco de dados MySQL**.

## Funcionalidades

- Cadastro de clientes com campos de **nome, CPF, renda, idade** e **situação de crédito**.
- **Análise de crédito automática** com base em renda e idade.
- **Relatório** com todos os clientes cadastrados.
- Funcionalidade de **editar** e **excluir** registros de clientes.
  
## Tecnologias Utilizadas

- **PyQt5**: Interface gráfica do usuário.
- **MySQL**: Banco de dados para armazenamento de informações.
- **Python 3.x**: Linguagem de programação.

## Como Instalar e Rodar

### Pré-requisitos

1. **Python 3.x**: Se você ainda não tem o Python instalado, [baixe e instale](https://www.python.org/downloads/).
2. **MySQL Server**: Para o banco de dados. Você pode [baixar e instalar o MySQL](https://dev.mysql.com/downloads/installer/).
3. **Instalar dependências**:
   
   Abra o terminal ou prompt de comando e execute:
   ```bash
   pip install mysql-connector-python
   pip install pyqt5



Crie um banco de dados no MySQL com o nome lcxSpoting_creditos. Você pode fazer isso diretamente no MySQL ou utilizando um cliente como o MySQL Workbench .

Execute o seguinte comando SQL para criar a tabela necessária:

SQL->
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    cpf VARCHAR(20),
    idade INT,
    renda DECIMAL(10,2),
    situacao VARCHAR(50)
);
Como Rodar o Projeto
Abra o arquivo principal do projeto .

Execute main.pypara iniciar o sistema.
Caso o arquivo cadastro.ui, relatorio.ui, ou editar.uinão seja encontrado, você pode gerar essas interfaces no Qt Designer ou pedir ajuda para criar as mesmas.

Conecte o banco de dados :

Verifique o arquivo main.pye altere as credenciais de acesso ao MySQL conforme sua configuração:
Pitão

Copiar

Editar
conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='seu_usuario',
    password='sua_senha',
    database='lcxSpoting_creditos'
)
Rodando o sistema : Após as configurações, execute o código. Uma interface gráfica aparecerá, permitindo que você cadastre clientes, faça a análise de crédito e visualize os relatórios.

Impressão da Interface Gráfica
Aqui está um exemplo de como a interface gráfica do sistema de cadastro de clientes pode parecer:


Contribuições
Se você quiser contribuir para o projeto, basta fazer um fork , criar um branch para suas alterações e depois criar um pull request .

Licença
Este projeto é de código aberto e pode ser utilizado conforme a Licença MIT .

