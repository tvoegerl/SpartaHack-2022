from flask import Flask, render_template, url_for, request
import time

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    time_wanted = 0
    if request.method == 'POST':
        time_wanted = request.form.get("times")
        sessions_wanted = request.form.get("sessions")
        break_activity = request.form.get("break")
        return render_template('timer.html', time_wanted=time_wanted, sessions_wanted=sessions_wanted)
    else:
        return render_template('index.html')
    


if __name__ == "__main__":
    app.run(use_reloader= True, debug = True)