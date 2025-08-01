from mcp.server.fastmcp import FastMCP


mcp = FastMCP()

from servers.tools import calendar, task_manager, weather

__all__ = ['mcp', 'calendar', 'task_manager', 'weather']

