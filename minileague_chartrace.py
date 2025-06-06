import requests
import pandas as pd
import json
import bar_chart_race as bcr
import argparse
import sys

def get_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Something went wrong. Check minileague ID. Received status code {response.status_code}")
        sys.exit(1)
    return response.json()

parser = argparse.ArgumentParser(description='Bar chart racer for your fpl mini league\nRequires FFMPEG installed. Dependencies:Pandas,Json,Bar Chart Race,ArgPase')
parser.add_argument('--id', required=True, help='Your minileague ID (Required)')
parser.add_argument('--teams', type=int, default=5, help='How many players do you want to map. (Default is top 5)')
parser.add_argument('--output', type=str, default='2024_5.mp4', help="Output file name")
args = parser.parse_args()

json = get_data(f'https://fantasy.premierleague.com/api/leagues-classic/{args.id}/standings/')
data = pd.DataFrame(json['standings'])

team_ids = []
team_names = []
for i in range(len(data)):
    if len(team_ids) < args.teams:
        team_ids.append(data.iloc[i]['results']['entry'])
        team_names.append(data.iloc[i]['results']['entry_name'])

data_to_display = {}
for i in range(len(team_ids)):
    json = get_data('https://fantasy.premierleague.com/api/entry/' + str(team_ids[i]) + '/history/')
    data = pd.DataFrame(json['current'])
    a = data['total_points'].tolist()
    data_to_display[team_names[i]] = a

for i in data_to_display:
    data_to_display[i].insert(0,0)

data = pd.DataFrame(data_to_display)

final_row = data.iloc[-1]
for i in range(2):
    data = pd.concat([data, final_row.to_frame().T], ignore_index=True)

if args.output:
    if args.output.endswith('.mp4'):
        filename = args.output
    else:
        filename= args.output + '.mp4'
else:
    filename = args.output

bcr.bar_chart_race(
    df=data, 
    period_length=2500,
    steps_per_period=120, 
    n_bars=args.teams, 
    filename=filename
)