"""
This module simulates a weather forecast tool.

It generates fictional but plausible weather data for a given location.
"""

import json
import random
from typing import Dict, Any
from servers.tools import mcp

@mcp.resource("weather://{location}")
def get_weather_forecast(location: str) -> str:
    """
    Generates a simulated weather forecast for a specific location.

    :param location: The location to get the forecast for (e.g., "São Paulo, Brazil").
    :return: A JSON string with the simulated weather forecast details.
    """
    # Simulate weather conditions
    conditions = ["Sunny", "Cloudy", "Partly Cloudy", "Rainy", "Stormy", "Windy"]
    selected_condition = random.choice(conditions)

    # Simulate temperature based on condition
    if "Sunny" in selected_condition:
        temp_celsius = random.uniform(25.0, 35.0)
    elif "Cloudy" in selected_condition:
        temp_celsius = random.uniform(18.0, 24.0)
    elif "Rainy" in selected_condition or "Stormy" in selected_condition:
        temp_celsius = random.uniform(15.0, 20.0)
    else:
        temp_celsius = random.uniform(20.0, 28.0)

    # Simulate other weather data
    humidity = random.uniform(40.0, 90.0)
    wind_speed_kmh = random.uniform(5.0, 25.0)
    precipitation_chance = random.uniform(0.0, 100.0) if "Rainy" in selected_condition or "Stormy" in selected_condition else random.uniform(0.0, 20.0)

    forecast = {
        "location": location,
        "condition": selected_condition,
        "temperature_celsius": f"{temp_celsius:.1f}",
        "humidity_percent": f"{humidity:.1f}",
        "wind_speed_kmh": f"{wind_speed_kmh:.1f}",
        "precipitation_chance_percent": f"{precipitation_chance:.1f}"
    }

    response = {
        "status": "success",
        "message": f"Simulated weather forecast for {location}.",
        "forecast": forecast
    }

    return json.dumps(response, indent=4)