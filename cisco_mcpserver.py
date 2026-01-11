from mcp.server.fastmcp import FastMCP
import paramiko

mcp = FastMCP("Cisco Master")

@mcp.tool()
def get_router_config(ip: str, user: str, password: str) -> str:
    """
    Connects to a Cisco router via SSH and retrieves its running configuration.

    Args:
        ip (str): The IP address of the Cisco router.
        user (str): The username for SSH authentication.
        password (str): The password for SSH authentication.

    Returns:
        str: The running configuration of the router.
    """
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the router
        ssh.connect(ip, username=user, password=password, timeout=10)

        # Execute the command to get the running configuration
        stdin, stdout, stderr = ssh.exec_command("show running-config")

        # Read the output
        config = stdout.read().decode()

        # Close the SSH connection
        ssh.close()

        return config

    except Exception as e:
        return f"An error occurred: {e}"
if __name__ == "__main__":
    mcp.run()