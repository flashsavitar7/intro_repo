from flask import Flask, request, Response
import pytz
import datetime
from collections import OrderedDict
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    
    slack_name = "triumph_edet"
    track = "backend"

    utc_time = get_current_utc_time()

    current_day = get_current_day()

    github_file_url = "https://github.com/flashsavitar7/intro_repo/blob/main/app.py"
    github_repo_url = "https://github.com/flashsavitar7/intro_repo"

    response_data = OrderedDict([
        ("slack_name", slack_name),

        ("current_day", current_day),

        ("utc_time", utc_time),

        ("track", track),

        ("github_file_url", github_file_url),

        ("github_repo_url", github_repo_url),

        ("status_code", 200)
    ])

    json_response = json.dumps(response_data, indent=4)

    return Response(json_response, content_type='application/json')

def get_current_utc_time():
    current_time = datetime.datetime.now(pytz.utc)
    formatted_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    return formatted_time

def get_current_day():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_index = datetime.datetime.now().weekday()
    return days[current_day_index]

if __name__ == '__main__':
    app.run(debug=True)
