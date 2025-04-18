FROM python:3.10-slim-buster

# escolhendo o diretório de trabalho
WORKDIR /app

COPY requirements.txt .

# instalando as dependências
RUN pip install -r requirements.txt

# copiar o resto do código
COPY . .

# escolhendo a porta que o flask vai rodar
EXPOSE 5000

# rodando o flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
