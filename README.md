# Запуск проекта на Docker Compose

## Установка Docker и Docker Compose

Перед запуском проекта убедитесь, что у вас установлены Docker и Docker Compose.

- [Установка Docker](https://docs.docker.com/get-docker/)
- [Установка Docker Compose](https://docs.docker.com/compose/install/)

## Настройка окружения

1. Склонируйте репозиторий:

   ```sh
   git clone https://gitlab.geeks.kg/urfa-med-center/urfa-med.git
   ```
   
2. Создайте файл .env и укажите в нем переменные окружения:
   ```sh
   cp .env.example .env
   ```

3. Для сборки Docker образов выполните:
   ```sh
   make docker_build
   ```
   
4. Для запуска сервера выполните:
   ```sh
   make docker_server
   ```
   
5. Для выполнения миграций базы данных выполните:
   ```sh
   make docker_migrate
   ```

6. Для создания суперпользователя выполните:
   ```sh
   make docker_createsuperuser
   ```
Сервер будет доступен по адресу http://localhost:8000/



