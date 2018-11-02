function make_list(json_items) {
    /* Build an HTML list from JSON items */

    var list = document.createElement('ul');

    /* If no elements to insert */
    if(json_items.length === 0)
    {
        /* Create a list element */
        var item = document.createElement('li');

        /* Insert text */
        item.appendChild(document.createTextNode("None"));

        /* Add to list */
        list.appendChild(item);
    }

    /* Otherwise insert all elements */
    else {
        for (var i = 0; i < json_items.length; i++) {
            /* Create the list element */
            var item = document.createElement('li');

            /* Insert text from JSON */
            item.appendChild(document.createTextNode(json_items[i]["name"]));

            /* Add to list */
            list.appendChild(item);
        }
    }

    return list;
}

function build_modal(char_json) {
    /* Insert content into modal */

    /* Insert the full sized image in the modal */
    var att = document.createAttribute("src");
    att.value = char_json.thumbnail.path + '.' + char_json.thumbnail.extension;
    document.getElementById("char-image").setAttributeNode(att);

    /* Insert the character name */
    document.getElementById("char-name").innerHTML = char_json.name;

    /* Insert the character description */
    if (char_json.description.trim().length === 0 )
        document.getElementById("char-desc").innerHTML = "Description: None";
    else
        document.getElementById("char-desc").innerHTML = "Description: " + char_json.description; //TODO - replace unicode

    /* Insert a list of comics */
    var comic_list = make_list(char_json["comics"]["items"]);
    var dom_comic_list = document.getElementById("char-comics");
    dom_comic_list.replaceChild(comic_list, dom_comic_list.childNodes[0]);

    //TODO - Build series list
    //TODO - Build stories list
}

function char_click(char_json) {
    /* Display modal on character thumbnail click
       @ char_json - A chunk of the search result JSON containing only information about the clicked character */

    /* If the modal is not displayed */
    if ($(".char-modal-bg").is(":hidden"))
    {
        /* Display the modal */
        $(".char-modal-bg").css("display", "block");

        /* Fill the modal */
        build_modal(char_json);
    }
    else
        $(".char-modal-bg").hide();

    return false;
}

function modal_close() {
    /* Close the modal on X button click */

    if ($(".char-modal-bg").is(":visible"))
        $(".char-modal-bg").hide();

    return false;

}

