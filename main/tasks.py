from mailing_list_project.celeryapp import app

from .service import send


@app.task
def send_list(name, last_name, birthday, list_mail, layout):
    send(name, last_name, birthday, list_mail, layout)
