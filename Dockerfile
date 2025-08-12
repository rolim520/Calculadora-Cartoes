# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de dependências e instale-as
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do projeto para o diretório de trabalho
COPY . .

# Exponha a porta que o Flask usará
EXPOSE 5000

# O comando para iniciar a aplicação quando o contêiner rodar
CMD ["python", "app.py"]
