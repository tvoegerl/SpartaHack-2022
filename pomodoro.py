from flask import Flask, render_template, url_for, request
import time

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        time_wanted = request.form.get("times")
        time_secs = int(time_wanted) * 60
        for i in range(0, time_secs):
            mins = (time_secs-i)/60
            secs = (time_secs-i)%60
            return render_template('timer.html', mins = str(mins), secs = str(secs))
            time.sleep(1)
    else:
        return render_template('index.html')
    


if __name__ == "__main__":
    app.run(debug = True)