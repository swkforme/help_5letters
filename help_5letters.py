# Помощник в игре "5 букв" (аналог Wordle, Тинькофф и др.)
import re
from words import words


def find_words_by_pattern(pattern, word_list):
    # Заменяет _ на . и ищет совпадения по позиции
    regex = re.compile(f"^{pattern.replace('_', '.')}$")
    return [word for word in word_list if regex.match(word)]


def main():
    no_letters = input("Буквы, которых нет в слове (через пробел): ").lower().split()
    white = (
        input("Буквы, которые точно есть (любая позиция, через пробел): ")
        .lower()
        .split()
    )
    yellow = input("Маска (например, ва__с, если известны позиции): ").lower()

    # Отбираем слова по условиям
    filtered = [w for w in words if all(l in w for l in white)]
    filtered = [w for w in filtered if not any(l in w for l in no_letters)]
    result = find_words_by_pattern(yellow, filtered)

    if result:
        print("Подходящие слова:")
        print(*result, sep=", ")
    else:
        print("Ничего не найдено. Вот что осталось после фильтрации:")
        print(*filtered, sep=", ")


if __name__ == "__main__":
    main()
