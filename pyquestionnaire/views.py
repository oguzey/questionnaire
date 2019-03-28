from django.shortcuts import redirect, render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def handle_form_data(request):
    if request.method == "POST":
        try:
            name = request.POST["Name"]
            color = request.POST["Color"]
            animal = request.POST["Animal"]
            all_data = "name={}, color={}, animal={}".format(name, color, animal)
            print("Got POST with: " + all_data)
            response = HttpResponse("Data were accepted: name={}, color={}, animal={}".format(name, color, animal))
            response["User-Data"] = all_data
            return response
        except Exception as error:
            if hasattr(error, 'message'):
                msg = error.message
            else:
                msg = str(error)
            response =  HttpResponse("Bad data: {}".format(str(request.POST)), status=500)
            response["Server-Error-Msg"] = msg
            return response
        pass
    else:
        msg = "{} method is not supported".format(request.method)
        response =  HttpResponse("Bad method", status=500)
        response["Server-Error-Msg"] = msg
        return response