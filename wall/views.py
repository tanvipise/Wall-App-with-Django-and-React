from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Wall

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    # return HttpResponse("<h1> Hi There </h1>")
    return render(request, "pages/home.html", context = {}, status = 200)

def wall_items_view(request, *args, **kwargs):
   """
   REST API VIEW
   Consume by Javascript 
   return json data
   """  
   #qs= list of django model objs
   qs = Wall.objects.all()   
   wall_items = [{"id": x.id, "content": x.content} for x in qs]
   data = {
      "response": wall_items,
      "isUser": False,
   }
   return JsonResponse(data)


def wall_detail_view(request, wall_id, *args, **kwargs):
   """
   REST API VIEW
   Consume by Javascript 
   return json data
   """
   
   data = {
# take data and response into JsonResponse obj
         "id": wall_id,
   }
   status = 200
   try:
      obj = Wall.objects.get(id=wall_id)
      data['content'] = obj.content
   except:
      data['message'] = "Not found"
      status = 404
   
   return JsonResponse(data, status = status) #json.dumps content_type='application/json
   #passing status as arg to response object
   
    
