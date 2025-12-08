# Scrapy Parser PEP  
Парсер для автоматического сбора информации о всех PEP (Python Enhancement Proposals) с официального сайта python.org.

## Автор

**GitHub:** [eqsx000111](https://github.com/eqsx000111)
**Email:** [deddotu@yandex.ru](mailto:deddotu@yandex.ru)  
**ФИО:** Ильницкий Иван Александрович 


---

## Описание проекта

Этот проект — Scrapy-парсер, который собирает информацию с сайта PEP:

1. **Полный список PEP**  
   - Номер  
   - Название  
   - Статус  

2. **Сводку по статусам**  
   - Статус  
   - Количество документов в этом статусе  
   - Итоговое количество всех PEP  

По итогам парсинга формируется **два CSV-файла**:  
- `pep_<timestamp>.csv` — полный список всех PEP (генерируется Scrapy FEEDS).  
- `status_summary_<timestamp>.csv` — отчёт по статусам (генерируется pipeline).

---

## Стек технологий

- **Python 3.10+**
- **Scrapy**
- **CSV**
- Проект разделён на:
  - Spider
  - Item'ы
  - Pipelines
  - Settings

---

## Как запустить проект 

### 1. Клонировать репозиторий 

 

```bash 

git clone https://github.com/eqsx000111/scrapy_parser_pep-main.git 

cd scrapy_parser_pep-main

``` 

 

### 2. Создать и активировать виртуальное окружение 

 

```bash 

python3 -m venv venv 

``` 

 

Для Linux/macOS: 

 

```bash 

source venv/bin/activate 

``` 

 

Для Windows: 

 

```bash 

venv\Scripts\activate 

``` 

 

### 3. Установить зависимости 

 

```bash 

python3 -m pip install --upgrade pip 

pip install -r requirements.txt 

``` 
### 4. Запуск парсера 
```bash
scrapy crawl pep
```

## Структура проекта
```
scrapy_parser_pep/
│
├── pep_parse/
│ ├── spiders/
│ │ └── pep.py
│ ├── pipelines.py
│ ├── items.py
│ ├── settings.py
│ ├── constants.py
│ ├── middlewares.py
│
├── tests
├── results/ # сюда сохраняются сводки
├── LICENSE
├── requirements.txt
├── scrapy.cfg
└── README.md
```