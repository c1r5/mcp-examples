"""
This module simulates a task scheduler.

Tasks are stored in memory and will be lost on server restart.
"""

import json
import uuid
from typing import Dict, Any, Optional
from servers import mcp
# In-memory storage for scheduled tasks
_scheduled_tasks: Dict[str, Dict[str, Any]] = {}


@mcp.tool()
def schedule_task(title: str, start_time: str, end_time: str) -> str:
    """
    Schedules a new task in the calendar.

    :param title: The title or description of the task.
    :param start_time: The start time for the task (e.g., "2025-12-01T10:00:00").
    :param end_time: The end time for the task (e.g., "2025-12-01T11:00:00").
    :return: A JSON string confirming the creation and the task details.
    """
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "status": "scheduled"
    }
    _scheduled_tasks[task_id] = task
    response = {
        "status": "success",
        "message": "Task scheduled successfully.",
        "task": task
    }
    return json.dumps(response, indent=4)

@mcp.tool()
def delete_task(task_id: str) -> str:
    """
    Deletes a scheduled task.

    :param task_id: The unique ID of the task to delete.
    :return: A JSON string confirming the deletion or reporting an error.
    """
    if task_id in _scheduled_tasks:
        del _scheduled_tasks[task_id]
        response = {"status": "success", "message": f"Task {task_id} deleted."}
    else:
        response = {"status": "error", "message": f"Task {task_id} not found."}
    return json.dumps(response, indent=4)

@mcp.tool()
def edit_task(task_id: str, title: Optional[str] = None, start_time: Optional[str] = None, end_time: Optional[str] = None) -> str:
    """
    Edits an existing scheduled task.

    :param task_id: The unique ID of the task to edit.
    :param title: The new title for the task (optional).
    :param start_time: The new start time for the task (optional).
    :param end_time: The new end time for the task (optional).
    :return: A JSON string confirming the update or reporting an error.
    """
    if task_id not in _scheduled_tasks:
        response = {"status": "error", "message": f"Task {task_id} not found."}
        return json.dumps(response, indent=4)

    task = _scheduled_tasks[task_id]
    if title is not None:
        task["title"] = title
    if start_time is not None:
        task["start_time"] = start_time
    if end_time is not None:
        task["end_time"] = end_time
    
    _scheduled_tasks[task_id] = task
    response = {
        "status": "success",
        "message": f"Task {task_id} updated.",
        "task": task
    }
    return json.dumps(response, indent=4)

@mcp.resource("tasks://list")
def list_tasks() -> str:
    """
    Lists all currently scheduled tasks.

    :return: A JSON string containing a list of all tasks.
    """
    response = {
        "status": "success",
        "count": len(_scheduled_tasks),
        "tasks": list(_scheduled_tasks.values())
    }
    return json.dumps(response, indent=4)
