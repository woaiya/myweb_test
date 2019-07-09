$(function () {
    $('btnAjax').click(function () {
        username = $('username').val();
        password = $('password').val();

        $.ajax({
            'url': '/login/login_ajax',
            'type': 'post',
            'data': {'username': username, 'password': password},
            'dataType': 'json'
        }).success(function (data) {
            if (data.res.code===400){
                $('#errmsg').show().html(data.res.msg)
            }else {
                location.href = '/blog/index'
            }
        })

    })

});