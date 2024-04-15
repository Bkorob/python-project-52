### Hexlet tests and linter status:
[![Actions Status](https://github.com/Bkorob/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Bkorob/python-project-52/actions)
<a href="https://codeclimate.com/github/Bkorob/python-project-52/maintainability"><img src="https://api.codeclimate.com/v1/badges/ed5e835b9e6ff314af61/maintainability" /></a>
[![Test Coverage](https://api.codeclimate.com/v1/badges/ed5e835b9e6ff314af61/test_coverage)](https://codeclimate.com/github/Bkorob/python-project-52/test_coverage)
[![run linter](https://github.com/Bkorob/python-project-52/actions/workflows/get-linter.yml/badge.svg)](https://github.com/Bkorob/python-project-52/actions/workflows/get-linter.yml)
# Task Manager
Task Manager – система управления задачами, подобная http://www.redmine.org/. Она позволяет ставить задачи, назначать исполнителей и менять их статусы. Для работы с системой требуется регистрация и аутентификация:

## Демонстрация
Проект доступен по [адресу]()

## Установка

**Выполните следующие команды в вашем терминале:**
```
git clone https://github.com/Bkorob/python-project-52
cd python-project-52
make install
make migrate
make start
```
**Приложение будет доступно по адресу:**

http://127.0.0.1:8000


### Переменные среды

Так же, вам потребуется создать файл ```.env```, либо скачать и переменовать имеющийся в проекте 
```.example_env``` 
Для настройки приложения можно установить следующие переменные среды:

*DATABASE_URL*: URL-адрес подключения к базе данных.
**(можно оставить пустым)**
*SECRET_KEY*: Секретный ключ Django.
*ROLLBAR*: токен доступа к Rollbar.

```
# Пример  .env файла
DATABASE_URL=your_database_connection_url
SECRET_KEY=your_django_secret_key
ROLLBAR=your_rollbar_access_token
```