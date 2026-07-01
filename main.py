import os
import requests

# used to discover values and you paste them into your environment.
API_URL = os.getenv("API_URL", "http://4.224.186.213/evaluation-service/vehicles")
API_KEY = os.getenv("API_KEY")

# If API_KEY is not set in the environment, offer a quick interactive prompt
# and a short help message explaining how to copy a bearer token from Postman.
if not API_KEY:
    print("Error: API_KEY not found in environment.")
    print("How to get a bearer token from Postman:")
    print(" 1) Open your request in Postman.")
    print(" 2) Go to the Authorization tab and choose the auth type (e.g. Bearer Token).")
    print(" 3) Copy the token value shown and paste it below when prompted.")
    try:
        API_KEY = input("Paste Bearer token (or press Enter to exit): ").strip()
    except (EOFError, KeyboardInterrupt):
        API_KEY = ""

    if not API_KEY:
        print("No API key provided. Exiting.")
        raise SystemExit(1)

headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.get(API_URL, headers=headers)
print("Status Code:", response.status_code)
try:
    print("Data:", response.json())
except ValueError:
    print("Response text:", response.text)

# import dotenv
# import json
# import os
# import requests

# dotenv.load_dotenv()

# print("Getting Started..")

# def load_api_config():
#     dotenv_path = dotenv.find_dotenv()
#     if dotenv_path:
#         dotenv.load_dotenv(dotenv_path, override=False)

#     api_url = os.getenv("API_URL")
#     api_key = os.getenv("API_KEY")

#     config_path = os.getenv("API_CONFIG_PATH", "config.json")
#     if os.path.exists(config_path):
#         with open(config_path, "r", encoding="utf-8") as config_file:
#             config = json.load(config_file)
#             api_url = api_url or config.get("API_URL")
#             api_key = api_key or config.get("API_KEY")

#     config_url = os.getenv("API_CONFIG_URL")
#     if not api_url and config_url:
#         config_response = requests.get(config_url, timeout=10)
#         config_response.raise_for_status()
#         config = config_response.json()
#         api_url = api_url or config.get("API_URL")
#         api_key = api_key or config.get("API_KEY")

#     return api_url, api_key

# def fetch_data(endpoint, api_url, api_key):
#     if not api_url:
#         raise ValueError("API_URL is not configured")

#     url = f"{api_url.rstrip('/')}/{endpoint.lstrip('/')}"
#     headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     return response.json()

# def main():
#     api_url, api_key = load_api_config()

#     if not api_url:
#         print("API_URL not defined in environment, .env, config.json, or external config source.")
#         return

#     try:
#         depots = fetch_data("depots", api_url, api_key)
#         print("Depots:", depots)

#         task_details = fetch_data("tasks", api_url, api_key)
#         print("Task details:", task_details)
#     except requests.RequestException as error:
#         print("Error fetching data:", error)
#     except ValueError as error:
#         print("Configuration error:", error)

# if __name__ == "__main__":
#     main()
