from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from web.models import Teacher, Subject, Room, StudentInRoom,Absent, TeacherInRoom

# Create your views here.
def index(request):

    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    rooms = Room.objects.all()
    absents = Absent.objects.all()

    teach_time = ''
    time= ''
    subject=''
    teacher=''
    room=''
    student_in_room =[]

    if request.method == 'POST':
        print(request.POST)
        teach_time = request.POST.get('teach_time')
        teach_date = datetime.strptime(teach_time, '%d/%m/%Y')

        time = request.POST.get('time')
        subject = request.POST.get('subject')
        teacher = request.POST.get('teacher')
        room = request.POST.get('teacher')

        room_select = Room.objects.get(pk=room)

        teacher_select = Teacher.objects.get(pk=teacher)
        subject_select = Subject.objects.get(pk=subject)


        teacherInRoom = TeacherInRoom.objects.filter(time = time, subject= subject_select, \
                                     teacher=teacher_select, room =room_select,\
                                     teach_date = teach_date).first()

        if teacherInRoom is None:
            teacherInRoom = TeacherInRoom(time = time, subject= subject_select, \
                                     teacher=teacher_select, room =room_select,\
                                     teach_date = teach_date)
            teacherInRoom.save()

        student_in_room = StudentInRoom.objects.filter(room=room_select).all()

    context = {'teachers': teachers,
               'subjects': subjects,
               'rooms': rooms,
               'absents': absents,
               'teach_time': teach_time,
               'time': time,
               'subject': subject,
               'teacher': teacher,
               'room': room,
               'student_in_room':student_in_room
               }

    return render(request, 'index.html', context)


def viewstudentinroom(request):

    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    rooms = Room.objects.all()
    absents = Absent.objects.all()

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
        student_in_room = StudentInRoom.objects.filter(room=room_select).all()
        print(students)
    context = {'teachers': teachers,
               'subjects': subjects,
               'rooms': rooms,
               'absents': absents,
               'teach_time': teach_time,
               'time': time,
               'subject': subject,
               'teacher': teacher,
               'room': room,
               'student_in_room':student_in_room
               }

    return render(request, 'index.html', context)