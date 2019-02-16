
from django.shortcuts import render
from django.http import HttpResponse
from web.models import Teacher, Subject, Room, StudentInRoom

# Create your views here.
def index(request):

    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    rooms = Room.objects.all()

    teach_time = ''
    time= ''
    subject=''
    teacher=''
    room=''
    students =[]

    if request.method == 'POST':
        print(request.POST)
        teach_time = request.POST.get('teach_time')
        time = request.POST.get('time')
        subject = request.POST.get('subject')
        teacher = request.POST.get('teacher')
        room = request.POST.get('teacher')

        room_select = Room.objects.get(pk=room)
        students = StudentInRoom.objects.filter(room=room_select).all()
        print(students)
    context = {'teachers': teachers,
               'subjects': subjects,
               'rooms': rooms,
               'teach_time': teach_time,
               'time': time,
               'subject': subject,
               'teacher': teacher,
               'room': room,
               'students':students
               }



    return render(request, 'index.html', context)
