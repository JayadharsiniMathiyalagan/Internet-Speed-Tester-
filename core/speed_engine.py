import time
import speedtest


class SpeedTestEngine:
    """
    Core engine for real internet speed testing.
    """

    def run_test(self, optimized=True):
        start_time = time.time()

        try:
            st = speedtest.Speedtest()

            if optimized:
                st.get_best_server()
            else:
                st.get_servers()
                st.get_best_server()

            download_speed = st.download() / 1_000_000
            upload_speed = st.upload() / 1_000_000
            latency = st.results.ping

            execution_time = round(time.time() - start_time, 2)

            return {
                "mode": "Optimized" if optimized else "Naive",
                "download_speed": round(download_speed, 2),
                "upload_speed": round(upload_speed, 2),
                "latency": round(latency, 2),
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
