import json
import boto3
import re

# Normalize phone number
def normalize_phone(phone):
    if not phone:
        return None
    digits = re.sub(r"\D", "", phone)
    return f"+{digits}"

# DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("CustomerAccounts")

def lambda_handler(event, context):
    print("EVENT:", event)

    return_connect = {}

    contact_data = event.get("Details", {}).get("ContactData", {})
    customer_endpoint = contact_data.get("CustomerEndpoint") or {}
    phone = customer_endpoint.get("Address")
    phone = normalize_phone(phone) if phone else None
    print("Normalized Phone:", phone)

    attributes = contact_data.get("Attributes") or {}
    aadhar = attributes.get("AadhaarNumber")
    print("Aadhaar:", aadhar)

    try:
        item = None

        # ---------------------------
        # Lookup by Aadhaar & Phone (composite key)
        # ---------------------------
        if aadhar and phone:
            response = table.get_item(Key={
                "AadhaarNumber": aadhar,
                "PhoneNumber": phone
            })
            item = response.get("Item")
            print("Item found by Aadhaar+Phone:", item)

        # ---------------------------
        # Fallback: Aadhaar only
        # ---------------------------
        if not item and aadhar:
            response = table.query(
                KeyConditionExpression="AadhaarNumber = :aadhar",
                ExpressionAttributeValues={":aadhar": aadhar}
            )
            items = response.get("Items", [])
            if items:
                item = items[0]
            print("Item found by Aadhaar:", item)

        # ---------------------------
        # Fallback: Phone only
        # ---------------------------
        if not item and phone:
            response = table.scan(
                FilterExpression="PhoneNumber = :phone",
                ExpressionAttributeValues={":phone": phone}
            )
            items = response.get("Items", [])
            if items:
                item = items[0]
            print("Item found by Phone:", item)

        # ---------------------------
        # Return results
        # ---------------------------
        if item:
            return_connect["Name"] = str(item.get("CutomerName", ""))
            return_connect["AccountBalance"] = str(item.get("Balance", ""))
            return return_connect
        else:
            return {"Name": "", "AccountBalance": "", "Error": "No record found"}

    except Exception as e:
        print("ERROR:", e)
        return {"Name": "", "AccountBalance": "", "Error": f"Error fetching item: {str(e)}"}
