from flask import Flask, render_template, send_file, jsonify
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename
import logging
import os
import json
import time
import sys
import updater
import base64

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Where bundled static/template files live (read-only)
    data_path = os.getcwd()   # Where the EXE was launched — use this for reading/writing JSON files
else:
    base_path = os.path.abspath(".")
    data_path = base_path

updater.checkUpdates()

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

app = Flask(__name__, template_folder=os.path.join(base_path, 'templates'))
socketio = SocketIO(app, async_mode='threading')

# Support for PyInstaller's temp folder
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
    app.template_folder = os.path.join(base_path, 'templates')

#logging.getLogger('werkzeug').setLevel(logging.ERROR)

#os.system("clear")

def getCurRunner():
    with open("runner_data.json", "r") as runnerdatraw:
        runnerdat = json.load(runnerdatraw)
        for runner in runnerdat:
            if runnerdat[runner]["status"] == "running":
                return runner
            
def getNextRunner():
    with open("runner_data.json", "r") as runnerdatraw:
        runnerdat = json.load(runnerdatraw)
        for runner in runnerdat:
            if runnerdat[runner]["status"] == "waiting" and runnerdat[runner]["place_runorder"] == 1:
                return runner


# ========== ENDPOINTS ==========

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/controller")
def controller():
    return render_template("controller.html")

@app.route("/config")
def config():
    return render_template("config.html")

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/buzzer")
def buzzer():
    return render_template("buzzer.html")

@app.route("/overlay")
def overlay():
    return render_template("streamoverlay.html")

@app.route("/debugGrid")
def debug():
    return render_template("debug.html")


@app.route('/api')
def serveApiFile():
    fullApiFile = {
        "runnerData": {},
        "compConfiguration": {},
        "obstacleData": {}
    }

    with open("runner_data.json", "r") as runnerdatfile:
        fullApiFile["runnerData"] = json.load(runnerdatfile)

    with open("comp_config.json", "r") as compconfigfile:
        fullApiFile["compConfiguration"] = json.load(compconfigfile)

    with open("obstacles.json", "r") as obstacledatfile:
        fullApiFile["obstacleData"] = json.load(obstacledatfile)

    return jsonify(fullApiFile)

# ========== FILES ==========

@app.route("/runner_data.json")
def runnerfile():
    return send_file(os.path.join(data_path, "runner_data.json"))

@app.route("/comp_config.json")
def configfile():
    return send_file(os.path.join(data_path, "comp_config.json"))

@app.route("/socket.io.min.js")
def socketiofile():
    return send_file("./socket.io.min.js")

@app.route("/timer.ttf")
def timerfont():
    return send_file("./timer.ttf")


# ========== SOUNDS ==========

@app.route("/sounds/buzzer_finish.wav")
def buzzersound():
    return send_file("./sounds/buzzer_finish.wav")

@app.route("/sounds/obstacle_complete.wav")
def obstaclesound():
    return send_file("./sounds/obstacle_complete.wav")

@app.route("/sounds/failing_is_sad_lol.wav")
def failsound():
    return send_file("./sounds/failing_is_sad_lol.wav")

global start_time
global end_time

@socketio.on('connect')
def handle_connect():
    print("Client connected!")


@socketio.on('btnpressed')
def handle_button(button):
    #print(button)
    if button == "finished" or button == "failed":
        global start_time
        global end_time
        global old_time
        end_time = time.time()

        elapsed = (end_time - start_time) + old_time  # Add previous time only here

        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        hundreths = int((elapsed * 100) % 100)

        with open("runner_data.json", "r") as runnerdatraw:
            runnerdat = json.load(runnerdatraw)
            runnerdat[getCurRunner()]["status"] = button
            runnerdat[getCurRunner()]["time"] = f"{minutes}:{seconds}.{hundreths}"

            print(f"\nSet runner {getCurRunner()} status to {button}")
            
            with open("runner_data.json", "w") as runnerdatdump:
                json.dump(runnerdat, runnerdatdump, indent=4)

    elif button == "pause":
        old_time += time.time() - start_time  # Accumulate pause duration
        start_time = None  # Mark timer as paused
        print(old_time)
        emit("timer_pause", broadcast=True)

    elif button == "resume":
        start_time = time.time()  # Resume from now
        emit("timer_resume", broadcast=True)

    elif button == "running":
        start_time = time.time()
        old_time = 0  # Reset accumulated time on fresh run

        with open("runner_data.json", "r") as runnerdatraw:
            runnerdat = json.load(runnerdatraw)
            runnerdat[getNextRunner()]["status"] = button
            
            with open("comp_config.json", "r") as compconfigraw:
                compconfig = json.load(compconfigraw)
                emit("timer_start", {
                    "timelimit": compconfig["time_limit"],
                    "timeformat": compconfig["comp_timetype"],
                    "coursetype": compconfig["comp_type"],
                    "runnername": runnerdat[getNextRunner()]["runner_name"],
                    "runnerdivision": runnerdat[getNextRunner()]["division"]
                }, broadcast=True)

            print(f"\nSet runner {getNextRunner()} status to {button}")

            for runner in runnerdat:
                if not runner == getNextRunner():
                    runnerdat[runner]["place_runorder"] -= 1

            with open("runner_data.json", "w") as runnerdatdump:
                json.dump(runnerdat, runnerdatdump, indent=4)

    elif button == "obstacle":
        with open("runner_data.json", "r") as runnerdatraw:
            runnerdat = json.load(runnerdatraw)
            runnerdat[getCurRunner()]["obstacles"] = runnerdat[getCurRunner()]["obstacles"] + 1

            with open("obstacles.json", "r") as obstaclesraw:
                obstacles = json.load(obstaclesraw)
                runnerdat[getCurRunner()]["result"] = obstacles[str(runnerdat[getCurRunner()]["obstacles"])]
                #runnerdat[getCurRunner()]["obstacle_times"][obstacles[str(runnerdat[getCurRunner()]["obstacles"])]] = elapsed = (end_time - start_time) + old_time

            print(f"\nSet runner {getCurRunner()} obstacles to {button}")
            print(f"Set runner {getCurRunner()} result to {runnerdat[getCurRunner()]["result"]}")

            emit("update_controls", {"currunner": getCurRunner(), "obstacles_completed": runnerdat[getCurRunner()]["obstacles"], "last_obstacle": runnerdat[getCurRunner()]["result"]}, broadcast=True)

            with open("runner_data.json", "w") as runnerdatdump:
                json.dump(runnerdat, runnerdatdump, indent=4)

    if button == "finished":
        emit("timer_finished", broadcast=True)

    if button == "failed":
        emit("timer_failed", broadcast=True)


    emit("update_boards", broadcast=True)

@socketio.on('push_compconfig')
def handle_comp_configs(compData):
    with open("comp_config.json", "w") as runnerdatdump:
        json.dump(compData, runnerdatdump, indent=4)
        
@socketio.on('push_competitors')
def handle_runner_dat(runnerData):
    with open("runner_data.json", "w") as runnerdatdump:
        json.dump(runnerData, runnerdatdump, indent=4)
    emit("update_boards", broadcast=True)

@socketio.on('push_obstacles')
def handle_runner_dat(obstacles):
    with open("obstacles.json", "w") as runnerdatdump:
        json.dump(obstacles, runnerdatdump, indent=4)

    time.sleep(1)
    emit("compdumped")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=49152)
