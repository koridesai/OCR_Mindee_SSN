import requests
import json
import time
import subprocess

url = "https://api.mindee.net/v1/products/saikoride1999/us_pay_stubs/v1/predict_async"


with open("Income/PayStub_3.pdf", "rb") as myfile:
    files = {"document": myfile}
    headers = {"Authorization": "Token 24e87821e0b72583dcf4227d98333ff7"}
    response = requests.post(url, files=files, headers=headers)
    response_data = response.json()

# Write response data to a JSON file
output_file = "paystub_output.json"
with open(output_file, "w") as json_file:
    json.dump(response_data, json_file)

print("\nOutput saved to", output_file)

time.sleep(5)

# Call the get_output.py script
subprocess.run(["python", "get_output.py"])

time.sleep(2)

# Call the get_output.py script
subprocess.run(["python", "extract_data.py"])