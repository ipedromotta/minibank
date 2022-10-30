<h1 align="center">
 <img src="https://github.com/ipedromotta/VueJS-Flask/blob/main/frontend/src/assets/logo-python.png" width="50"> <img src="https://github.com/ipedromotta/VueJS-Flask/blob/main/frontend/src/assets/logo.png" width="55"><br>Sistema bancário utilizando Django e VueJS
</h1>

## :page_facing_up: Sobre #
Este sistema possui as funcionalidades de depósito, saque e transferencia de saldo entre as contas criadas. Também é possivel verificar as movimentações no extrato com filtro de data. <br>
O sistema também conta com uma pagina "Minha conta" que possibilita alterar os dados do usuario e excluir a conta

## :wrench: Configuração do projeto #
### Backend
Para a inicialização do backend é necessário ativar o ambiente virtual Pipenv ( Caso não possua basta usar o comando ```pip install pipenv``` )<br>
Dentro do diretório backend utilize o comando a seguir para ativar o ambiente virtual:
```
pipenv shell
```
Após ativar o ambiente virtual, instale as dependencias com o seguinte comando:
```
pipenv install --dev
```
Agora você está com o ambiente virtual ativado e configurado, agora é preciso configurar o projeto django.<br>
Utilize o seguinte comando para criar novas migrações para alterar ou criar a estrutura do banco de dados:
```
python manage.py makemigrations
```
Em seguida, utilize o seguinte comando para criar as tabelas:
```
python manage.py migrate
```
Agora já está tudo configurado, para subir o servidor basta executar o seguinte comando:
```
python manage.py runserver
```
Agora a API já está rodando na porta <a href="http://localhost:8000/api/v1/">http://localhost:8000/api/v1/</a><br>

### Frontend
Para iniciar o frontend também é necessário fazer a instalação das dependências. Dentro do diretório frontend execute o comando:
```
npm install
```
Após a instalação das dependências inicie a aplicação com o comando:
```
npm run dev
```
E a aplicação já estará funcionando na porta <a href="http://localhost:5173/">http://localhost:5173/</a>


## 🛠️ Tecnologias utilizadas #

Para o desenvolvimento desse projeto foram utilizadas as seguintes tecnologias:

* Django;
* VueJS;
* Bootstrap.
