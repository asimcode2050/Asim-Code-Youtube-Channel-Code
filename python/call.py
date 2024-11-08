import requests

def check_spam_call(phone_number):
    # Your NumVerify API Key (get it from https://numverify.com/)
    api_key = "your_api_key_here"
    url = f"http://apilayer.net/api/validate?access_key={
        api_key}&number={phone_number}&country_code=US&format=1"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("error"):
            print(f"Error: {data['error']['info']}")
            return
        is_valid = data.get("valid", False)
        is_possible = data.get("possible", False)
        line_type = data.get("line_type", "Unknown")
        carrier = data.get("carrier", "Unknown")
        location = data.get("location", "Unknown")
        spam = data.get("spam", False)
        print(f"Number Info: {data}")
        print(f"Valid: {is_valid}")
        print(f"Possible: {is_possible}")
        print(f"Line Type: {line_type}")
        print(f"Carrier: {carrier}")
        print(f"Location: {location}")
        if spam:
            print(f"Warning: The number {phone_number} is flagged as spam!")
        else:
            print(f"The number {phone_number} seems legitimate.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to fetch the data: {e}")


phone_number = "+14158586273"  # Replace with the phone number you want to check
check_spam_call(phone_number)
