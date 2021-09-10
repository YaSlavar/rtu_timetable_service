import calendar
from timetable_app.apps import TimetableAppConfig
from timetable_app.utils.timetable_controller import get_timetable_for_group, get_timetable_for_teacher, \
    get_timetable_for_classroom, get_schedule_calls
from collections import OrderedDict
from datetime import datetime, timedelta, time
import locale
from typing import Optional, Any


class Timetable:

    def __init__(self, config):
        locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
        self.config = config
        self.schedule_calls = get_schedule_calls()

    @staticmethod
    def get_today_name(date: str) -> str:
        """
        Получение наименования дня
        :param date: Дата d.m.Y
        :return: Наименования дня
        """
        today = datetime.today().date()
        date = datetime.strptime(date, '%d.%m.%Y').date()
        if date == today:
            return "Сегодня"
        elif date == today + timedelta(days=1):
            return "Завтра"
        elif date == today + timedelta(days=2):
            return "Послезавтра"
        else:
            return ""

    @staticmethod
    def get_day_name(day: int) -> str:
        """
        Получение названия дня недели
        :param day: Номер дня недели
        :return: Названия дня недели
        """

        return calendar.day_name[day - 1].capitalize()

    @staticmethod
    def get_timetable_type(week_count_dict: dict, week: int) -> Optional[Any]:
        """
        Получение типа периода обучения в зависимости от указанной недели
        :param week_count_dict: Стоварь количества недель
            {вид семестра: {степень подготовки: {четность семестра: {номер курса: количество недель}}}}
        :param week: Неделя (текущая)
        :return: Типа периода обучения [semester, zach, exam]
        """
        _week_count = 0
        for semester_type, week_count_dict in week_count_dict.items():
            _week_count += week_count_dict
            if week <= week_count_dict:
                return semester_type
        return None

    @staticmethod
    def get_day(date_obj) -> int:
        """
        Получение номера дня недели
        :param date_obj: Дата d.m.Y
        :return: Номер дня недели
        """
        return int(date_obj.strftime('%w'))

    @staticmethod
    def get_week(date_obj, week_delta: int) -> int:
        """
        Получение номера недели с поправкой на количество недель (delta)
        :param date_obj: Дата
        :param week_delta: Дельта недель
        :return: Номер недели
        """
        return int(date_obj.strftime('%W')) - week_delta

    @staticmethod
    def get_date_list(date_start: str, day_count: int) -> list[str]:
        """
        Получение списка дат
        :rtype: Список дат list
        """
        date_obj = datetime.strptime(date_start, '%d.%m.%Y')
        date_list = [date_start]
        for i in range(day_count + 1):
            calc_date = date_obj + timedelta(i)
            date_list.append(calc_date.strftime('%d.%m.%Y'))

        return date_list

    @staticmethod
    def get_day_count_from_week(week_count: int) -> int:
        """
        Получение количества дней от количества недель
        :rtype: Количество дней
        """
        return week_count * 7

    @staticmethod
    def is_show(lesson_info: dict, week: int) -> dict:
        """
        Проверка на необходимость отображения занятия для текущей недели
        :param lesson_info: информация о занятии
        :param week: номер недели
        :return: информация о занятии с/без признака отображения
        """
        lesson_info['show'] = ''

        if lesson_info['exception'] != '':
            if isinstance(lesson_info['exception'], str):
                lesson_info['exception'] = lesson_info['exception'].replace("'", "")
                lesson_info['exception'] = list(map(int, lesson_info['exception'].split(", ")))

        if lesson_info['include'] != '':
            if isinstance(lesson_info['include'], str):
                lesson_info['include'] = lesson_info['include'].replace("'", "")
                lesson_info['include'] = list(map(int, lesson_info['include'].split(", ")))

        if lesson_info['include'] == '' and lesson_info['exception'] == '':
            lesson_info['show'] = True

        if isinstance(lesson_info['include'], list):
            if week in lesson_info['include']:
                lesson_info['show'] = True

        if isinstance(lesson_info['exception'], list):
            if week in lesson_info['exception']:
                lesson_info['show'] = False
            else:
                lesson_info['show'] = True

        return lesson_info

    def get_timetable_on_day(self, timetable_info_list: list, date: object, day: int, week: int,
                             timetable_type: str) -> dict:
        """
        Получение распиания для одного дня
        :param timetable_info_list: Список занятий
        :param date: Дата
        :param day: Номер дня недели
        :param week: Номер недели с поправкой
        :param timetable_type: тип расписания
        :return: dict расписание
        """

        result_timetable = {}

        # Четность недели
        if week % 2 == 0:
            parity_week = 2
        else:
            parity_week = 1

        if timetable_type == 'all':
            timetable_type = ['semester', 'zach', 'exam']
        else:
            timetable_type = [timetable_type]

        result_timetable['day_name'] = self.get_day_name(day)
        result_timetable['week_num'] = week
        result_timetable['today_name'] = self.get_today_name(date.strftime('%d.%m.%Y'))
        result_timetable['lessons'] = {}

        for call_time_dict in self.schedule_calls:
            result_timetable['lessons'][call_time_dict['call_time']] = {}

        for lesson_info in timetable_info_list:

            if isinstance(lesson_info['call_time'], time):
                lesson_info['call_time'] = lesson_info['call_time'].strftime('%H:%M')

            if (lesson_info['day'] == day and lesson_info['week'] == parity_week) or lesson_info['date'] == date:
                lesson_info = self.is_show(lesson_info, week)
                if lesson_info['show'] != '' and lesson_info['occupation'] in timetable_type:
                    result_timetable['lessons'][lesson_info['call_time']] = lesson_info

        result_timetable['lessons'] = OrderedDict(sorted(result_timetable['lessons'].items()))
        return result_timetable

    def get_timetable(self, date_str: str) -> dict:
        """
        Получение расписания на определенную дату
        :param date_str: Дата d.m.Y
        :return: dict расписания
        """
        raise NotImplementedError  # Должны реализовать дочерние классы

    def get_timetable_today(self):
        """
        Получение расписания на сегодня
        :return: информация о занятии с/без признака отображения
        """
        date_today = datetime.today().date().strftime('%d.%m.%Y')
        return self.get_timetable(date_today)


