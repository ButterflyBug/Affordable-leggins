import os
import textwrap
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.template import Context, Template, Engine


def send_email(email, subject, message_body):
    message = Mail(
        from_email="notifications@leggins.com",
        to_emails=email,
        subject=subject,
        plain_text_content=message_body,
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
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
    return (
        f"* {product['leggin_name']} ({product['leggin_price']}.00 PLN) - {leggin_url}"
    )


# template = Template("My name is {{ my_name }}.")

# >>> context = Context({"my_name": "Adrian"})
# >>> template.render(context)


def message(mail_address, products):
    message = open("affordable_leggins/templates/notification_email.txt", "r").read()
    context = Context({"email_address": mail_address, "leggins": products})
    engine = Engine()

    return engine.from_string(message).render(context)
