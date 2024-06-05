function validateForm(event) {
    const form = event.target;
    const fullName = form.querySelector('#firstName').value.trim();
    const gender = form.querySelector('input[name="gender"]:checked');
    const email = form.querySelector('#email').value.trim();
    const birthDate = form.querySelector('input[name="birthDate"]').value.trim();
    const message = form.querySelector('#message').value.trim();

    if (!fullName || !gender || !email || !birthDate || !message) {
        alert('Please fill in all fields');
        event.preventDefault();
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const firstName = document.getElementById('firstName');
    const email = document.getElementById('email');
    const birthDate = document.querySelector('input[name="birthDate"]');
    const message = document.getElementById('message');
    const genderRadios = document.querySelectorAll('input[name="gender"]');

    form.addEventListener('submit', function(event) {
        let valid = true;

        // Clear previous error messages
        clearErrors();

        // Validate Full Name
        if (!validateNotEmpty(firstName.value)) {
            showError(firstName, "Full name cannot be empty.");
            valid = false;
        }

        // Validate Gender
        if (!validateGender(genderRadios)) {
            showError(genderRadios[0].parentElement, "Please select your gender.");
            valid = false;
        }

        // Validate Email
        if (!validateNotEmpty(email.value)) {
            showError(email, "Email cannot be empty.");
            valid = false;
        } else if (!validateEmail(email.value)) {
            showError(email, "Please enter a valid email address.");
            valid = false;
        }

        // Validate Date of Birth
        if (!validateNotEmpty(birthDate.value)) {
            showError(birthDate, "Date of birth cannot be empty.");
            valid = false;
        }

        // Validate Message
        if (!validateNotEmpty(message.value)) {
            showError(message, "Message cannot be empty.");
            valid = false;
        }

        // If any validation fails, prevent form submission
        if (!valid) {
            event.preventDefault();
        }
    });

    function validateNotEmpty(value) {
        return value.trim().length > 0;
    }

    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    function validateGender(radios) {
        for (let i = 0; i < radios.length; i++) {
            if (radios[i].checked) {
                return true;
            }
        }
        return false;
    }

    function showError(input, message) {
        const error = document.createElement('div');
        error.className = 'error';
        error.style.color = 'red';
        error.innerText = message;
        input.parentElement.appendChild(error);
    }

    function clearErrors() {
        const errors = document.querySelectorAll('.error');
        errors.forEach(function(error) {
            error.remove();
        });
    }
});
