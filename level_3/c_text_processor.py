"""У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    """Класс для логики работы обработки сообщений."""
    def __init__(self, text: str) -> None:
        """Инициализатор класса TextProcessor."""
        self.text = text

    def to_upper(self) -> str:
        """Возвращает строку в верхнем регистре."""
        return self.text.upper()

    def summarize(self) -> str:
        """Возвращает кол-во символов в строке."""
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    """Класс для умной логики работы обработки сообщений."""
    def summarize(self) -> str:
        """Возвращает кол-во символов и кол-во слов в строке."""
        return f'Total text length: {len(self.text)}, total number of words in the text: {len(self.text.split())}.'


if __name__ == '__main__':
    # экземпляр первого класса
    text_processor = TextProcessor("Hello world example")

    print(text_processor.to_upper())
    print(text_processor.summarize())

    # экземпляр второго класса
    advanced_text_processor = AdvancedTextProcessor("Hello world example")

    print(advanced_text_processor.to_upper())
    print(advanced_text_processor.summarize())
