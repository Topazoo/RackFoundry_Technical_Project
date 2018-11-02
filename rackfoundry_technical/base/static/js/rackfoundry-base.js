function char_click(char_json) {
    if ($(".char-modal-bg").is(":hidden"))
    {
        $(".char-modal-bg").css("display", "block");

        var att = document.createAttribute("src");
        att.value = char_json.thumbnail.path + '.' + char_json.thumbnail.extension;

        document.getElementById("char-image").setAttributeNode(att);
        document.getElementById("char-name").innerHTML = char_json.name;
        document.getElementById("char-desc").innerHTML = "Description: " + unescape(char_json.description);
        window.alert(char_json.description)
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

