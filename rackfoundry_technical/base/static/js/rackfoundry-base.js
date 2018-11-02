function char_click(char_json) {
    if ($(".char-modal-bg").is(":hidden"))
    {
        $(".char-modal-bg").css("display", "block");
    }
    else
    {
        $(".char-modal-bg").hide();
    }

    var parsed_json = JSON.stringify(char_json);
    window.alert(parsed_json);
    return false;
}

function modal_close() {
    if ($(".char-modal-bg").is(":visible"))
    {
        $(".char-modal-bg").hide();
    }

    return false;

}

