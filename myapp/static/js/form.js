function validateForm() {
    let name = document.getElementById("firstName").value;
    let gender = document.querySelector('input[name="gender"]:checked').value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    let correct = 1;

    if (name == "" || email == "" || message == "" || gender == "") {
        alert("Please fill all the form.");
        correct = 0;
        return false;
    }

    let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        correct = 0;
        return false;
    }
    
    if(correct == 1){
        alert("Success!");
    }

    return true;
}