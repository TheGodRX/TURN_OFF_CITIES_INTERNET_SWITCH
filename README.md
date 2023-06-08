# TURN_OFF_CITIES_INTERNET_SWITCH

# Switch Off Script

This script utilizes the Shodan API and the Paramiko library to turn off a switch remotely.

## Installation

To use this code, the following installations must be made:

- [Python 3.x](https://www.python.org/)
- [Shodan Python Library](https://pypi.org/project/shodan/)
- [Paramiko Python Library](https://www.paramiko.org/installing.html)

You can install these libraries using pip by executing the following command in the terminal:
```shell
pip install shodan paramiko
```

## Configuration

Ensure you have an account on [Shodan.io](https://www.shodan.io/) and an API key generated. This key must be entered into the code. Replace `YOUR_API_KEY` with your personal API key:
```python
SHODAN_API_KEY = "YOUR_API_KEY"
```

## Usage

When you run the script, it will prompt you to enter the name of the city where the switch is located. The script will then use the Shodan API to search for switches in that city.

If any switches are found, the script will attempt to turn off each switch by attempting a remote SSH connection using the default username and passwords stored in the `switch_passwords` list.

**Caution:** This script may be illegal and immoral if used without explicit permission. Misuse of this script could result in serious consequences.

## Disclaimer

This code is for educational and informational purposes only. The developers of this code are not responsible for any illegal or unethical use of this code. Please use it at your own risk.
