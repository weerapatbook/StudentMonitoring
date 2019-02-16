from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from web.models import Teacher, Subject, Room, StudentInRoom,Absent, TeacherInRoom, StudentAbsent

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
    student_inroom_absent =[]

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


        for inroom in student_in_room:
            student_absent  = StudentAbsent.objects.filter(student = inroom.student, teacherinroom = teacherInRoom).first()

            if student_absent is None:
                student_absent = StudentAbsent(student = inroom.student, teacherinroom = teacherInRoom)
                student_absent.save()

            student_inroom_absent.append(student_absent)


    context = {'teachers': teachers,
               'subjects': subjects,
               'rooms': rooms,
               'absents': absents,
               'teach_time': teach_time,
               'time': time,
               'subject': subject,
               'teacher': teacher,
               'room': room,
               'student_inroom_absent':student_inroom_absent
               }

    return render(request, 'index.html', context)


def savestudentabsent(request):
    if request.method == 'POST':
        print(request.POST)
        student_inroom = request.POST.getlist('student_inroom')
        absent = request.POST.getlist('absent')

        for i in range(0, len(absent)):
            print("%s %s" %(student_inroom[i], absent[i]))
            studentAbsent = StudentAbsent.objects.get(pk=student_inroom[i])

            std_absent = Absent.objects.get(pk=absent[i])
            studentAbsent.absent = std_absent
            studentAbsent.save()
    context = {
               }

    return render(request, 'save.html', context)