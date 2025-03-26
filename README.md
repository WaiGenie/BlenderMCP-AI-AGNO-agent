# Blender MCP + AI AGNO Agent

## Overview

This project integrates Blender with AI Agent capabilities through (MCP) and AGNO Agent framework, powered by Google Gemini 2.0 Flash. This groundbreaking integration allows you to control Blender using natural language, creating a powerful AI assistant for 3D modeling, animation, and visual effects.

The system connects Blender to an AI agent that understands complex 3D modeling concepts and can execute commands directly in Blender, making it the first implementation of its kind.

## Features

- Natural Language Control : Interact with Blender using conversational language
- Persistent Chat History : All conversations are saved for future reference
- Session Management : Create and manage multiple modeling sessions
- Advanced 3D Modeling Assistance : Get expert guidance on modeling techniques
- Asset Integration : Download and import assets from Poly Haven
- AI-Generated 3D Models : Generate models from text descriptions or images using Hyper3D
- Custom Material Creation : Create and apply materials with simple text commands
- Python Script Execution : Run custom Blender Python scripts through the agent

## Demo

Watch the demo video

## Setup and Installation

### Prerequisites

- Blender : Version 3.0 or newer
- Python : Version 3.10 or newer
- uv package manager :

  Mac :

  ```bash
  brew install uv
  ```

  Windows :

  ```powershell
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  set Path=C:\Users\nntra\.local\bin;%Path%
  ```

  For other platforms, follow the instructions on the uv installation page .

  ⚠️ Do not proceed before installing UV

### Installing the Blender MCP Addon

1. Download the addon.py file from this repository
2. Open Blender
3. Go to Edit > Preferences > Add-ons
4. Click "Install..." and select the addon.py file
5. Enable the addon by checking the box next to "Interface: Blender MCP"

### Setting Up the AGNO Agent

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/blender-mcp-agent.git
   cd blender-mcp-agent
   ```
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables (create a .env file with your API keys)

### Claude for Desktop Integration (Optional)

Watch the setup instruction video

Go to Claude > Settings > Developer > Edit Config > claude_desktop_config.json to include:

```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": [
                "blender-mcp"
            ]
        }
    }
}
```

### Cursor Integration (Optional)

Run blender-mcp without installing it permanently through uvx. Go to Cursor Settings > MCP and paste:

```plaintext
uvx blender-mcp
```

For Windows users, go to Settings > MCP > Add Server, add a new server with:

```json
{
    "mcpServers": {
        "blender": {
            "command": "cmd",
            "args": [
                "/c",
                "uvx",
                "blender-mcp"
            ]
        }
    }
}
```

Watch the Cursor setup video

⚠️ Only run one instance of the MCP server (either on Cursor or Claude Desktop), not both

## Usage

### Starting the Connection

1. In Blender, go to the 3D View sidebar (press N if not visible)
2. Find the "BlenderMCP" tab
3. Turn on the Poly Haven checkbox if you want assets from their API (optional)
4. Click "Connect to Claude"

### Running the AGNO Agent

1. Make sure Blender is running with the MCP addon activated
2. Run the agent script:

   ```bash
   python trail.py
   ```
3. The script will check for an active MCP server on port 9876
4. You can start with a predefined task or enter your own instructions
5. Type exit or quit to end the session

### Example Commands

- "Create a bicycle with a red frame and black wheels"
- "Add a metallic material to the selected object"
- "Import a wooden table from Poly Haven"
- "Generate a 3D model of a futuristic spaceship"
- "Apply a custom texture with a carbon fiber pattern"

## How It Works

The system uses a three-part architecture:

1. Blender MCP Addon : Runs inside Blender and exposes a server on port 9876
2. MCP Client : Connects to the Blender server and provides a communication channel
3. AGNO Agent : Powered by Google Gemini 2.0 Flash, interprets natural language and converts it to Blender operations
4. The agent maintains context through a SQLite database, allowing for complex, multi-step modeling tasks across multiple sessions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch ( git checkout -b feature/amazing-feature )
3. Commit your changes ( git commit -m 'Add some amazing feature' )
4. Push to the branch ( git push origin feature/amazing-feature )
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Blender Foundation for the amazing 3D software
- Google for the Gemini AI model
- Poly Haven for the 3D assets
- The AGNO framework developers
- The MCP protocol developers

## Contact

Your Name - Richardson Gunde

Youtube-demo - https://github.com/yourusername/blender-mcp-agent

Linkedin - 

Note : This is the first implementation connecting Blender MCP with an AGNO Agent powered by Google Gemini 2.0 Flash, making it a pioneering project in AI-assisted 3D modeling.
