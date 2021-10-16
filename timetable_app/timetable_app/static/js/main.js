initTheme();

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

function setTheme(theme = '') {

    let dark_color = '#3e3d3d';
    let light_color = '#ffffff';
    let body_obj = $('body');
    let theme_switcher_obj = $('.theme_switcher');

    let meta_theme_color = $('meta[name=theme-color]');
    let meta_msapplication_TileColor = $('meta[name=msapplication-TileColor]');
    let meta_msapplication_navbutton_color = $('meta[name=msapplication-navbutton-color]');
    let meta_apple_mobile_web_app_status_bar_style = $('meta[name=apple-mobile-web-app-status-bar-style]');

    if (theme === '') {
        if (theme_switcher_obj.hasClass('light')) {
            theme = 'light';
        } else {
            theme = 'dark';
        }
    }

    body_obj.removeClass("theme-light");
    body_obj.removeClass("theme-dark");
    if (theme === 'light') {
        theme_switcher_obj.removeClass('light');
        theme_switcher_obj.addClass('dark');
        theme_switcher_obj.html(
            '<svg class="dark_mode_icon" xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24px" viewBox="0 0 24 24" width="24px" fill="#000000">' +
            '<rect fill="none" height="24" width="24"/>' +
            '<path d="M9.37,5.51C9.19,6.15,9.1,6.82,9.1,7.5c0,4.08,3.32,7.4,7.4,7.4c0.68,0,1.35-0.09,1.99-0.27C17.45,17.19,14.93,19,12,19 c-3.86,0-7-3.14-7-7C5,9.07,6.81,6.55,9.37,5.51z M12,3c-4.97,0-9,4.03-9,9s4.03,9,9,9s9-4.03,9-9c0-0.46-0.04-0.92-0.1-1.36 c-0.98,1.37-2.58,2.26-4.4,2.26c-2.98,0-5.4-2.42-5.4-5.4c0-1.81,0.89-3.42,2.26-4.4C12.92,3.04,12.46,3,12,3L12,3z"/>' +
            '</svg>'
        );
        body_obj.addClass('theme-light');
        meta_theme_color.attr('content', light_color);
        meta_msapplication_TileColor.attr('content', light_color);
        meta_msapplication_navbutton_color.attr('content', light_color);
        meta_apple_mobile_web_app_status_bar_style.attr('content', light_color);
    } else {
        theme_switcher_obj.removeClass('dark');
        theme_switcher_obj.addClass('light');
        theme_switcher_obj.html(
            '<svg class="light_mode_icon" xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24px" ' +
            'viewBox="0 0 24 24" width="24px" fill="#000000"> <rect fill="none" height="24" width="24"/>' +
            '<path d="M12,9c1.65,0,3,1.35,3,3s-1.35,3-3,3s-3-1.35-3-3S10.35,9,12,9 M12,7c-2.76,0-5,2.24-5,5s2.24,5,5,5s5-2.24,5-5 S14.76,7,12,7L12,7z M2,13l2,0c0.55,0,1-0.45,1-1s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S1.45,13,2,13z M20,13l2,0c0.55,0,1-0.45,1-1 s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S19.45,13,20,13z M11,2v2c0,0.55,0.45,1,1,1s1-0.45,1-1V2c0-0.55-0.45-1-1-1S11,1.45,11,2z M11,20v2c0,0.55,0.45,1,1,1s1-0.45,1-1v-2c0-0.55-0.45-1-1-1C11.45,19,11,19.45,11,20z M5.99,4.58c-0.39-0.39-1.03-0.39-1.41,0 c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0s0.39-1.03,0-1.41L5.99,4.58z M18.36,16.95 c-0.39-0.39-1.03-0.39-1.41,0c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0c0.39-0.39,0.39-1.03,0-1.41 L18.36,16.95z M19.42,5.99c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06c-0.39,0.39-0.39,1.03,0,1.41 s1.03,0.39,1.41,0L19.42,5.99z M7.05,18.36c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06 c-0.39,0.39-0.39,1.03,0,1.41s1.03,0.39,1.41,0L7.05,18.36z"/>' +
            '</svg>'
        );
        body_obj.addClass('theme-dark');
        meta_theme_color.attr('content', dark_color);
        meta_msapplication_TileColor.attr('content', dark_color);
        meta_msapplication_navbutton_color.attr('content', dark_color);
        meta_apple_mobile_web_app_status_bar_style.attr('content', dark_color);
    }
    setCookie('theme', theme, 31536000)
}

