from django.http import HttpResponse


def dummy(request):
    return HttpResponse(request.get_full_path())
