from django.shortcuts import render


def handler403(request, exception):
    return render(request, "core/403.html", status=403)
