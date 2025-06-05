# FPL Tools

Various Python tools I've created to better visualize Fantasy Premier League data.

## Mini League Bar Chart Racer

An animated bar chart showing the progression of your FPL mini-league standings over time.

### Prerequisites

- **Python 3.x**
- **FFmpeg** (for video generation)

### Dependencies

Install the required Python packages:

```bash
pip install pandas bar_chart_race argparse
```

| Option    | Description | Required | Default |
| -------- | ------- | -------- | ------- |
| ```-h ```  | Display help | N | - |
| ```--id``` | MiniLeague ID [How to find mini league ID](https://fplrank.live/how-to-find-your-league-id 'minileagueid')| Y | - |
|```--teams```| How many teams to chart. Example if you select 10 the script will chart the top 10 teams. | N | 5 |
|```--output``` | Name output file | N | 2024_5.mp4 |

