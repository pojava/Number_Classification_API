# Number Classification API

## Overview
This API classifies numbers by returning interesting mathematical properties, including prime status, Armstrong status, digit sum, and a fun fact retrieved from the Numbers API.

## API Endpoint
```
GET <your-api-url>/api/classify-number?number=<integer>
```

## Usage Instructions
To use the API:
1. Send a **GET** request to the provided endpoint.
2. Include the number parameter as a query string.

### Example Request
```
GET https://<your-api-url>/api/classify-number?number=371
```

## Example JSON Responses

### **Successful Response (200 OK)**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Error Response (400 Bad Request)**
```json
{
    "number": "alphabet",
    "error": true
}
```

### **Error Response (500 Internal Server Error)**
```json
{
    "message": "Internal Server Error: <error description>"
}
```

## Deployment Instructions

### 1. Create AWS Lambda Function
- Open the AWS Lambda Console and create a new function.
- Select "Author from scratch."
- Choose Python as the runtime environment.
- Upload the zipped code containing the `lambda_function.py` file and dependencies.

### 2. Set Up API Gateway
- Open the API Gateway Console.
- Create a new API and connect it to the Lambda function using a **Lambda Proxy Integration**.
- Deploy the API to a stage.
- Enable **CORS** for public access.

### 3. Environment Variables
Ensure that the Numbers API does not require an API key; otherwise, configure environment variables to securely store credentials.

### 4. GitHub Repository
- Create a new public GitHub repository.
- Upload all project files, including the Lambda function and `README.md`.
- Ensure the repository includes clear instructions and is well-organized.

## Conclusion
This API provides mathematical properties for numbers and retrieves fun facts from the Numbers API. Test thoroughly to ensure all requirements are met before deployment and submission.
