function message_box_control(json_param) {

    let notification_block = $('.notification_modal');
    let notification_block_header = $('.notification_modal #notification_header');
    let notification_block_message = $('.notification_modal .notification_body');
    let notification_block_date = $('.notification_date');

    if (getCookie(json_param.key) !== 'yes' && json_param.is_show === true) {
        notification_block_header.html(json_param.header);
        notification_block_message.html(json_param.message);
        notification_block_date.html(json_param.date);

        notification_block.modal('show');
    } else {
        notification_block.modal('hide');
    }

    notification_block.on('hidden.bs.modal', function () {
        setCookie(json_param.key, 'yes', 31536000);
    });

}




