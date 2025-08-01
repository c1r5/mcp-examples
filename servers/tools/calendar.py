"""
This module provides date and time functions.
"""

import json
import pytz

from datetime import datetime, timedelta
from typing import Optional
from dateutil import parser
from servers import mcp


@mcp.tool()
def get_current_datetime(timezone_str: str = "UTC") -> str:
    """
    Gets the current date and time for a given timezone and returns it as a JSON string.

    :param timezone_str: The timezone to use, e.g., "America/Sao_Paulo".
    :return: A JSON string with the current date and time details.
    """
    timezone = pytz.timezone(timezone_str)
    now = datetime.now(timezone)
    output = {
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": timezone_str,
        "iso_format": now.isoformat(),
        "weekday": now.strftime("%A"),
    }
    return json.dumps(output, indent=4)

@mcp.tool()
def get_future_datetime(days: int, date_str: Optional[str] = None) -> str:
    """
    Calculates a future date and returns it as a JSON string.

    :param days: The number of days to add.
    :param date_str: The base date as a string. If None, the current date is used.
    :return: A JSON string with the future date details.
    """
    base_date = parser.parse(date_str) if date_str else datetime.now()
    future_date = base_date + timedelta(days=days)
    output = {
        "base_date": base_date.isoformat(),
        "days_added": days,
        "future_datetime": future_date.strftime("%Y-%m-%d %H:%M:%S"),
        "iso_format": future_date.isoformat(),
    }
    return json.dumps(output, indent=4)

@mcp.tool()
def get_past_datetime(days: int, date_str: Optional[str] = None) -> str:
    """
    Calculates a past date and returns it as a JSON string.

    :param days: The number of days to subtract.
    :param date_str: The base date as a string. If None, the current date is used.
    :return: A JSON string with the past date details.
    """
    base_date = parser.parse(date_str) if date_str else datetime.now()
    past_date = base_date - timedelta(days=days)
    output = {
        "base_date": base_date.isoformat(),
        "days_subtracted": days,
        "past_datetime": past_date.strftime("%Y-%m-%d %H:%M:%S"),
        "iso_format": past_date.isoformat(),
    }
    return json.dumps(output, indent=4)
