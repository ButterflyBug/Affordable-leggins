import os
import textwrap
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(email, subject, message_body):
    message = Mail(
        from_email='notifications@leggins.com',
        to_emails=email,
        subject=subject,
        plain_text_content=message_body)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def email_address():
    return os.environ.get("EMAIL_NOTIFICATION", "")


def subject():
    return "We have found a promotion for you."


def single_leggin_format(product):
    leggin_url = f"https://www.myprotein.pl/{product['leggin_id']}.html"
    return f"* {product['leggin_name']} ({product['leggin_price']}.00 PLN) - {leggin_url}"


def message(mail_address, products):
    formatted_leggins = "\n            ".join(list(map(single_leggin_format, products)))
    if products:
        expected_message = f"""
            Hello {mail_address},

            We have found products which meet your criteria:

            {formatted_leggins}

            Happy hunting!
        """
    else:
        expected_message = f"""
            Hello {mail_address},

            We have not found products which meet your criteria.

            Happy hunting!
        """

    return textwrap.dedent(expected_message).strip()
