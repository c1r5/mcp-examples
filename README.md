# MCP Examples Project

This project demonstrates a Model Context Protocol (MCP) server and client setup, including tools and configuration for running the server in a Docker container.

## Project Structure

```
.
├── Dockerfile                # Docker build instructions for the MCP server
├── pyproject.toml            # Python project configuration
├── uv.lock                   # Lock file for dependencies
├── README.md                 # Project documentation
├── client/                   # Client-side code (if any)
└── servers/                  # MCP server implementation
    ├── __init__.py
    ├── main.py               # Main entry point for the server
    └── tools/                # Additional server tools
        ├── __init__.py
        ├── calendar.py       # Calendar tool implementation
        ├── task_manager.py   # Task manager tool implementation
        └── weather.py        # Weather tool implementation
```

## Setting Up and Building the Docker Image

1. **Build the Docker Image**

   From the project root, run:

   ```sh
   docker build -t mcp-example-stdio-server:latest .
   ```

   This will create a Docker image named `mcp-example-stdio-server:latest` containing the MCP server.

2. **Run the Server (Standalone)**

   You can run the server directly with:

   ```sh
   docker run --rm -i mcp-example-stdio-server:latest
   ```

   The server will start and listen for MCP stdio requests.

## `mcp.json` Configuration

The `.vscode/mcp.json` file configures how the MCP server is launched in development environments (such as VS Code):

```jsonc
{
  "servers": {
    "example-mcp-server": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "mcp-example-stdio-server:latest"
      ]
    }
  },
  "inputs": []
}
```

- **type**: `stdio` indicates the server communicates over standard input/output.
- **command**: The command to launch the server (`docker`).
- **args**: Arguments to run the Docker container with the built image.

This setup allows development tools to start the MCP server in a containerized environment automatically.

## Additional Notes

- Ensure Docker is installed and running on your system.
- Update the Docker image as needed after making changes to the server code by rebuilding the image.
- The `servers/tools/` directory contains modular tool implementations that can be extended as needed.
