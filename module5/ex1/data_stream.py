from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._stg: list[tuple[int, str]] = []
        self._k: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._stg:
            raise IndexError("No data stored.")
        return self._stg.pop(0)


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
                self._k += 1
                self._stg.append((self._k, str(item)))
        else:
            self._k += 1
            self._stg.append((self._k, str(data)))


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
                self._k += 1
                self._stg.append((self._k, item))
        else:
            self._k += 1
            self._stg.append((self._k, data))


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
                self._k += 1
                log_str = f"{item['log_level']}: {item['log_message']}"
                self._stg.append((self._k, log_str))
        else:
            self._k += 1
            log_str = f"{data['log_level']}: {data['log_message']}"
            self._stg.append((self._k, log_str))


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            found = False

            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    found = True
                    break

            if not found:
                print(
                    f"DataStream error - Can't process element in stream: "
                    f"{item}"
                )

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            remaining = len(proc._stg)
            print(
                f"{proc.__class__.__name__}: "
                f"total {proc._k} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:

    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")

    stream = DataStream()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    stream.register_processor(NumericProcessor())

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print("\nSend first batch of data on stream:", batch)

    stream.process_stream(batch)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print("\nSend the same batch again")

    stream.process_stream(batch)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        stream.processors[0].output()

    for _ in range(2):
        stream.processors[1].output()

    stream.processors[2].output()

    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
