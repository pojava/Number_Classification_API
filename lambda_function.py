import json
import urllib.request

def classify_number(number):
    # Check if the number is prime
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        else:
            is_prime = True
    else:
        is_prime = False

    # Check if the number is a perfect number
    is_perfect = sum(i for i in range(1, number) if number % i == 0) == number

    # Check if the number is Armstrong
    digits = [int(digit) for digit in str(number)]
    armstrong_check = sum(digit ** len(digits) for digit in digits)
    is_armstrong = armstrong_check == number

    # Sum of the digits
    digit_sum = sum(digits)

    # Determine properties
    properties = []
    if is_armstrong:
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    return is_prime, is_perfect, properties, digit_sum

def fetch_fun_fact(number):
    try:
        url = f"http://numbersapi.com/{number}/math"
        with urllib.request.urlopen(url) as response:
            return response.read().decode()
    except Exception:
        return "Unable to fetch fun fact at the moment."

def lambda_handler(event, context):
    try:
        number = int(event["queryStringParameters"]["number"])

        is_prime, is_perfect, properties, digit_sum = classify_number(number)
        fun_fact = fetch_fun_fact(number)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "number": number,
                "is_prime": is_prime,
                "is_perfect": is_perfect,
                "properties": properties,
                "digit_sum": digit_sum,
                "fun_fact": fun_fact
            })
        }
    except (ValueError, KeyError):
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "number": event["queryStringParameters"].get("number", "invalid"),
                "error": True
            })
        }
