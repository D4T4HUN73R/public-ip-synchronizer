# public-ip-synchronizer
A simple Python script that will synchronize your public IP address to a website.

This script uses the requests library to make HTTP requests. It has two functions: get_public_ip and update_website.

The get_public_ip function uses the requests library to make a GET request to the https://api.ipify.org API, which returns the public IP address of the device running the script as a string.

The update_website function takes in an IP address as a parameter and makes a PUT request to the website's API, passing the IP address in the request body as JSON. You will need to replace YOUR_WEBSITE_URL and YOUR_API_KEY with the actual URL of the website and the API key for the website.

The main function calls the get_public_ip and update_website functions to get the public IP address of the device and update the website with that IP address.
