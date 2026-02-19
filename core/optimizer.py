import speedtest
import time


class SpeedTestService:

    def run_test(self, optimized=True):
        """
        Runs internet speed test.
        optimized=True  -> Uses best server (faster)
        optimized=False -> Fetches all servers first (slower)
        """

        start_time = time.time()

        try:
            st = speedtest.Speedtest()

            if optimized:
                # Optimized: Select best server directly
                st.get_best_server()
            else:
                # Naive: Get all servers first (takes more time)
                st.get_servers()
                st.get_best_server()

            download_speed = round(st.download() / 1_000_000, 2)
            upload_speed = round(st.upload() / 1_000_000, 2)
            latency = round(st.results.ping, 2)

            execution_time = round(time.time() - start_time, 2)

            return {
                "mode": "Optimized" if optimized else "Naive",
                "download_speed": download_speed,
                "upload_speed": upload_speed,
                "latency": latency,
                "execution_time": execution_time
            }

        except Exception as e:
            return {
                "mode": "Optimized" if optimized else "Naive",
                "download_speed": 0,
                "upload_speed": 0,
                "latency": 0,
                "execution_time": 0,
                "error": str(e)
            }
