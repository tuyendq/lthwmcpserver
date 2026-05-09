from fastmcp import FastMCP
import datetime

mcp = FastMCP("Catering MCP Server")

@mcp.tool()
def get_current_menu() -> str:
    """Get the current menu for the day from lyskitchen.com"""
    # In a real implementation, this would fetch data from a database or API
    return "Today's menu: Grilled Chicken, Caesar Salad, and Chocolate Cake."

@mcp.tool()
def check_availability(delivery_date: str) -> bool:
    """Check if delivery is available for the given date (based on lyskitchen.com's working days and holidays)"""
    # In a real implementation, this would check against a schedule or database
    today = datetime.date.today()
    requested_date = datetime.datetime.strptime(delivery_date, "%Y-%m-%d").date()
    return requested_date >= today

@mcp.tool()
def create_catering_order(customer_name: str, menu_item: str, quantity: int, delivery_date: str) -> str:
    """Create a catering order for the specified menu item, quantity, and delivery date"""
    # In a real implementation, this would save the order to a database and return an order ID
    if not check_availability(delivery_date):
        return "Delivery date is not available."
    return f"Order created for {customer_name}: {quantity} x {menu_item} for delivery on {delivery_date}."

if __name__ == "__main__":
    mcp.run()
    