class StudentTimetable(Timetable):
    class Group:
        def __init__(self, config: dict, group: str):
            """
            Класс навания группы XX[XX]-XX-XX
            :param config: Параметры конфигурации
            :param group: Название группы XX[XX]-XX-XX
            """
            self.config = config

            self.group_name = group
            self.group_type = self.get_group_type(self.group_name)
            self.course_num = self.get_course_num(self.config['FIRST_COURSE_YEAR'], self.group_name)
            self.semester_week_count = self.get_semester_week_count_dict(self.group_name,
                                                                         self.config['WEEK_COUNT_DICT'],
                                                                         self.config['SEMESTER_COUNT'],
                                                                         self.config['FIRST_COURSE_YEAR'])

        @staticmethod
        def get_group_type(group: str) -> str:
            """
            Получение типа группы
            :param group: Название группы XX[XX]-XX-XX
            :return: тип группы [mag, bac]
            """
            group_postfix = {
                'bac': [
                    'БО',
                    'СО'
                ],
                'mag': [
                    'МО'
                ]
            }

            def get_group_postfix(group_name: str) -> str:
                """
                Получение постфикса группы XX[XX]-XX-XX, где
                - 3 символ -> степень подготовки
                    [Б - бакалавриат, С - специалитет, М - магистратура]
                - 4 символ -> вид обучения
                    [О - очный, З - заочный, В - вечерний]
                :param group_name: Название группы
                :return: постфикс группы
                """
                return group_name[2:4]

            postfix = get_group_postfix(group)
            group_type = None
            for group_postfix_key in group_postfix:
                if postfix in group_postfix[group_postfix_key]:
                    group_type = group_postfix_key

            return group_type

        @staticmethod
        def get_course_num(first_course_year: int, group: str) -> int:
            """
            Получение номера курса группы
            :param first_course_year: Год поступления первого курса
            :param group: Название группы
            :return: Номер курса
            """
            group_year = 2000 + int(group[8:10])
            return first_course_year - group_year + 1

        def get_semester_week_count_dict(self, group: str, week_count_dict: dict, semester_count: int,
                                         first_course_year: int) -> dict:
            """
            Получение количества недель в семестре
            :param group: Название группы
            :param week_count_dict: Стоварь количества недель
                {вид семестра: {степень подготовки: {четность семестра: {номер курса: количество недель}}}}
            :param semester_count: четность семестра [1- нечетный, 2- четный]
            :param first_course_year: год поступления первого курса
            :return: dict количество недель для каждого периода обучения
            """
            group_type = self.get_group_type(group)
            course_num = self.get_course_num(first_course_year, group)

            semester_week_count = {}
            for timetable_type, group_type_dict in week_count_dict.items():
                semester_week_count[timetable_type] = group_type_dict[group_type][semester_count][course_num]

            return semester_week_count

    def __init__(self, config: dict, group: str):
        """
        Получение расписания студента
        :param config: Конфигурация
        :param group: Название группы
        """
        super().__init__(config)
        self.group = self.Group(self.config, group)

    def get_timetable(self, date_str: str) -> dict:
        """
        Получение расписания на определенную дату
        :param date_str: Дата d.m.Y
        :return: dict расписания
        """

        date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
        day = self.get_day(date_obj)
        week = self.get_week(date_obj, self.config['WEEK_DELTA'])

        timetable_type = self.get_timetable_type(self.group.semester_week_count, week)

        timetable_info_list = get_timetable_for_group(self.group.group_name)

        timetable_dict = self.get_timetable_on_day(timetable_info_list, date_str, day, week, timetable_type)

        return timetable_dict

    def get_all_timetable(self):
        """
        Получение всего расписания
        :return:
        """
        week_count = 0
        for period_name, week_count_for_period in self.group.semester_week_count.items():
            week_count += week_count_for_period

        day_count = self.get_day_count_from_week(week_count)
        date_list = self.get_date_list(self.config['START_DAY'], day_count)

        timetable_info_list = get_timetable_for_group(self.group.group_name)

        timetable_dict = {}

        for date_str in date_list:
            date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
            day = self.get_day(date_obj)
            week = self.get_week(date_obj, self.config['WEEK_DELTA'])

            timetable_type = self.get_timetable_type(self.group.semester_week_count, week)

            timetable_dict_for_one_day = self.get_timetable_on_day(timetable_info_list, date_obj, day, week,
                                                                   timetable_type)
            timetable_dict[date_str] = timetable_dict_for_one_day

        return timetable_dict


