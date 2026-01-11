from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("MyFirstMCPServer")

# Add a Tool: Something the AI can 'do'
@mcp.tool()
def add_number(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply_number(a: int, b: int) -> int:
    """Multiply two numbers together"""
    return a * b

# Add a Resource: Data the AI can 'read'
@mcp.resource("echo://greeting")
def get_greeting() -> str:
    """Returns a static greeting message."""
    return "Hello! This message is coming from your local MCP server."

if __name__ == "__main__":
    mcp.run()
    