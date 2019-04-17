function validatepass()
{ 
     var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("passwordconfirm").value;
    var uname = document.getElementById("uname").value;
    var email = document.getElementById("email").value;
     var phone = document.getElementById("phone").value;
     var fname = document.getElementById("fname").value;
     var lname = document.getElementById("lname").value;


    if(uname==''|| email==''|| phone==''||fname==''||lname=='')
    {
        swal("Invalid Information", "please check the informations you have entered", "info");
        return false;
    }
    if (password != confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }
    return true;

}


function validate_login()
{
    var uname = document.getElementById("uname").value
    var pass= document.getElementById("loginPassword").value

    if(uname ==''|| pass=='')
    {  
        swal("Invalid Information", "Empty username or password , please provide correct information", "info"); 
        return false;

    }
    return true 
}