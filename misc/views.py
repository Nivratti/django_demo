from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from notifications.signals import notify

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def mark_noti_as_read(request):
    """
    Mark notification as read
    
    Arguments:
        request {[type]} -- [description]
    """
    from notifications.models import Notification
    msg_id = request.POST.get("id")
    notifications = Notification.objects.filter(
        id=msg_id
    )
    for notification in notifications:
        # print(notification)
        notification.mark_as_read()

    response = {
        "success": 0,
        "message": {
            "type": "success",
            "title": "Success Info",
            "text": "Notification marked as read",
        },
    }
    return JsonResponse(response, safe=False)