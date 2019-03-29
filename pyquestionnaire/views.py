from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.conf import settings
import sqlite3


class UserData(object):

    def __init__(self, name, color, animals):
        self.name = name.lower()
        self.color = color.lower()
        self.animals = animals.lower()

    def check(self):
        if self.name is None or len(self.name) == 0:
            return "Name was not provided"
        if self.color is None or len(self.color) == 0:
            return "Favourite color was not provided"
        if self.animals is None or len(self.animals) == 0:
            return "Animals were not provided"
        if self.animals not in ("cats", "dogs"):
            return "Bad value of 'Animals'. Possible values: cats, dogs"
        return "ok"

    def save(self):
        db_path = settings.DATABASES['default']['NAME']
        insert_query = "INSERT INTO user_data (name, color, animals) VALUES (?, ?, ?)"

        print("Connecting to DB: {}".format(db_path))
        con = sqlite3.connect(db_path)
        if con is None:
            return "Could not connect to sqlite3 DB: {}".format(db_path)
        try:
            cursor = con.cursor()
            cursor.execute(insert_query, (self.name, self.color, self.animals))
            con.commit()
            return "ok"
        except Exception as e:
            con.rollback()
            db_error = str(e)
            db_error_lower = db_error.lower()
            if db_error_lower.find("unique") != -1:
                return "Could not add data. Data from user '{}' have been already received".format(self.name.capitalize())
            else:
                return "DB error: {}".format(db_error)


def home(request):
    return render(request, 'index.html')


def gen_error_response(msg):
    print("Error: " + msg)
    response =  HttpResponse(msg, status=500)
    response["Questionnaire-Server-Error-Msg"] = msg
    return response


def handle_form_data(request):
    if request.method != "POST":
        return gen_error_response("{} method is not supported".format(request.method))

    # Handle POST method
    try:
        name = request.POST["Name"]
        color = request.POST["Color"]
        animals = request.POST["Animals"]
        print("Received data: name={}, color={}, animals={}".format(name, color, animals))

        data = UserData(name, color, animals)
        error_msg = data.check()
        if error_msg != "ok":
            return gen_error_response(error_msg)

        error_msg = data.save()
        if error_msg == "ok":
            return HttpResponse("Data were accepted")
        else:
            return gen_error_response(error_msg)
    except Exception as error:
        if hasattr(error, 'message'):
            error_msg = error.message
        else:
            error_msg = str(error)
        return gen_error_response("Bad data: {}".format(error_msg))
