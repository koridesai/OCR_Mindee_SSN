import json

# Load data from final_output.json
with open("final_output.json", "r") as json_file:
    data = json.load(json_file)

# Extract relevant details
document_info = data["document"]["inference"]["prediction"]

# Extract features
first_name = document_info["first_name"]["value"]
last_name = document_info["last_name"]["value"]
date = document_info["date"]["value"]
social_security_number = document_info["social_security_number"]["value"]

# Print extracted details
print("\nExtracted details from the document:\n\n")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Date:", date)
print("Social Security Number:", social_security_number)
