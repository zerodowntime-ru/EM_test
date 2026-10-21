# Тестовое задание на позицию DevOps (Effective Mobile)
В данном репозитории реализовано развертывание простого веб-приложения, доступного через Nginx в Docker-контейнерах. [GitHub](https://github.com/zerodowntime-ru/EM_test "Перейти в репозиторий")

### Технологический стек

- Backend: Python (http.server).
- Reverse Proxy: Nginx.
- Orchestration: Docker & Docker Compose.

### Архитектура (nginx → backend)
```
[ Пользователь ]
         │
         ▼ (Порт 80)
┌──────────────────────┐
│    Nginx (Proxy)     │
└────────┬─────────────┘
         │ (Docker network)
         ▼ (Порт 8080)
┌──────────────────────┐
│   Backend (Python)   │
└──────────────────────┘
```
### Запуск проекта

1) Клонировать репозиторий
```bash
git clone https://github.com/zerodowntime-ru/EM_test.git
cd EM_test
```
2) Запустить Docker Compose:
```bash
docker-compose up -d --build
```
Проверка работоспособности
```bash
curl http://localhost
```
*Ожидаемый ответ:*
Hello from Effective Mobile!