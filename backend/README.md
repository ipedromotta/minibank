# ⚙️ Configuração do projeto #
## 🐳 Execução em docker
1. Construir e subir os containers

    No terminal, dentro da pasta do backend, rode:
    ```
    docker-compose -f docker-compose.prod.yml up --build
    ```
    Esse comando vai:

    - Construir a imagem Docker com base no seu Dockerfile.

    - Criar e iniciar os containers do Django (Gunicorn) e do Nginx.

    - O Nginx vai ficar escutando na porta 80 da sua máquina.

2. Acessar a aplicação

    Abra seu navegador e acesse 🔗 http://localhost/

    Se tudo estiver correto, você verá a API rodando via Docker.

*Nota: Certifique-se de ter o Docker e o Docker Compose instalados na sua máquina.

## 🖥️ Execução local
Para iniciar o backend localmente, siga os passos abaixo:

1. Ativar o ambiente virtual com Pipenv

    Se você ainda não possui o Pipenv instalado, instale-o com o comando:
    ```
    pip install pipenv
    ```
    Em seguida, navegue até o diretório backend do projeto e ative o ambiente virtual:
    ```
    cd backend
    pipenv shell
    ```
2. Instalar as dependências

    Com o ambiente virtual ativado, instale as dependências (incluindo as de desenvolvimento):
    ```
    pipenv install --dev
    ```
3. Configurar o projeto Django

    Crie as migrações do banco de dados com:
    ```
    python manage.py makemigrations
    ```
    Aplique as migrações para criar as tabelas no banco:
    ```
    python manage.py migrate
    ```
4. Subir o servidor local

    Agora que tudo está configurado, inicie o servidor com:
    ```
    python manage.py runserver
    ```

A API estará disponível em:
🔗 http://localhost:8000/api/v1/
