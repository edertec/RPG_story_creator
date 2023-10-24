Sistema de Criação de Histórias para RPG
Descrição
Este projeto é uma aplicação web desenvolvida para auxiliar na criação de histórias para jogos de RPG. Ele permite que os usuários insiram características de personagens como idade, cor da pele, altura, cor dos olhos, peso e outras características para gerar uma história única.

Tecnologias Utilizadas
Back-end: Flask
Front-end: HTML, CSS, JavaScript
Banco de Dados: PostgreSQL
Estrutura do Projeto

- RPG_Story_Creator/
  - app/
    - controllers/
    - models/
    - templates/
    - static/
      - css/
      - js/
  - config/
    - config.py
    - db_config.py
  - migrations/
  - run.py
  - README.md


Descrição dos Diretórios
controllers/: Contém os controladores que manipulam a lógica de negócios e interagem com os modelos.
models/: Contém as classes que representam os modelos de dados.
templates/: Contém os arquivos HTML que são renderizados no lado do cliente.
static/: Contém arquivos estáticos como CSS e JavaScript.
config/: Contém arquivos de configuração, incluindo configurações do Flask e do banco de dados.
migrations/: Contém arquivos de migração do banco de dados.
Configuração do Banco de Dados
Este projeto utiliza o PostgreSQL como sistema de gerenciamento de banco de dados. As configurações do banco de dados estão localizadas em config/db_config.py.

Instalação e Execução
Clone o repositório.
Instale as dependências usando pip install -r requirements.txt.
Configure o banco de dados PostgreSQL e atualize as configurações em config/db_config.py.
Execute as migrações do banco de dados.
Inicie o servidor Flask usando python run.py.


