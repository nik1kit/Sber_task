# Задание для практики в Сбербанке 

## Описание проекта

Данный проект предназначен для парсинга информации об арбитражных делах за июнь 2024 года с сайта [kad.arbitr.ru](https://kad.arbitr.ru). Программа собирает следующие данные о каждом деле:  
- Номер дела  
- Дата дела  
- Суд  
- Истец (ИНН, название)  
- Ответчик (ИНН, название)  
- Суть/тема дела  
- Третьи лица (ИНН, название)  
- Иные лица (ИНН, название)  

## Технические детали

Проект написан на языке Python и использует следующие библиотеки:  
- `selenium` для автоматизации работы с браузером и получения HTML-кода страниц  
- `beautifulsoup4` для парсинга HTML-кода  
- `openpyxl` для сохранения данных в формате Excel  
- `fake_useragent` для генерации случайных User-Agent

- `requirements.txt` все используемые версии библиотек 
