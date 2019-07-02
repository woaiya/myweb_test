function loginForm() {
    var x = document.forms["login"]["username"].value;
    var y = document.forms["login"]["password"].value;
    if (x === ""){
        document.getElementById("usernameError").innerHTML = "用户名不能为空！";
        return false;
    }else if (y === ""){
        document.getElementById("passwordError").innerHTML = "密码不能为空！";
        return false;
    }else {
        if (x.length < 6) {
            document.getElementById("usernameError").innerHTML = "用户名不能少于6位！";
            return false;
        }else if (y.length < 6) {
            document.getElementById("passwordError").innerHTML = "密码不能少于6位！";
            return false;
        }
    }
}