# Projeto de Questões Sobre o Oceano

## Alunos
- **Lucas Iori** - RM 553183
- **Miguel Tasso** - RM 553009
- **João Victor Flaitt** - RM 553888

## Descrição do Projeto
Este projeto visa criar um sistema de gerenciamento de questões sobre o oceano, com foco em tópicos como pesca ilegal e poluição. O sistema permite a criação, leitura, atualização e exclusão (CRUD) de questões. As questões são armazenadas em um arquivo JSON, permitindo a persistência dos dados entre execuções do programa.

## Funcionalidades
- **Criar Questão**: Permite adicionar uma nova questão ao sistema, especificando título, descrição e categoria.
- **Ler Questões**: Exibe todas as questões armazenadas no sistema.
- **Atualizar Questão**: Permite modificar os detalhes de uma questão existente.
- **Deletar Questão**: Permite remover uma questão do sistema.

## Requisitos
- Python 3.x
- Biblioteca padrão `json` do Python

## Instruções de Uso

1. **Clone o Repositório**
    ```bash
    git clone https://github.com/seu-usuario/projeto-oceano.git
    cd projeto-oceano
    ```

2. **Execute o Script**
    ```bash
    python main.py
    ```

3. **Interaja com o Menu**
    - **Criar nova questão**: Escolha a opção 1 e siga as instruções para inserir o título, descrição e categoria da nova questão.
    - **Ler todas as questões**: Escolha a opção 2 para visualizar todas as questões armazenadas.
    - **Atualizar uma questão**: Escolha a opção 3, selecione o número da questão que deseja atualizar e insira os novos dados.
    - **Deletar uma questão**: Escolha a opção 4 e selecione o número da questão que deseja deletar.
    - **Sair**: Escolha a opção 5 para sair do programa.

## Estrutura do Projeto
- **main.py**: Arquivo principal do projeto que contém todo o código para executar o sistema CRUD.
- **ocean_issues.json**: Arquivo JSON onde as questões são armazenadas. Este arquivo é criado automaticamente na primeira execução do programa.

## Dependências
Não há dependências externas além da biblioteca padrão `json` do Python.

## Informações Adicionais
- O sistema realiza validações para garantir que os campos de título, descrição e categoria não sejam deixados vazios.
- O programa lida com exceções para garantir que entradas inválidas não causem falhas.

## Licença
Este projeto é licenciado sob a MIT License.
