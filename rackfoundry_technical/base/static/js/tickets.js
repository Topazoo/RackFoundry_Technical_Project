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

		if (!isNotEmpty('Please enter a ticket'))
		    return false;

        /* Send AJAX POST request */
		$.ajax({
				"type": "POST",
				"dataType": "json",
				"url": '/receive_ticket',
				"data": {'csrfmiddlewaretoken': token},
                /* Message on success */
                "success": function(response) {},
                /* Message on failure */
				"error": function(response) {},
        });

        return false;
    });
});
