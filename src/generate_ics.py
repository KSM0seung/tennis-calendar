from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz
import os

# Initialize calendar
calendar = Calendar()

# Time zone (e.g. US Open in New York)
tz = pytz.timezone("America/New_York")

# Example mock matches
mock_matches = [
    {
        "summary": "US Open - Men's Round 1: Player A vs Player B",
        "start": datetime(2025, 8, 25, 11, 0),
        "duration_minutes": 120,
        "location": "Arthur Ashe Stadium"
    },
    {
        "summary": "US Open - Women's Round 1: Player C vs Player D",
        "start": datetime(2025, 8, 25, 13, 0),
        "duration_minutes": 90,
        "location": "Louis Armstrong Stadium"
    }
]

# Add events to calendar
for match in mock_matches:
    event = Event()
    event.name = match["summary"]
    event.begin = tz.localize(match["start"])
    event.duration = timedelta(minutes=match["duration_minutes"])
    event.location = match["location"]
    calendar.events.add(event)

# Save .ics file
output_path = os.path.join("output", "tennis_grandslam.ics")
with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(calendar)

print(f"✅ ICS file created: {output_path}")
