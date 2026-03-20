# Django Brain.com.ua Parser

# Створена вітка bodya де виконано поставлену задачу

---

Тестове завдання: Парсер мобільного телефону Apple iPhone 16 Pro Max з сайту Brain.com.ua, збереження даних у PostgreSQL
та вивантаження у CSV.

## Стек технологій

* **Python 3.x**
* **Django** (ORM & Management Commands)
* **PostgreSQL**
* **BeautifulSoup4 / Requests** (для парсингу)
* **python-dotenv** (для безпеки даних)

## Встановлення та запуск

### 1. Клонування репозиторію

```bash
git clone https://github.com/Bohdan11Dii/RequestDjangoParse
cd DjangoParser

```

### 2. Налаштування віртуального оточення

```

python3 -m venv .venv
source .venv/bin/activate  # Для Linux/macOS
# або
.venv\Scripts\activate     # Для Windows
```

### 3. Встановлення залежностей

```
pip install -r requirements.txt
```

### 4. Налаштування бази даних

```

DB_NAME=your_db_name
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_django_secret_key
DEBUG=True
```

### 5. Міграції бази даних

```

python manage.py migrate
```

# Використання

### 1. Парсинг даних

Команда збирає інформацію про товар за посиланням і зберігає її в БД:

```
python manage.py fetch_brain_product
```

### 2. Експорт у CSV

Команда вивантажує всі збережені товари з бази даних у файл products.csv:

```
python manage.py export_products_csv
```

# Структура проекту
1. **parser/utils.py** — логіка скрапінгу (класи ParserUtils та BrainMobileParse).

2. **parser/models.py** — модель Parser для збереження даних у Postgres.

3. **parser/management/commands/** — кастомні команди Django для автоматизації задач