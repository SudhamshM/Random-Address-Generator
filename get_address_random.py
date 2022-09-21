# parse address from json api request 
import requests

url = "https://fakerapi.it/api/v1/addresses?_quantity=100&_locale=en_US"

# sending a request to the api and converting to json object to parse
response = requests.request("GET", url).json()

# similar to a dictionary, accessing the status code's value from the 'code' key
status_desc = response["status"]
status_code = response["code"]
print(f"The status is {status_code}, so it is {status_desc}!")


# parsing the address values from the dictionary
def parse_base(index_number):
    bas_response = response["data"]
    addr_street = bas_response[index_number]["street"]
    build_no = bas_response[index_number]["buildingNumber"]
    cityx = bas_response[index_number]["city"]
    zip_codex = bas_response[index_number]["zipcode"]
    countryx = bas_response[index_number]["country"] + " (" + bas_response[index_number]["county_code"] + ")"
    return f'''
       Street Address: {addr_street}
       Building Number: {build_no} 
       City: {cityx}
       Zip Code: {zip_codex}
       Country: {countryx}
            '''


# printing 10 addresses
for number in range(10):
    print(parse_base(number))

