# IdeaToProd

A powerful AI-driven project that transforms ideas into production-ready applications using CrewAI agents and Model Context Protocol (MCP) integrations.

## Overview

IdeaToProd is an intelligent system that leverages multiple AI agents to design, develop, and deploy software projects. The system integrates with various services through MCP servers including GitHub, Jira, and Google Drive.

## Architecture

The project consists of several specialized AI agents:

- **High-Level Design Agent** (`HL_Design_agent.py`) - Creates architectural designs and system overviews
- **Detailed Design Agent** (`Detailed_Design_agent.py`) - Develops detailed technical specifications
- **Coder Agent** (`Coder_agent.py`) - Implements the actual code based on designs

## Project Structure

```
IdeaToProd/
├── agents/                     # AI agents for different tasks
│   ├── Coder_agent.py
│   ├── Detailed_Design_agent.py
│   └── HL_Design_agent.py
├── tasks/                      # Task definitions for agents
│   ├── detailed_design_task.py
│   └── hl_design_task.py
├── config/                     # Configuration files
│   └── mcp_config.json.template
├── credentials/                # Authentication files (gitignored)
├── .vscode/                    # VS Code configuration
│   └── mcp.json.template
├── App.py                      # Main application entry point
├── crew_manager.py             # CrewAI management logic
├── main.py                     # Primary execution script
├── setup_gdrive_auth.py        # Google Drive authentication setup
├── requirements.txt            # Python dependencies
└── next_steps.txt             # Development roadmap
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd IdeaToProd
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MCP configurations:**
   - Copy `.vscode/mcp.json.template` to `.vscode/mcp.json`
   - Copy `config/mcp_config.json.template` to `config/mcp_config.json`
   - Fill in your actual API tokens and credentials

4. **Configure authentication:**
   - Set up Google Drive credentials in the `credentials/` folder
   - Configure GitHub Personal Access Token
   - Set up Jira API token

## Configuration

### MCP Server Setup

The project uses Model Context Protocol servers for integration:

- **GitHub MCP Server** - For repository management and code operations
- **Jira MCP Server** - For project management and issue tracking  
- **Google Drive MCP Server** - For document storage and collaboration

### Environment Variables

Create configuration files from templates and populate with your credentials:

```bash
# GitHub Token
GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token

# Jira Configuration  
JIRA_BASE_URL=your_jira_url
JIRA_USERNAME=your_email
JIRA_API_TOKEN=your_jira_token

# Google Drive
GOOGLE_APPLICATION_CREDENTIALS=path_to_credentials_file
```

## Usage

1. **Run the main application:**
   ```bash
   python main.py
   ```

2. **Or use the Flask app:**
   ```bash
   python App.py
   ```

3. **Set up Google Drive authentication:**
   ```bash
   python setup_gdrive_auth.py
   ```

## Security

**Important:** This project handles sensitive credentials. Make sure to:

- Never commit actual API tokens or credentials
- Use the provided `.template` files as guides
- Keep the `credentials/` folder secure
- Regularly rotate your API tokens

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure no sensitive data is committed
5. Submit a pull request

## Requirements

See `requirements.txt` for detailed Python dependencies. Key frameworks include:

- CrewAI for multi-agent orchestration
- Flask for web interface
- Various MCP client libraries

## Roadmap

Check `next_steps.txt` for the current development roadmap and planned features.

## Important Notes

- **Never commit sensitive files** - The `.gitignore` is configured to protect credentials
- **Use templates** - Always copy from `.template` files and fill in your actual values
- **Security first** - Regularly review and rotate API tokens

## License

[Add your license information here]

## Support

[Add support information, issues link, or contact details]

---

**Made with using CrewAI and MCP**
