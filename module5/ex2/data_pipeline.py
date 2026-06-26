from abc import ABC, abstractmethod
from typing import Protocol, Any


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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

    def output(self, nb: int) -> list[tuple[int, str]]:
        result = []
        for _ in range(nb):
            if not self._stg:
                break
            result.append(self._stg.pop(0))
        return result


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
                    "DataStream error - Can't process element in stream: "
                    f"{item}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data = processor.output(nb)
            if data:
                plugin.process_output(data)

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            remaining = len(proc._stg)

            name = (
                proc.__class__.__name__
                .replace("Processor", " Processor")
            )

            print(
                f"{name}: total {proc._k} items processed, "
                f"remaining {remaining} on processor"
            )


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")

        items = []

        for idx, value in data:
            items.append(f'"item_{idx}": "{value}"')

        print("{" + ", ".join(items) + "}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    stream = DataStream()

    print("Initialize Data Stream...\n")
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    data1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"Send first batch of data on stream: {data1}")
    stream.process_stream(data1)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    data2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print(f"\nSend another batch of data: {data2}")
    stream.process_stream(data2)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
