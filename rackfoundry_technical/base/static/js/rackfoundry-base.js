function char_click() {
    if ($(".char-modal-bg").is(":hidden"))
    {
        $(".char-modal-bg").css("display", "block");
    }
    else
    {
        $(".char-modal-bg").hide();
    }
    return false;
}

function modal_close() {
    if ($(".char-modal-bg").is(":visible"))
    {
        $(".char-modal-bg").hide();
    }

    return false;

}

