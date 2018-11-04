function isNotEmpty(error_message) {
    /* Checks if a form field is empty */

    var val = document.getElementById("form-sub").value;

    if (val.trim() == "") {
        alert(error_message);
        return false;
    }

    return true;
}