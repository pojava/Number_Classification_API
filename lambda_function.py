import json
import math
import urllib.request

# Check if the number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Check if the number is an Armstrong number
def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    num_of_digits = len(digits)
    return number == sum(digit ** num_of_digits for digit in digits)

# Check if the number is perfect
def is_perfect(number):
    if number < 2:
        return False
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

# Fetch a fun fact about the number from Numbers API
def get_fun_fact(number):
    try:
        url = f"http://numbersapi.com/{number}/math?json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data.get("text", "No fun fact found.")
    except Exception as e:
        return "Unable to fetch fun fact."

# Lambda handler function
def lambda_handler(event, context):
    # Validate input number
    try:
        number = int(event["queryStringParameters"]["number"])
    except (ValueError, TypeError):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "number": event["queryStringParameters"].get("number", "undefined"),
                "error": True
            })
        }

    # Determine number properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": get_fun_fact(number)
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
