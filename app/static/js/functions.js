function message_error(obj) {
    var html = '<ul style="text-align: left; ">';
    $.each(obj, function (key, value) {
        console.log(key);
        console.log(value);
    });
    html += '</ul>';
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}