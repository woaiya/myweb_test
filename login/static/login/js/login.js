$(document).ready(function(){
  $("#sum").click(function(){
    var a = $("#a").val();
    var b = $("#b").val();

    $.post("{% url 'login:login_ajax' %}",{'a':a,'b':b}, function(res){
        $('#result').show().text(res.sum)
    })
  });
});