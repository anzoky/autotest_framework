## Описание
Этот проект представляет собой набор **UI-автотестов** для тестирования функционала сайта [DemoQA](https://demoqa.com/).  
Тесты написаны с использованием **Python + Selenium + Pytest**, а результаты оформлены в **Allure-отчётах**.

## Технологии
- **Python** – язык программирования
- **Selenium WebDriver** – взаимодействие с браузером
- **Pytest** – тестовый фреймворк
- **Allure** – генерация отчётов
- **pytest-xdist** – параллельный запуск тестов

- ## Как запустить проект?
1. **Установите зависимости:**  
   ```bash
   pip install -r requirements.txt

2. **Запустите тесты:**
    ```bash
    pytest --alluredir=allure-results

3. **Сгенерируйте и откройте Allure-отчёт:**
    ```bash
   allure serve allure-results

**Аллюр отчет**
![Allure Report](https://github.com/anzoky/autotest_framework/issues/2#issue-2910433798)
