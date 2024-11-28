FROM 0xwen/explorer-app:v1.0

WORKDIR /app

COPY . .

CMD ["sh", "-c", "python3 main.py && tail -f /dev/null"]