class TeacherTimetable(Timetable):
    class Teacher:
        def __init__(self, name):
            """
            Класс ФИО преподавателя
            :param name: ФИО преподавателя
            """
            self.teacher_name = name

    def __init__(self, config: dict, teacher_name: str):
        """
        Получение расписания преподавателя
        :param config: Конфигурация
        :param teacher_name: ФИО преподавателя
        """
        super().__init__(config)
        self.teacher = self.Teacher(teacher_name)

    def get_timetable(self, date_str: str) -> dict:
        """
        Получение расписания на определенную дату
        :param date_str: Дата d.m.Y
        :return: dict расписания
        """

        date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
        day = self.get_day(date_obj)
        week = self.get_week(date_obj, self.config['WEEK_DELTA'])

        timetable_type = 'all'

        timetable_info_list = get_timetable_for_teacher(self.teacher.teacher_name)

        timetable_dict = self.get_timetable_on_day(timetable_info_list, date_str, day, week, timetable_type)

        return timetable_dict

    def get_all_timetable(self):
        """
        Получение всего расписания
        :return:
        """
        week_count = 21  # TODO: Поправить вычисление количества недель для преподавателей

        day_count = self.get_day_count_from_week(week_count)
        date_list = self.get_date_list(self.config['START_DAY'], day_count)

        timetable_info_list = get_timetable_for_teacher(self.teacher.teacher_name)

        timetable_dict = {}

        for date_str in date_list:
            date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
            day = self.get_day(date_obj)
            week = self.get_week(date_obj, self.config['WEEK_DELTA'])

            timetable_type = ""  # TODO: Тоже что-то нужно с этим сделать

            timetable_dict_for_one_day = self.get_timetable_on_day(timetable_info_list, date_obj, day, week,
                                                                   timetable_type)
            timetable_dict[date_str] = timetable_dict_for_one_day

        return timetable_dict


class ClassroomTimetable(Timetable):
    class Classroom:
        def __init__(self, room):
            """
            Класс аудитории
            :param room: Номер аудитории
            """
            self.classroom = room

    def __init__(self, config: dict, classroom: str):
        """
        Получение расписания преподавателя
        :param config: Конфигурация
        :param classroom: Номер аудитории
        """
        super().__init__(config)
        self.classroom = self.Classroom(classroom)

    def get_timetable(self, date_str: str) -> dict:
        """
        Получение расписания на определенную дату
        :param date_str: Дата d.m.Y
        :return: dict расписания
        """

        date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
        day = self.get_day(date_obj)
        week = self.get_week(date_obj, self.config['WEEK_DELTA'])

        timetable_type = 'all'

        timetable_info_list = get_timetable_for_classroom(self.classroom.classroom)

        timetable_dict = self.get_timetable_on_day(timetable_info_list, date_str, day, week, timetable_type)

        return timetable_dict

    def get_all_timetable(self):
        """
        Получение всего расписания
        :return:
        """
        week_count = 21  # TODO: Поправить вычисление количества недель для преподавателей

        day_count = self.get_day_count_from_week(week_count)
        date_list = self.get_date_list(self.config['START_DAY'], day_count)

        timetable_info_list = get_timetable_for_teacher(self.classroom.classroom)

        timetable_dict = {}

        for date_str in date_list:
            date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
            day = self.get_day(date_obj)
            week = self.get_week(date_obj, self.config['WEEK_DELTA'])

            timetable_type = ""  # TODO: Тоже что-то нужно с этим сделать

            timetable_dict_for_one_day = self.get_timetable_on_day(timetable_info_list, date_obj, day, week,
                                                                   timetable_type)
            timetable_dict[date_str] = timetable_dict_for_one_day

        return timetable_dict


if __name__ == "__main__":
    timetable = StudentTimetable(TimetableAppConfig.TIMETABLE_CONFIG, 'ИНМО-01-20')

    print(timetable.get_timetable('23.02.2021'))
    print(timetable.get_timetable('24.02.2021'))
    print(timetable.get_timetable_today())

    timetable = TeacherTimetable(TimetableAppConfig.TIMETABLE_CONFIG, 'Зуев')

    print(timetable.get_timetable('23.02.2021'))
    print(timetable.get_timetable('24.02.2021'))
    print(timetable.get_timetable_today())

    timetable = ClassroomTimetable(TimetableAppConfig.TIMETABLE_CONFIG, 'Г-310')

    print(timetable.get_timetable('23.02.2021'))
    print(timetable.get_timetable('24.02.2021'))
    print(timetable.get_timetable_today())
