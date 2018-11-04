function getCookie(name) {
    /* Get a cookie */

    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    /* Set CSRF token */

    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

$(document).ready(function() {
    /* POST to tickets endpoint */

    $("#post-ticket").click(function() {
		token = String(getCookie('csrftoken'));

		if (!isNotEmpty('Please enter the required ticket information.'))
		    return false;

        var ticket = document.getElementById("form-sub").value;

        /* Send AJAX POST request */
		$.ajax({
				"type": "POST",
				"dataType": "text",
				"url": 'receive/',
				"data": {'csrfmiddlewaretoken': token, 'ticket':ticket},
                /* Message on success */
                success: function(response) {
                    alert("Ticket submitted successfully!")
                },

                /* Message on failure */
				error: function(response) {
				    alert(response.responseText)
				},
        });

        return false;
    });
});
