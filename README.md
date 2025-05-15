
# Проект Sprint_6: Автотесты для сервиса аренды самокатов

## Описание
Проект содержит автотесты для проверки:
1. Раздела FAQ (8 ключевых вопросов)
2. Полного цикла оформления заказа через верхнюю и нижнюю кнопки
3. Переходов по логотипам системы

## Технологии
- **Python 3.7+**
- **Selenium 4+**
- **Pytest**
- **Allure Framework**
- **Page Object Pattern**

## Структура проекта
Sprint_6/
├── .gitignore
├── conftest.py
├── curl.py
├── data_generator.py
├── data.py
├── README.md
├── requirements.txt
├── locators/
│ ├── init.py
│ ├── faq_page_locators.py
│ └── order_page_locators.py
├── pages/
│ ├── init.py
│ ├── faq_page.py
│ ├── main_page.py
│ └── order_page.py
└── test/
├── init.py
├── test_faq.py
└── test_order_flow.py

## Установка
1. Клонируйте репозиторий
2. Установите зависимости:
```bash
pip install -r requirements.txt

Запуск тестов
# Все тесты с генерацией Allure-отчета
pytest --alluredir=allure-results

# Только тесты FAQ
pytest -k TestFAQ

# Только тесты оформления заказа
pytest -k TestFullOrderFlow

# Только тесты переходов по логотипам
pytest -k TestTrafficFromClick

Особенности реализации
1. Тесты FAQ (test_faq.py)
Параметризованная проверка 8 вопросов

Динамические названия тестов

Прикрепление сравнения ответов в отчет

2. Тесты оформления заказа (test_order_flow.py)
Два сценария оформления:

Через верхнюю кнопку

Через нижнюю кнопку (со скроллом)

Поддержка разных наборов данных

Проверка модальных окон

Работа с несколькими вкладками

3. Тесты переходов по логотипам: (test_click_on_the_logo.py)
Тест перехода на главную страницу п клику на логотип Самоката.
Тест при нажатии на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.

Генерация отчетов
Соберите результаты тестов:
allure generate allure-results -o allure-report --clean
Откройте отчет:
allure open allure-report