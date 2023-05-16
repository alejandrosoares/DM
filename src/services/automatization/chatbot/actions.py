"""Actions module define the actions to do in each topic"""

from contact.models import ContactInformation


def get_contact():
    contact = ContactInformation.objects.first()
    phone = contact.phone
    return f"""
    <p class="text-dark">You can contact us through:</p>
    <p class="text-muted">Phone: {phone} or
        <a href="https://api.whatsapp.com/send?phone={phone}">
            <i class="fa fa-whatsapp"></i> Whats app
        </a>
    </p>
    """


def get_location():
    contact = ContactInformation.objects.first()
    address = contact.address
    return f"""
        <p class="text-dark">We are in {address}.</p>
        <p class="text-dark">We wait you!!.</p>
        <a href="http://localhost:8000">Mi address</a>
        """


def get_opening_hours():
    return """
    Our opening hours are from 8 am to 5 pm
    """


def get_products():
    return """
    it costs 10 francs
    """


def get_another_action():
    return """
    I will put with a vendor. Just a moment please
    """


def get_welcome_greeting():
    return """
    Hello :) May I help you?
    """


def get_goodbye_greeting():
    return """
    See you soon
    """
