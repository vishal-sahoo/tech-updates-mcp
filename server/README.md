## Run the server

### Set up the environment

1. Create virtual environment and activate it

```
uv venv
source .venv/bin/activate
```

2. Add requirements

```
uv pip install -r pyproject.toml
```

### Test the server with MCP inspector

```
mcp dev server.py
```

If the above fails, try

```
uv run mcp dev server.py
```

### Install in Claude Desktop

Install [Claude Desktop](https://claude.ai/download)

```
mcp install server.py
```

Restart Claude Desktop

#### Note

If you see an error in Claude Desktop, click `Settings -> Developer tab -> Edit Config` and update as follows

```
{
  "mcpServers": {
    "Tech Updates": {
      "command": "/Users/vishalsahoo/.local/bin/uv",
      "args": [
        "--directory",
        "/Users/vishalsahoo/Desktop/tech-updates-mcp/project",
        "run",
        "server.py"
      ]
    }
  }
}
```

You can run the following to get the path to your uv

```
which uv
```

### References:

Server set up:

- https://modelcontextprotocol.io/quickstart/server
- https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file

Claude Desktop set up:

- https://modelcontextprotocol.io/quickstart/user
