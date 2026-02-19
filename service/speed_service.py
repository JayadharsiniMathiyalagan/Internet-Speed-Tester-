from core.speed_engine import SpeedTestEngine
from models.result import SpeedTestResult
from data.database import DatabaseManager


class SpeedTestService:

    def __init__(self):
        self.engine = SpeedTestEngine()
        self.database = DatabaseManager()

    def run_test(self, optimized=True):

        result_dict = self.engine.run_test(optimized=optimized)

        result = SpeedTestResult(
            mode=result_dict["mode"],
            download_speed=result_dict["download_speed"],
            upload_speed=result_dict["upload_speed"],
            latency=result_dict["latency"],
            execution_time=result_dict["execution_time"]
        )

        self.database.insert_result(result.to_tuple())

        return result

    def compare_performance(self):
        naive_result = self.run_test(optimized=False)
        optimized_result = self.run_test(optimized=True)

        improvement = round(
            naive_result.execution_time - optimized_result.execution_time, 2
        )

        return naive_result, optimized_result, improvement

    def get_test_history(self):
        return self.database.fetch_all_results()
