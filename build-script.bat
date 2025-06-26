pyinstaller --onefile ^
--add-data "templates;templates" ^
--add-data "comp_config.json;." ^
--add-data "obstacles.json;." ^
--add-data "runner_data.json;." ^
--add-data "timer.ttf;." ^
--add-data "socket.io.min.js;." ^
server.py
