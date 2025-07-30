from crewai import Agent
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
import os
import json

class HighLevelDesignAgent:
    def __init__(self):
        # Load MCP configuration
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'mcp_config.json')
        try:
            with open(config_path, 'r') as f:
                mcp_config = json.load(f)
        except FileNotFoundError:
            print(f"Configuration file not found at {config_path}")
            exit(1)

        # Get Google Drive MCP server configuration
        gdrive_config = mcp_config['mcpServers']['gdrive']

        # Configure Google Drive MCP server parameters
        self.server_params = StdioServerParameters(
            command=gdrive_config['command'],
            args=gdrive_config['args'],
            env={**gdrive_config.get('env', {}), **os.environ}
        )

    def create_agent(self):
        """Create and return the HL Design agent with Google Drive tools initialized"""
        with MCPServerAdapter(self.server_params) as mcp_tools:
            return Agent(
            role="High-Level Design Architect",
            goal="Create comprehensive high-level design documents from project ideas and save them to Google Drive",
            backstory="""I am an experienced system architect with 15+ years of experience in translating 
            innovative ideas into structured, actionable design documents. I specialize in creating clear, 
            comprehensive high-level designs that serve as blueprints for development teams.""",
            tools=mcp_tools,
            verbose=True,
            allow_delegation=False
            )

