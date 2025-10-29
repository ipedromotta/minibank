FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./

ENV BASE_URL=http://localhost

# Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential libpq-dev

RUN pip install --upgrade pip && pip install uv

# Instala dependências diretamente no sistema (sem venv)
RUN uv pip install --system -r requirements.txt

COPY . .

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Executa o servidor
CMD ["gunicorn", "configs.wsgi:application", "--bind", "0.0.0.0:8000"]
