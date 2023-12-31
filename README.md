# Google Sheets для QRKot


# Описание
Обновление для приложения QRKot - добавлена возможность формирования отчёта в гугл-таблице. В ней отображены закрытые проекты, отсортированные по скорости сборасредств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.
 
  
# Установка

1. Клонируйте репозиторий
```
git clone https://github.com/dagedarr/QRkot_spreadsheets.git
```
Если вы не используете Git, то вы можете просто скачать исходный код репозитория в ZIP-архиве и распаковать его на свой компьютер.

2. Создайте виртуальное окружение и активируйте его
```
python -m venv venv
source venv/bin/activate
```
3. Установите зависимости и создайте файл .env
```
pip install -r requirements.txt
```
4. Запустите миграции
```
alembic revision --autogenerate -m "First migration" 
alembic upgrade head 
```
5. Запустите сервер
```
uvicorn app.main:app
```
6. Создайте администратора проекта
Перейдите по адресу http://127.0.0.1:8000/auth/register и передайте
```
{
  "email": "user@example.com",
  "password": "string",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}
```
Далее в менеджере БД (например, DBeaver) и вручную измените значение столбца is_superuser для созданного пользователя.

# Готово!
Вы успешно установили проект благотворительного фонда поддержки котиков и готовы начать его использовать!
Для формирования отчета в гугл таблице зарегистрируйтесь и сделайте POST запрос к эндпоинту http://127.0.0.1:8000/google

# API  
Список доступных эндпоинтов в проекте c примерами запросов, варианты ответов и ошибок приведены в спецификации openapi.json или по адресу http://127.0.0.1:8000/docs
  
