from datetime import datetime


class SpeedTestResult:

    def __init__(self, mode, download_speed, upload_speed, latency, execution_time):
        self.mode = mode
        self.download_speed = download_speed
        self.upload_speed = upload_speed
        self.latency = latency
        self.execution_time = execution_time
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_tuple(self):
        return (
            self.mode,
            self.download_speed,
            self.upload_speed,
            self.latency,
            self.execution_time,
            self.timestamp
        )

    def __str__(self):
        return (
            "\n===== Speed Test Result =====\n"
            f"Mode           : {self.mode}\n"
            f"Download Speed : {self.download_speed:.2f} Mbps\n"
            f"Upload Speed   : {self.upload_speed:.2f} Mbps\n"
            f"Latency        : {self.latency:.2f} ms\n"
            f"Execution Time : {self.execution_time:.2f} sec\n"
            f"Timestamp      : {self.timestamp}\n"
        )
