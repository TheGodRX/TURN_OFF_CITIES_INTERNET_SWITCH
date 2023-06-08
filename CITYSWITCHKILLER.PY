import os

# Enter the IP or domain name of the switch to be turned off
switch_ip = "switch_ip_address"

# Enter the switch login credentials
switch_username = "switch_username"
switch_password = "switch_password"

# Turn off switch
os.system(f"ssh {switch_username}@{switch_ip} -p 22 '{switch_password}; no shutdown'")
