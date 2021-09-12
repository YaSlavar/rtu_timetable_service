# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from timetable_app import models
from timetable_app.utils.timetable_generator import StudentTimetable, TeacherTimetable, ClassroomTimetable
from timetable_app.utils.timetable_controller import get_group_names, get_teacher_names, get_rooms
from timetable_app.utils.calendar_generator import CalendarGenerator
from timetable_app.apps import TimetableAppConfig
from datetime import datetime
from timetable.settings import DATABASES


def index(request):
    """
    Главная страница и страница с расписанием
    :param request:
    :return:
    """

    update_timetable_date = datetime.fromtimestamp(
        TimetableAppConfig.get_create_date_db(DATABASES['default']['NAME'])).strftime('%d.%m.%Y')

    try:
        group_name = request.COOKIES.get('group')
    except KeyError:
        group_name = ''

    groups_list = get_group_names()
    teacher_names_list = get_teacher_names()
    rooms_list = get_rooms()

    data = {
        'admin_email': TimetableAppConfig.TIMETABLE_CONFIG['ADMIN_EMAIL'],
        'today_date': datetime.now().strftime('%d.%m.%Y'),
        'update_timetable_date': update_timetable_date,
        'groups_list': groups_list,
        'teacher_names_list': teacher_names_list,
        'rooms_list': rooms_list
    }

    if 'group' in request.GET or group_name:
        try:
            group_name = request.GET['group']
        except KeyError:
            group_name = group_name

        if group_name != '':
            timetable = StudentTimetable(TimetableAppConfig.TIMETABLE_CONFIG, group_name)
            timetable_dict = timetable.get_all_timetable()

            data['identity_name'] = group_name
            data['timetable'] = timetable_dict

    elif 'teacher' in request.GET:
        teacher_name = request.GET['teacher']
        timetable = TeacherTimetable(TimetableAppConfig.TIMETABLE_CONFIG, teacher_name)
        timetable_dict = timetable.get_all_timetable()

        data['identity_name'] = teacher_name
        data['timetable'] = timetable_dict

    elif 'room' in request.GET:
        room_name = request.GET['room']
        timetable = ClassroomTimetable(TimetableAppConfig.TIMETABLE_CONFIG, room_name)
        timetable_dict = timetable.get_all_timetable()

        data['identity_name'] = room_name
        data['timetable'] = timetable_dict

    else:
        pass

    if 'timetable' in data:
        response = render(request, 'timetable_app/index.html', context=data)
    else:
        response = render(request, 'timetable_app/welcome.html', context=data)

    return response


def get_ics(request):
    """
    Получение расписания в формате ICS
    :param request:
    :return:
    """
    datetime_str = datetime.strftime(datetime.now(), "%d.%m.%Y_%H.%M.%S")

    group = request.POST['group']

    if group:
        timetable = StudentTimetable(TimetableAppConfig.TIMETABLE_CONFIG, group)

        if request.POST['date_from'] and request.POST['date_to']:
            start_date = datetime.strftime(datetime.strptime(request.POST['date_from'], "%Y-%m-%d"), "%d.%m.%Y")
            end_date = datetime.strftime(datetime.strptime(request.POST['date_to'], "%Y-%m-%d"), "%d.%m.%Y")
            all_timetable = timetable.get_timetable_by_dates(start_date, end_date)
        else:
            all_timetable = timetable.get_all_timetable()

        cal = CalendarGenerator('test', all_timetable, 1)
        cal.generate_calendar_events()
        calendar_file_content = cal.return_calendar_as_text()

        filename = "{}.ics".format(datetime_str)
        print(filename)

        response = HttpResponse(calendar_file_content, content_type='text/plain; charset=UTF-8')
        response['Content-Disposition'] = ('attachment; filename={0}'.format(filename))
        return response
