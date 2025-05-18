# Help 5 Letters / Помощь 5 Букв

## О проекте / About the Project

Этот скрипт помогает находить слова из 5 букв для игр типа Wordle, используя заданные условия:  
- буквы, которых нет в слове  
- буквы, которые есть в слове  
- шаблон слова с пропусками  

This script helps find 5-letter words for games like Wordle based on given criteria:  
- letters not in the word  
- letters that are in the word  
- word pattern with blanks  

## Структура проекта / Project Structure

- `help_5letters.py` — основной скрипт / main script  
- `words.py` — список слов из 1993 пятибуквенных слов / list of 1993 five-letter words  
- `README.md` — это описание / this description file  

## Зависимости / Requirements

Проект использует только встроенные библиотеки Python и не требует внешних пакетов.

This project uses only built-in Python libraries and requires no external packages.

Используемые модули / Modules used:  
- `re` — регулярные выражения / regular expressions  
- `random` — случайный выбор (если понадобится) / random selections (if needed)  
- `pathlib`, `json` — для возможных расширений / for potential extensions  

## Как использовать / How to Use

1. Запустите скрипт `help_5letters.py`  
2. Введите буквы, которых нет в слове, через пробел  
3. Введите буквы, которые есть в слове, через пробел  
4. Введите шаблон слова с подчёркиваниями вместо неизвестных букв (например, `па__р`)  

1. Run the script `help_5letters.py`  
2. Enter letters NOT in the word, separated by spaces  
3. Enter letters IN the word, separated by spaces  
4. Enter the word pattern with underscores for unknown letters (e.g., `pa__r`)  

---

Если хочешь, могу помочь оформить коммит и пуш этого файла на GitHub.
