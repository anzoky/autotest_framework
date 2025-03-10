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
![Allure Report](https://private-user-images.githubusercontent.com/158040655/420249073-93e426be-3179-4fc9-ae38-509142f84d4d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE1OTA3ODgsIm5iZiI6MTc0MTU5MDQ4OCwicGF0aCI6Ii8xNTgwNDA2NTUvNDIwMjQ5MDczLTkzZTQyNmJlLTMxNzktNGZjOS1hZTM4LTUwOTE0MmY4NGQ0ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMxMFQwNzA4MDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xZjRmODNkMzVjNzEwMDFkYWJiMTg3NzkwY2U1MzUxODIzN2QwNTI1ZmMyYjU5NDAyMjdiNWMzYjRiNzM2YjFkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.6poUI9mGLghLiaHKlTirtiPIS6MaWfHqIht4nXT81jE)
