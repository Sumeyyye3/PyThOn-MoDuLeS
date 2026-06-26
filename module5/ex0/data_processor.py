from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data stored.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(i, (int, float)) for i in data)
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._counter += 1
                self._storage.append((self._counter, str(item)))
        else:
            self._counter += 1
            self._storage.append((self._counter, str(data)))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._counter += 1
                self._storage.append((self._counter, item))
        else:
            self._counter += 1
            self._storage.append((self._counter, data))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(i, dict) and
                all(isinstance(k, str) and isinstance(v, str)
                    for k, v in i.items())
                for i in data
            )

        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._counter += 1
                log_str = f"{item['log_level']}: {item['log_message']}"
                self._storage.append((self._counter, log_str))
        else:
            self._counter += 1
            log_str = f"{data['log_level']}: {data['log_message']}"
            self._storage.append((self._counter, log_str))


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()

    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")  # type: ignore
    except TypeError as e:
        print(f"Got exception: {e}")

    numeric.ingest([1, 2, 3, 4, 5])

    print("Processing data: [1, 2, 3, 4, 5]")
    print("Extracting 3 values...")

    for i in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {i}: {value}")

    print("\nTesting Text Processor...")
    text = TextProcessor()

    print(f"Trying to validate input '42': {text.validate(42)}")

    text.ingest(["Hello", "Nexus", "World"])

    print("Processing data: ['Hello', 'Nexus', 'World']")
    print("Extracting 1 value...")

    for i in range(1):
        rank, value = text.output()
        print(f"Text value {i}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()

    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]

    print(f"Processing data: {log_data}")

    log.ingest(log_data)

    print("Extracting 2 values...")

    for i in range(2):
        rank, value = log.output()
        print(f"Log entry {i}: {value}")


if __name__ == "__main__":
    main()
