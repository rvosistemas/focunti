from django.core.mail import send_mail


def send_registration_email(username, email):
    subject = "Bienvenido a nuestro sitio"
    message = f"Hola {username}, gracias por registrarte en nuestro sitio."
    from_email = "noreply@example.com"
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
