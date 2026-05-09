import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_client():
    # Parameters for connecting to the MCP server
    params = StdioServerParameters(
        command=["python"],  # Command to start the server 
        args=["server.py"],  # Arguments for the server command
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await sesion.list_tools()
            print("Available tools:")
            for tool in tools:
                print(f"- {tool.name}: {tool.description}")
            
            print("\nInvoking check_stock tool with item='apple' and quantity=10")
            result = await session.call_tool(
                "check_stock", 
                args={"item": "apple", "quantity": 10}
            )

            for content in result.content:
                if content.type == "text":
                    print(f"Tool Output: {content.text}")

if __name__ == "__main__":
    try:
        asyncio.run(run_client())
    except KeyboardInterrupt:
        pass