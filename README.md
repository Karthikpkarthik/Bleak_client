Here's a documentation for the provided code:

### Introduction
This Python script demonstrates how to use the Bleak library to communicate with a Bluetooth Low Energy (BLE) device. It connects to a BLE device with a specific address and reads and writes data to a characteristic. The script also plots real-time data using matplotlib.

### Dependencies
- Bleak library (for BLE communication)
- Matplotlib library (for plotting)

### Functionality
1. Imports necessary libraries and defines global variables.
2. Defines a function `fn(address)` to handle BLE communication:
   - Connects to the BLE device.
   - Starts notifications for a specific characteristic (`CHAR_UUID`) and calls `notify_handler(sender, data)` on notification.
   - Writes data (`text_to_write`) to the characteristic every 4 seconds and plots real-time data.
   - Stops notifications after 100 updates.
3. Defines `notify_handler(sender, data)` function to parse and handle received data:
   - Updates global variables (`time`, `temp`, `hrm`, `spo2`) based on the received data.
   - Appends data to corresponding lists for plotting.
4. Calls `asyncio.run(fn(ADDRESS))` to run the BLE communication function.

### Usage
- Replace `ADDRESS` with the BLE device address you want to connect to.
- Ensure the `CHAR_UUID` and `SER_UUID` match the characteristics of your BLE device.

### Note
- This script is a basic example and may need modifications to work with different BLE devices.
- Ensure that the `CHAR_UUID` and `SER_UUID` match the characteristics of your BLE device for proper communication.
- Handle exceptions and errors appropriately in your application.
