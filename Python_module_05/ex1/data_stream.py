"""
Docstring for ex1.data_stream
"""
from abc import abstractmethod, ABC
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str):
        """
        Sets up the stream with an ID.
        """
        self.stream_id = stream_id
        self.items_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a group of data.
        """
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """
        Keeps only the data we need.
        """
        if criteria is None:
            return data_batch
        return [item for item in data_batch]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Returns the stream ID and count.
        """
        return {
            "stream_id": self.stream_id,
            "processed_count": self.items_processed
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Calculates the average of numbers.
        """
        try:
            valid_readings = [
                x for x in data_batch
                if isinstance(x, (int, float))
            ]
            count = 0
            for _ in valid_readings:
                count += 1
            if count == 0:
                return "Sensor analysis: No valid numeric data found."
            total_val = 0
            for val in valid_readings:
                total_val += val

            avg = total_val / count
            self.items_processed += count

            return (
                f"Sensor analysis: {count} readings processed, "
                f"avg temp: {avg:.2f}°C"
            )
        except Exception as e:
            return f"Error processing sensor batch: {e}"


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Calculates the sum of money.
        """
        try:
            valid_transactions = [
                x for x in data_batch
                if isinstance(x, (int, float))
            ]
            count = 0
            for _ in valid_transactions:
                count += 1
            if count == 0:
                return "Transaction analysis: No valid financial data found."
            net_flow = 0

            for val in valid_transactions:
                net_flow += val

            flow_sign = "+" if net_flow >= 0 else ""
            self.items_processed += count

            return (
                f"Transaction analysis: {count} operations, "
                f"net flow: {flow_sign}{net_flow} units"
            )
        except Exception as e:
            return f"Error processing transaction batch: {e}"


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Counts the errors in text.
        """
        try:
            valid_events = [
                x for x in data_batch
                if isinstance(x, str)
            ]

            if not valid_events:
                return "Event analysis: No valid text data found."

            error_count = 0
            count = 0

            for event in valid_events:
                if (
                    "ERROR" in event or
                    "error" in event or
                    "Error" in event
                ):
                    error_count += 1
                count += 1

            self.items_processed += count
            return (
                f"Event analysis: {len(valid_events)} events, "
                f"{error_count} error(s) detected"
            )

        except Exception as e:
            return f"Error processing event batch: {e}"


def main():
    """
    Runs the main program.
    """
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")

    print("Initializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")

    sensor_data = [22.5, 24.1, "invalid", 21.8, 23.0]
    trans_data = [100, -50, "error_log", 200, -30, 75]
    event_data = [
        "User Login",
        "ERROR: DB Timeout",
        404,
        "User Logout",
        "ERROR: Connection lost"
    ]

    streams = [sensor, trans, event]
    inputs = [sensor_data, trans_data, event_data]

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    index = 0
    for stream in streams:
        data = inputs[index]

        print(f"\nBatch {index + 1} Results (ID: {stream.stream_id}):")
        result = stream.process_batch(data)
        print(f"- {result}")
        stats = stream.get_stats()
        print(f"  Stats: {stats}")
        index += 1

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
