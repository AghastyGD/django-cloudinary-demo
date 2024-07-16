# Projeto de Demonstração para Integração de Django e Cloudinary

## Instalação e Configuração

1. Clone este repositório.
2. Crie um ambiente virtual e ative-o.
3. Instale as dependências usando `pip install -r requirements.txt`.
4. Crie um arquivo  **.env** no diretorio root do seu projeto com as seguintes variaveis:
```makefiles
CLOUD_NAME=seu cloud_name
CLOUD_API_KEY=sua api_key
CLOUD_SECRET_KEY=sua secret_key
```
5. Execute as migrações: `python manage.py makemigrations`, `python manage.py migrate`.
6. Crie um superusuário para acesso ao painel de administração: `python manage.py createsuperuser`.
7. Inicie o servidor de desenvolvimento: `python manage.py runserver`.

Veja o [tutorial](https://dev.to/aghastygd/integracao-do-cloudinary-ao-seu-projeto-django-gratuitamente-8pm) e aprenda como obter suas credencias de API na plataforma Cloudinary.

## Enjoy! ❤️
