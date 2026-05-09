from fastmcp import FastMCP

mcp = FastMCP("KitchenServer")

@mcp.tool()
def check_stock(item_name: str) -> str:
    """Kiểm tra nguyên liệu trong kho."""
    # Giả lập kiểm tra kho
    inventory = {"tom": 10, "bun": 5}
    count = inventory.get(item_name.lower(), 0)
    return f"Hiện còn {count} phần {item_name}."

mcp.run()