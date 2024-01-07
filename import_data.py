import csv
from bard.models import Test, Question, Answer  # Замените 'bard' на название вашего Django-приложения, если оно другое

def import_data(csv_filename):
    with open(csv_filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')  # Указываем точку с запятой как разделитель

        for row in reader:
            # Извлекаем данные из CSV
            test_title = row['Test Title']
            question_text = row['Question']
            answers = [row['Answer 1'], row['Answer 2'], row['Answer 3'], row['Answer 4']]
            correct_answer_index = int(row['Correct Answer'].strip()) - 1  # Переводим в индекс списка (начиная с 0)

            # Создаем или получаем объект теста
            test, _ = Test.objects.get_or_create(title=test_title)
            # Создаем объект вопроса
            question = Question.objects.create(text=question_text, test=test)

            # Создаем объекты ответов
            for i, answer_text in enumerate(answers):
                is_correct = (i == correct_answer_index)
                Answer.objects.create(
                    question=question,
                    text=answer_text,
                    is_correct=is_correct
                )

# Вызовите функцию с путем к файлу CSV
import_data('C:/Users/mc02t/Desktop/test2.txt')  # Замените на актуальный путь к файлу
