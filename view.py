from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import ROOMS

@api_view(['GET', 'POST'])
def healthz(request):
    return Response(data={"status": "ok"})
    
@api_view(['GET'])
def rooms_info(request):
    if request.method == 'GET':
        l=[]
        d={}
        for i in DOGS.objects.all():
            l.append({
                "dog_id":i.id2,
                "age":i.age,
                "breed":i.breed,
                "gender":i.gender,
                "color":i.color})
            d["dogs"] = l
        
        return Response(status=200,data=d)

   
@api_view(['GET', 'POST', 'DELETE'])
def rooms_info1(request,id):
    if request.method == "GET":
        x = ROOMS.object.filter(room_id = id1)
        if len(x) == 0:
            return Response(status=404)
        else:
            d={}
            for i in x:
                d["room_id"]=i.room_id
                d["maximum_room_occupancy"]=i.maximum_room_occupancy
                d["guest_email"]=i.guest_email
                d["room_status"]=i.room_status
            return Response(status=200,data=d)
                
    elif request.method == 'POST':
        maximum_room_occupancy = request.data.get("maximum_room_occupancy")
        guest_email = request.data.get("guest_email")
        room_status = request.data.get("room_status")
        roomSecret = request.data.get("roomSecret")
        
        if roomSecret != "hFdRpJKls":
            return Response(status=401)
        else:
            Rooms(room_id=room_id, maximum_room_occupancy=maximum_room_occupancy, guest_email=guest_email, room_status=room_status).save()
            return Response(status=200)
            
    elif request.method == 'DELETE':
        removeRoomSecret = request.data.get("removeRoomSecret")
        if removeRoomSecret != "pLoRghtdp":
            return Response(status=401)
        x = ROOMS.object.filter(room_id = id)
        if len(x)==0:
            return Response(status=404)
        else:
            x.delete()
            return Response(status=200)
            
@api_view(["POST"])
def rooms_info2(request,id1):
    if request.method == "POST":
        email = request.data.get("email")
        reservationAdminCode = request.query_params.get("reservationAdminCode")
        if reservationAdminCode != "pFthaDepGyd":
            return Response(status=401)
        room=ROOMS.objects.filter(room_id=id1)
        if len(room)==0:
            return Response(status=404)
        else:
            if room[0].room_status=="reserved":
                return Response(status=400)
            else:
                room.update(room_status="reserved")
                return Response(status=200)
        
       
@api_view(["POST"])
def rooms_info2(request,id2):
    if request.method == "POST":
        email = request.data.get("email")
        reservationAdminCode = request.query_params.get("reservationAdminCode")
        if reservationAdminCode != "pFthaDepGyd":
            return Response(status=401)
        room=ROOMS.objects.filter(room_id=id1)
        if len(room)==0:
            return Response(status=404)
        else:
            if room[0].room_status=="unreserved":
                return Response(status=400)
            else:
                room.update(room_status="unreserved")
                return Response(status=200)
 
            
@api_view(["GET"])
def rooms_info4(request,id3):
    if request.method == 'GET':
        l=[]
        d={}
        for i in ROOMS.objects.all():
            if i.rooms==id3:
                l.append({
                    "room_id":i.room_id,
                    "maximum_room_occupancy":i.maximum_room_occupancy,
                    "guest_email":i.guest_email,
                    "room_status":i.room_status})
                          
                d["dogs"] = l
        return Response(status=200,data=d)
        
        
