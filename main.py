"""
show_rides.py

Reads virtual ride data from data.json (same directory as this script)
and prints it out as a nicely formatted table.

Run in PyCharm: just open this file and hit Run.
Make sure data.json sits in the same folder as this script.
"""

import json
import os


def load_rides(filename="data.json"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, filename)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("rides", [])


def fmt(value, unit=""):
    """Return '-' for missing values, otherwise value + unit."""
    if value is None:
        return "-"
    return f"{value}{unit}"


def print_table(rides):
    # Column headers and the width for each column
    columns = [
        ("Date", 10),
        ("Time", 6),
        ("Map", 32),
        ("Dist(km)", 8),
        ("Moving", 7),
        ("Elev(m)", 7),
        ("AvgW", 5),
        ("MaxW", 5),
        ("AvgHR", 6),
        ("MaxHR", 6),
        ("AvgSpd", 7),
        ("MaxSpd", 7),
        ("Cad", 4),
        ("Cals", 5),
        ("Effort", 6),
    ]

    header = " | ".join(name.ljust(width) for name, width in columns)
    print(header)
    print("-" * len(header))

    for ride in rides:
        row_values = [
            fmt(ride.get("date")),
            fmt(ride.get("time")),
            fmt(ride.get("map_name")),
            fmt(ride.get("distance_km")),
            fmt(ride.get("moving_time")),
            fmt(ride.get("elevation_m")),
            fmt(ride.get("power_avg_w")),
            fmt(ride.get("power_max_w")),
            fmt(ride.get("heart_rate_avg_bpm")),
            fmt(ride.get("heart_rate_max_bpm")),
            fmt(ride.get("speed_avg_kmh")),
            fmt(ride.get("speed_max_kmh")),
            fmt(ride.get("cadence_avg")),
            fmt(ride.get("calories")),
            fmt(ride.get("relative_effort")),
        ]

        row = " | ".join(
            str(val).ljust(width) for val, (_, width) in zip(row_values, columns)
        )
        print(row)


def main():
    rides = load_rides()

    if not rides:
        print("No ride data found in data.json.")
        return

    print(f"Found {len(rides)} ride(s):\n")
    print_table(rides)


if __name__ == "__main__":
    main()