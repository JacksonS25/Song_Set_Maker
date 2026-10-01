import os
import base64
from mailjet_rest import Client

def send_gmail_pdf(pdf_output, email_address, pdf_filename):
    # --- CONFIGURATION ---
    # Verified Gmail address on Mailjet
    my_email = os.getenv("EMAIL_ADDRESS") 
    # Mailjet API credentials set in Render Environment Variables
    api_key = os.getenv("MJ_APIKEY_PUBLIC")
    api_secret = os.getenv("MJ_APIKEY_PRIVATE")

    # 1. Read BytesIO buffer & Base64 encode for Mailjet
    pdf_output.seek(0)
    file_data = pdf_output.read()
    encoded_pdf = base64.b64encode(file_data).decode("utf-8")

    # 2. Build the API payload
    data = {
        "Messages": [
            {
                "From": {"Email": my_email},
                "To": [{"Email": email_address}],
                "Subject": "Your Generated PDF Set List",
                "TextPart": "Hello! Please find your Song Set List attached to this email.",
                "Attachments": [
                    {
                        "ContentType": "application/pdf",
                        "Filename": pdf_filename,
                        "Base64Content": encoded_pdf
                    }
                ]
            }
        ]
    }

    # 3. Send email via HTTPS
    try:
        mailjet = Client(auth=(api_key, api_secret), version="v3.1")
        result = mailjet.send.create(data=data)

        if result.status_code == 200:
            print("Success! The email has been sent.")
        else:
            print(f"Mailjet error [{result.status_code}]: {result.json()}")
    except Exception as error:
        print(f"Something went wrong: {error}")