from crewai_tools import MCPServerAdapter
from credentials.secret_keys import google_drive_mcp_url

print(f"Connecting to Composio MCP (Cursor): {google_drive_mcp_url}")

server_params = {
    "url": google_drive_mcp_url,
    "transport": "streamable-http"  
}

try:
    _adapter = MCPServerAdapter(server_params)
    google_drive_mcp_tools = list(_adapter.tools)
    
    print(f"Successfully connected! Found {len(google_drive_mcp_tools)} Google Drive tools:")
    for i, tool in enumerate(google_drive_mcp_tools):
        print(f"  {i+1}. {tool.name}")
    
except Exception as e:
    print(f"Error connecting to Composio MCP: {e}")
    print("Fallback: Using empty tools list")
    google_drive_mcp_tools = []
