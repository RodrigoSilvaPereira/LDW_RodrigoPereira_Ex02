# Loja de Suplementos

Este projeto é uma aplicação web desenvolvida com **Flask**, simulando uma loja de suplementos. A aplicação permite gerenciar um cadastro de suplementos com as funcionalidades básicas de um CRUD (Criar, Ler, Atualizar e Deletar), exibindo informações como título, ano de lançamento, categoria e descrição de cada suplemento. O projeto inclui uma interface simples com paginação, além de botões de ação (Editar e Excluir) estilizados para melhor experiência do usuário.

## Funcionalidades
- **Listagem de suplementos** com paginação para facilitar a navegação.
- **Adição de novos suplementos** através de um formulário intuitivo.
- **Edição e exclusão de suplementos** com botões estilizados e confirmação de exclusão.
- **Validação de dados** no formulário de cadastro e edição.

## Tecnologias Utilizadas
- **Python** e **Flask** para o desenvolvimento da aplicação backend.
- **HTML**, **CSS** e **Jinja2** para renderização de templates no frontend.
- **SQLite** (ou outro banco de dados) para armazenamento dos dados.
- **Bootstrap** para melhorar o design responsivo (opcional).
  
## Como Executar o Projeto

1. Clone o repositório para a sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/loja-de-suplementos.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd loja-de-suplementos
    ```

3. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

4. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute a aplicação:
    ```bash
    flask run
    ```

6. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:5000/
    ```

## Estrutura do Projeto

```bash
.
├── app.py                 # Arquivo principal da aplicação Flask
├── templates/             # Templates HTML usando Jinja2
│   ├── layout.html        # Layout base
│   ├── index.html         # Página de listagem de suplementos
│   ├── form.html          # Formulário de adição/edição de suplementos
├── static/                # Arquivos estáticos (CSS, JS, imagens)
│   └── style.css          # Arquivo de estilo CSS
├── models.py              # Definição do banco de dados e classes
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto

```

Esse arquivo `README.md` fornece todas as informações necessárias para outros desenvolvedores entenderem o projeto e como executá-lo.