function initTheme() {

    let installed_theme = getCookie('theme');
    if (installed_theme === undefined || installed_theme === 'light') {
        setTheme('light');
    } else {
        setTheme('dark');
    }


    $('.theme_switcher').click(function () {
        setTheme();
    });
}

$(document).ready(function () {
    initTheme();

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
        "key": "16_10_2021_update",
        "header": "Тёмная тема, загрузка в календарь",
        "message": "Здравствуйте, уважаемые студенты! <br><br>\
                  На сайт добавлена тёмная тема. <br>\
                  Включить/выключить можно в шапке сайта при помощи иконки: <svg class=\"dark_mode_icon\" xmlns=\"http://www.w3.org/2000/svg\" enable-background=\"new 0 0 24 24\" height=\"24px\" viewBox=\"0 0 24 24\" width=\"24px\" fill=\"#000000\"> <rect fill=\"none\" height=\"24\" width=\"24\"/> <path d=\"M9.37,5.51C9.19,6.15,9.1,6.82,9.1,7.5c0,4.08,3.32,7.4,7.4,7.4c0.68,0,1.35-0.09,1.99-0.27C17.45,17.19,14.93,19,12,19 c-3.86,0-7-3.14-7-7C5,9.07,6.81,6.55,9.37,5.51z M12,3c-4.97,0-9,4.03-9,9s4.03,9,9,9s9-4.03,9-9c0-0.46-0.04-0.92-0.1-1.36 c-0.98,1.37-2.58,2.26-4.4,2.26c-2.98,0-5.4-2.42-5.4-5.4c0-1.81,0.89-3.42,2.26-4.4C12.92,3.04,12.46,3,12,3L12,3z\"/></svg> / <svg class=\"light_mode_icon\" xmlns=\"http://www.w3.org/2000/svg\" enable-background=\"new 0 0 24 24\" height=\"24px\" viewBox=\"0 0 24 24\" width=\"24px\" fill=\"#000000\"> <rect fill=\"none\" height=\"24\" width=\"24\"/><path d=\"M12,9c1.65,0,3,1.35,3,3s-1.35,3-3,3s-3-1.35-3-3S10.35,9,12,9 M12,7c-2.76,0-5,2.24-5,5s2.24,5,5,5s5-2.24,5-5 S14.76,7,12,7L12,7z M2,13l2,0c0.55,0,1-0.45,1-1s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S1.45,13,2,13z M20,13l2,0c0.55,0,1-0.45,1-1 s-0.45-1-1-1l-2,0c-0.55,0-1,0.45-1,1S19.45,13,20,13z M11,2v2c0,0.55,0.45,1,1,1s1-0.45,1-1V2c0-0.55-0.45-1-1-1S11,1.45,11,2z M11,20v2c0,0.55,0.45,1,1,1s1-0.45,1-1v-2c0-0.55-0.45-1-1-1C11.45,19,11,19.45,11,20z M5.99,4.58c-0.39-0.39-1.03-0.39-1.41,0 c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0s0.39-1.03,0-1.41L5.99,4.58z M18.36,16.95 c-0.39-0.39-1.03-0.39-1.41,0c-0.39,0.39-0.39,1.03,0,1.41l1.06,1.06c0.39,0.39,1.03,0.39,1.41,0c0.39-0.39,0.39-1.03,0-1.41 L18.36,16.95z M19.42,5.99c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06c-0.39,0.39-0.39,1.03,0,1.41 s1.03,0.39,1.41,0L19.42,5.99z M7.05,18.36c0.39-0.39,0.39-1.03,0-1.41c-0.39-0.39-1.03-0.39-1.41,0l-1.06,1.06 c-0.39,0.39-0.39,1.03,0,1.41s1.03,0.39,1.41,0L7.05,18.36z\"/></svg>  <br>\
                  Так же появилась возможность выгрузить расписание в формате .ics для загрузки в календать Google, Outlook и другие.<br> \
                  --<br>\
                  С Уважением, Вячеслав\
                  <br><br>\
                  Для обратной связи: <a href=\"mailto:ya.slavar@yandex.ru\">ya.slavar@yandex.ru</a>",
                  // <br>\
                  // Последнее обновление расписания: " + update_timetable_date,
        "date": "16.10.2021"
    })

});