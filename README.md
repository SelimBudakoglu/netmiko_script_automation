Script to send configuration from a file to a list of devices

Tested on Python 2.7 and 3.6

Requires:
- netmiko >= 2.2.2

Supports:
- Routers and Switches Cisco with SSH/Telnet configured (default ports)

Limitations:
- Same credentials for all devices
- Only SSH/Telnet with default ports (22/23)
- Last line on configuration file can not be 'exit'
- Only config that can be the same in different devices

How to use:
1) Inform port (22/23) and IP address of devices in devices_to_configure.csv file
2) Put the configuration that you want to send to devices in file commands_to_send.txt
3) Run config_devices_from_file.py

Use case:
- to enables logging, to collects information, to creates username, shut/no shut interfaces, to removes config, any other config/command that can be repeated over different devices
