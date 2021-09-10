from django.apps import AppConfig
import os.path
from datetime import datetime


class TimetableAppConfig(AppConfig):
    name = 'timetable_app'
    TIMETABLE_CONFIG = {
        # Почта для обратной связи
        'ADMIN_EMAIL': "ya.slavar@yandex.ru",

        # Первый день семестра, День должен быть понедельником!
        'START_DAY': "01.09.2021",

        # Поправка на количество недель, для того, чтобы первая неделя семестра была первой.
        'WEEK_DELTA': 34,

        # Номер семестра [1 - четный семестр, 2 - нечетный семестр]
        'SEMESTER_COUNT': 1,

        # Год поступления первого курса в текущем учебном году.
        'FIRST_COURSE_YEAR': 2021,

        # Постфиксы групп XX[XX]-XX-XX
        'GROUP_POSTFIX_DICT': {
            "bac": {
                "БО",
                "СО"
            },
            "mag": {
                "МО"
            }
        },

        # Описание групп
        'GROUP_DESCRIPTION': {
            "bac": "Бакалавриат / Специалитет",
            "mag": "Магистратура"
        },

        # Количество недель в семестре
        'WEEK_COUNT_DICT': {
            "semester": {  # тип расписания
                "bac": {  # тип группы
                    1: {  # четность семестра
                        1: 16,
                        2: 16,
                        3: 16,
                        4: 16,
                        5: 16  # номер курса : количество недель в семестре
                    },
                    2: {
                        1: 16,
                        2: 16,
                        3: 16,
                        4: 8,
                        5: 16
                    }
                },
                "mag": {  # тип группы
                    1: {  # четность семестра
                        1: 17,
                        2: 17  # номер курса : количество недель в семестре
                    },
                    2: {
                        1: 17,
                        2: 14
                    }
                }
            },
            "zach": {
                "bac": {  # тип группы
                    1: {  # четность семестра
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1,
                        5: 1  # номер курса : количество недель в зачетной неделе
                    },
                    2: {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1,
                        5: 1
                    }
                },
                "mag": {  # тип группы
                    1: {  # четность семестра
                        1: 0,
                        2: 0
                    },
                    2: {
                        1: 0,
                        2: 0
                    }
                }
            },
            "exam": {
                "bac": {  # тип группы
                    1: {  # четность семестра
                        1: 5,
                        2: 5,
                        3: 5,
                        4: 5,
                        5: 5  # номер курса : количество недель в сессии
                    },
                    2: {
                        1: 5,
                        2: 5,
                        3: 5,
                        4: 2,
                        5: 2
                    }
                },
                "mag": {  # тип группы
                    1: {  # четность семестра
                        1: 5,
                        2: 5,
                        3: 5,
                        4: 5,  # номер курса : количество недель в сессии
                    },
                    2: {
                        1: 3,
                        2: 0
                    }
                }
            }
        }
    }

    @staticmethod
    def get_create_date_db(path_to_file):
        return os.path.getmtime(path_to_file)
