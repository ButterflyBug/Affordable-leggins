import os
import inspect
import textwrap
import pytest
import mock
from affordable_leggins.send_notification import (
    send_email,
    email_address,
    subject,
    message,
)
from fixtures import leggin_with_size_s, leggin_with_size_m


@mock.patch("affordable_leggins.send_notification.SendGridAPIClient")
def test_send_email(mocked_sendgrid_client):
    email = "kasia@gmail.com"
    subject = "We have found a promotion for you."
    message = "message"
    assert send_email(email, subject, message)


def test_email_address():
    os.environ["EMAIL_NOTIFICATION"] = "kasia@gmail.com"
    assert email_address() == "kasia@gmail.com"


def test_subject():
    assert subject() == "We have found a promotion for you."


def match_template(email_address, leggins, expected_message):
    assert message(email_address, leggins) == dedent_expression(expected_message)


def dedent_expression(expression):
    return textwrap.dedent(expression).strip()


def test_message(leggin_with_size_s):
    expected_message = """
        Hello kasia@gmail.com,

        We have found products which meet your criteria:

        * Power Curve (60.00 PLN) - https://www.myprotein.pl/11871452.html

        Happy hunting!
    """

    match_template("kasia@gmail.com", [leggin_with_size_s], expected_message)


def test_other_message(leggin_with_size_m):
    expected_message = """
        Hello kasia@gmail.com,

        We have found products which meet your criteria:

        * Szwowe Czarne (50.00 PLN) - https://www.myprotein.pl/11871452.html

        Happy hunting!
    """

    match_template("kasia@gmail.com", [leggin_with_size_m], expected_message)


def test_message_more_leggins(leggin_with_size_m, leggin_with_size_s):
    expected_message = """
        Hello kasia@gmail.com,

        We have found products which meet your criteria:

        * Szwowe Czarne (50.00 PLN) - https://www.myprotein.pl/11871452.html
        * Power Curve (60.00 PLN) - https://www.myprotein.pl/11871452.html

        Happy hunting!
    """

    match_template(
        "kasia@gmail.com", [leggin_with_size_m, leggin_with_size_s], expected_message
    )


def test_message_no_leggins():
    expected_message = """
        Hello kasia@gmail.com,

        We have not found products which meet your criteria.

        Happy hunting!
    """

    match_template("kasia@gmail.com", [], expected_message)
