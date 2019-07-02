function loginForm() {
    var x = document.forms["login"]["username"].value;
    var y = document.forms["login"]["password"].value;
    if (x === ""){
        alert("用户名不能为空！");
        return false;
    }else if (y === ""){
        alert("密码不能为空！");
        return false;
    }else {
        if (x.length < 6) {
            alert("用户名不能少于6位！");
            return false;
        }else if (y.length < 6) {
            alert("密码不能少于6位！");
            return false;
        }
    }
}