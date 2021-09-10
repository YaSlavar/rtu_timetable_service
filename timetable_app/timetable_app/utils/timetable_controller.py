from timetable_app.models import *
from django.db.models import F
from datetime import datetime, time


def get_schedule_calls(call_list=None):
    """
    Получение списка звонков
    :param call_list: список звонков
    :return: списка звонков dict
    """
    if call_list is None:
        call_list = [1, 2, 3, 4, 5, 6]
    calls = ScheduleCalls.objects.all().filter(call_id__in=call_list)

    result_list = []
    for db_row in calls:
        if isinstance(db_row.call_time, time):
            db_row.call_time = db_row.call_time.strftime('%H:%M')
        row = {
            'call_num': db_row.call_id,
            'call_time': db_row.call_time,
        }
        result_list.append(row)

    return result_list


def get_group_names(group_name: str = ''):
    """
    Получение названия групп по шаблону
    :param group_name: название группы
    :return: названия групп dict
    """
    groups = Groups.objects.all().filter(group_name__contains=group_name)
    result_list = []
    for db_row in groups:
        result_list.append(db_row.group_name)

    return sorted(result_list)


def get_teacher_names(teacher_name: str = ''):
    """
    Получение ФИО преподавателей по шаблону
    :param teacher_name: Фамилия И.О. преподавателя
    :return: Фамилия И.О. преподавателя list
    """
    teachers = Teachers.objects.all().filter(teacher_name__contains=teacher_name)
    result_list = []
    for db_row in teachers:
        result_list.append(db_row.teacher_name)

    return sorted(result_list)


def get_rooms(room: str = ''):
    """
    Получение аудиторий
    :param room: Номер аудитории
    :return: Аудитории list
    """
    rooms = Rooms.objects.all().filter(room_num__contains=room)
    result_list = []
    for db_row in rooms:
        result_list.append(db_row.room_num)

    return sorted(result_list)


def get_timetable_for_group(group_name: str = 'ИНМО-01-20'):
    """
    Получение полного расписания для одной группы
    :param group_name: название группы
    :return: расписание list
    """
    table = Lessons.objects.filter(
        group_num__group_name__contains=group_name).annotate(group=F('group_num__group_name'),
                                                             occupation_name=F('occupation_id__occupation'),
                                                             discipline_name=F('discipline_id__discipline_name'),
                                                             teacher_name=F('teacher_id__teacher_name'),
                                                             call_time=F('call_num__call_time'),
                                                             lesson_type_name=F('lesson_type_id__lesson_type_name'),
                                                             room_num=F('room_id__room_num'))
    result_list = []
    for db_row in table:
        row = {
            'group': db_row.group,
            'occupation': db_row.occupation_name,
            'discipline': db_row.discipline_name,
            'teacher': db_row.teacher_name,
            'date': db_row.date,
            'day': db_row.day,
            'call_time': db_row.call_time,
            'week': db_row.week,
            'lesson_type': db_row.lesson_type_name,
            'room': db_row.room_num,
            'include': db_row.include,
            'exception': db_row.exception
        }
        result_list.append(row)
    return result_list


def get_timetable_for_teacher(teacher_name: str = 'Смирнов'):
    """
    Получение полного расписания для преподавателя
    :param teacher_name: Фамилия И.О. преподавателя
    :return: расписание dict
    """
    table = Lessons.objects.filter(
        teacher_id__teacher_name__contains=teacher_name).annotate(group=F('group_num__group_name'),
                                                                  occupation_name=F('occupation_id__occupation'),
                                                                  discipline_name=F('discipline_id__discipline_name'),
                                                                  teacher_name=F('teacher_id__teacher_name'),
                                                                  call_time=F('call_num__call_time'),
                                                                  lesson_type_name=F(
                                                                      'lesson_type_id__lesson_type_name'),
                                                                  room_num=F('room_id__room_num'))
    result_list = []
    for db_row in table:
        row = {
            'group': db_row.group,
            'occupation': db_row.occupation_name,
            'discipline': db_row.discipline_name,
            'teacher': db_row.teacher_name,
            'date': db_row.date,
            'day': db_row.day,
            'call_time': db_row.call_time,
            'week': db_row.week,
            'lesson_type': db_row.lesson_type_name,
            'room': db_row.room_num,
            'include': db_row.include,
            'exception': db_row.exception
        }
        result_list.append(row)
    return result_list


def get_timetable_for_classroom(classroom: str = '145б'):
    """
    Получение полного расписания для преподавателя
    :param classroom: Номер аудитории
    :return: расписание dict
    """
    table = Lessons.objects.filter(
        room_id__room_num__contains=classroom).annotate(group=F('group_num__group_name'),
                                                        occupation_name=F('occupation_id__occupation'),
                                                        discipline_name=F('discipline_id__discipline_name'),
                                                        teacher_name=F('teacher_id__teacher_name'),
                                                        call_time=F('call_num__call_time'),
                                                        lesson_type_name=F(
                                                            'lesson_type_id__lesson_type_name'),
                                                        room_num=F('room_id__room_num'))
    result_list = []
    for db_row in table:
        row = {
            'group': db_row.group,
            'occupation': db_row.occupation_name,
            'discipline': db_row.discipline_name,
            'teacher': db_row.teacher_name,
            'date': db_row.date,
            'day': db_row.day,
            'call_time': db_row.call_time,
            'week': db_row.week,
            'lesson_type': db_row.lesson_type_name,
            'room': db_row.room_num,
            'include': db_row.include,
            'exception': db_row.exception
        }
        result_list.append(row)
    return result_list
