"""
This module processes numbers, text, and logs using polymorphic classes.
"""
from abc import abstractmethod, ABC
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Docstring for process

        :param self: Description
        :param data: Description
        :type data: any
        """

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Docstring for validate

        :param self: Description
        :param data: Description
        :type data: any
        :return: Description
        :rtype: bool
        """

    def format_output(self, result: str) -> str:
        """
        Docstring for format_output

        :param self: Description
        :param result: Description
        :type result: str
        :return: Description
        :rtype: str
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """
        We check that can we add empty string to
        our data? If we could it means it's not a
        number and we should return False.
        Also we check do we have a list of numbers?
        or it's just we have a number!

        :param self: Description
        :param data: Description
        """
        try:
            try:
                _ = data + ""
                return False
            except TypeError:
                pass

            for item in data:
                _ = item + 0
            return True
        except TypeError:
            return False
        except Exception:
            return False

    def process(self, data: Any) -> str:
        """
        Docstring for process

        :param self: Description
        :param data: Description
        """
        if not self.validate(data):
            print("Error: invalid data!")
            return ""
        total = 0.0
        count = 0
        for d in data:
            total += d
            count += 1
        avg = 0.0
        if count > 0:
            avg = total / count
        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """
        We check that the data is str or not by
        by adding empty string to it.

        :param self: Description
        :param data: Description
        """
        try:
            _ = data + ""
            print("Validation: Text data verified")
            return True
        except TypeError:
            return False

    def process(self, data: Any) -> str:
        """
        After valiading the data we loop
        through the data

        :param self: Description
        :param data: Description
        """
        if not self.validate(data):
            return "Error: Invalid data"

        char_num = 0
        for char in data:
            char_num += 1

        words_list = data.split()
        word_count = 0
        for w in words_list:
            word_count += 1
        return f"Processed text: {char_num} characters, {word_count} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """
        same as validate function in text_processor

        :param self: Description
        :param data: Description
        :type data: any
        :return: Description
        :rtype: bool
        """
        try:
            _ = data + ""
            print("Validation: Log entry verified")
            return True
        except TypeError:
            return False

    def process(self, data: Any) -> str:
        """
        After validation we check that do we have
        Error in our log or not!
        """
        if not self.validate(data):
            return "Error: Invalid data"

        if "ERROR" in data:
            return f"ERROR level detected: {data.split(': ')[-1]}"
        else:
            return f"INFO level detected: {data}"

    def format_output(self, result: str) -> str:
        """
        We override this function to printing the log to output

        :param self: Description
        :param result: Description
        :type result: str
        :return: Description
        :rtype: str
        """
        if "ERROR" in result:
            return f"[ALERT] {result}"
        return f"[INFO] {result}"


def main():
    """
    Docstring for main
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    data_n = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_n}")
    res_n = num_proc.process(data_n)
    print(num_proc.format_output(res_n))

    print("\nInitializing Text Processor...")
    txt_proc = TextProcessor()
    data_t = "Hello Dark Boring World"
    print(f"Processing data: \"{data_t}\"")
    res_t = txt_proc.process(data_t)
    print(txt_proc.format_output(res_t))

    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    data_l = "ERROR: Connection timeout"
    print(f"Processing data: \"{data_l}\"")
    res_l = log_proc.process(data_l)
    print(log_proc.format_output(res_l))

    # Polymorphism
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [num_proc, txt_proc, log_proc]
    inputs = [[1, 2, 3], "Hello World", "INFO: System ready"]
    i = 1
    index = 0
    for proc in processors:
        current_data = inputs[index]
        result = proc.process(current_data)
        formatted = proc.format_output(result)
        print(f"Result {i}: {formatted}")
        i += 1
        index += 1
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
