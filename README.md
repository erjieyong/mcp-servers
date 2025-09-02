# mcp-servers

## Browser Use
1) creates a mcp server that allow AI to browse the web for you. 
  a) We will be basing the browseruse-default-mcp based on browser-use (https://github.com/browser-use/browser-use/blob/main/browser_use/mcp/server.py). However, we stop using it as it seems to only support openai and we can't get the gemini option to work. Also we do not need all the detailed function (e.g scroll, _init_browser_session, etc), we just use the agent directly.
  b) Create our own version of MCP based on basic browser-use usage.
