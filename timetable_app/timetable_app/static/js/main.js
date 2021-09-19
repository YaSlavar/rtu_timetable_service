function getCookie(name) {
    let cookie_arr = document.cookie.split('; ');
    let cookie_obj = {};

    for (let i = 0; i < cookie_arr.length; i++) {
        let nv = cookie_arr[i].split('=');
        cookie_obj[nv[0]] = nv[1];
    }

    return cookie_obj[name];
}

function setCookie(name, value, set_sec) {
    let date = new Date(new Date().getTime() + set_sec * 1000);
    document.cookie = name + "=" + value + "; path=/; expires=" + date.toUTCString();
}


function formatDate(date) {

    function padNum(num) {
        return num.toString().padStart(2, '0');
    }

    let day = padNum(date.getDate());
    let monthIndex = padNum(date.getMonth() + 1);
    let year = date.getFullYear();

    return day + '.' + monthIndex + '.' + year;
}

$(document).ready(function () {

    window.onload = function () {
        location.href = "#top";
        location.href = "#" + formatDate(new Date);
    };


    $('.calendar_button').click(function () {
        $('.top_calendar').toggle();
    });

    $('.search_button').click(function () {
        $('#search_modal').modal('toggle');
    });

    $('.selected_element').click(function () {
        $('#search_modal').modal('toggle');
    });

    $('.download_button').click(function () {
        $('#get_ics_modal').modal('toggle');
    });

    $('.calendar').datepicker({
        format: "dd.mm.yyyy",
        language: "ru",
        todayHighlight: true,
        daysOfWeekHighlighted: '06'
    }).on('changeDate', function (e) {
        location.href = "#" + formatDate(e.date);
    });

    $('.top_calendar').datepicker({
        format: "dd.mm.yyyy",
        language: "ru",
        todayHighlight: true,
        daysOfWeekHighlighted: '06'
    }).on('changeDate', function (e) {
        $('.top_calendar').toggle();
        location.href = "#" + formatDate(e.date);
    });

    let search_modal = $("#search_modal");
    let get_ics_modal = $("#get_ics_modal");

    $('.select_group').select2({
        'width': '100%',
        'language': 'ru',
        'theme': 'bootstrap',
        'tags': true,
        'dropdownParent': search_modal
    });

    $('.select_teachers').select2({
        'width': '100%',
        'language': 'ru',
        'theme': 'bootstrap',
        'tags': true,
        'dropdownParent': search_modal
    });

    $('.select_rooms').select2({
        'width': '100%',
        'language': 'ru',
        'theme': 'bootstrap',
        'tags': true,
        'dropdownParent': search_modal
    });

    $('.select_ics_group').select2({
        'width': '100%',
        'language': 'ru',
        'theme': 'bootstrap',
        'tags': true,
        'dropdownParent': get_ics_modal
    });

    $('.select_welcome_group').select2({
        'width': '100%',
        'language': 'ru',
        'theme': 'bootstrap',
        'tags': true,
    });

    if (group_name) {
        setCookie('group_name', group_name, 31536000);
    }

    message_box_control({
        "is_show": true,
        "key": "08_02_2021_update",
        "header": "Обновление расписания",
        "message": "Здравствуйте, уважаемые студенты! <br><br>\
                  Сайт НЕ является официальным сайтом РТУ МИРЭА, при использовании расписания с этого сайта будьте внимательны! <br>\
                  Желаю успехов в учёбе :)<br>\
                  --<br>\
                  С Уважением, Вячеслав\
                  <br><br>\
                  Для обратной связи: <a href=\"mailto:ya.slavar@yandex.ru\">ya.slavar@yandex.ru</a> \
                  <br>\
                  Последнее обновление расписания: " + update_timetable_date,
        "date": "08.02.2021"
    })

});