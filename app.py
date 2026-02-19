from flask import Flask, render_template
from service.speed_service import SpeedTestService

app = Flask(__name__)
service = SpeedTestService()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run_test/<mode>")
def run_test(mode):
    optimized = True if mode == "optimized" else False
    result = service.run_test(optimized=optimized)

    return render_template("index.html", result=result)


@app.route("/compare")
def compare():
    naive, optimized, improvement = service.compare_performance()

    return render_template(
        "compare.html",
        compare={
            "naive": naive,
            "optimized": optimized,
            "improvement": improvement
        }
    )


@app.route("/history")
def history():
    records = service.get_test_history()
    return render_template("history.html", records=records)


if __name__ == "__main__":
    print("Starting Internet Speed Tester...")
    app.run(debug=True)
