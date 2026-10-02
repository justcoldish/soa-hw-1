# Деплой

Из корня репозитория:

```
docker compose up --build -d
```

Проверка:

```
docker compose ps -a
curl -i localhost:8000/health
```

Ожидаемый вывод:

```
NAME                IMAGE             COMMAND                  SERVICE   CREATED          STATUS         PORTS
soa-hw-1-orders-1   soa-hw-1-orders   "uvicorn main:app --…"   orders    10 seconds ago   Up 9 seconds   0.0.0.0:8000->8000/tcp

HTTP/1.1 200 OK

{"status":"ok"}
```

Остановка:

```
docker compose down
```
