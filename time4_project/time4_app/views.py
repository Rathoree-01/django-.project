
from django.http import HttpResponse
from datetime import datetime,timedelta
def current_datetime(request):
 now1 = datetime.now() - timedelta(hours=4)
 now2 = datetime.now() + timedelta(hours=4)
 html = "<html><body>Current date and time 4hrs ago: {}<br>Current date and time 4hrs after: <br>{}</body></html>".format(now1,now2)
 return HttpResponse(html)

