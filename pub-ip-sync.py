import requests

def get_public_ip():
  """
  Returns the public IP address of the device running the script.
  """
  response = requests.get("https://api.ipify.org")
  return response.text

def update_website(ip_address):
  """
  Updates the specified website with the provided IP address.
  """
  # Replace YOUR_WEBSITE_URL with the actual URL of the website you want to update
  website_url = "YOUR_WEBSITE_URL"

  # Replace YOUR_API_KEY with the actual API key for the website
  api_key = "YOUR_API_KEY"

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  data = {
    "ip_address": ip_address
  }

  # Make a PUT request to the website's API to update the IP address
  response = requests.put(website_url, headers=headers, json=data)

  # Print the response from the server
  print(response.text)

def main():
  # Get the public IP address of the device
  public_ip = get_public_ip()

  # Update the website with the IP address
  update_website(public_ip)

if __name__ == "__main__":
  main()
