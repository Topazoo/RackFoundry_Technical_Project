function create_link(link_text, href) {
    /* Create an <a> tag with a link
       @ link_text - The link text
       @ href - The URL to link to */

       var att = document.createAttribute("href");
       att.value = href;

       var a = document.createElement('a');
       a.setAttributeNode(att);
       var text = document.createTextNode(link_text);
       a.appendChild(text);

       return a;
}

function get_wiki(json_urls) {
    /* Find a wiki page link if in JSON
       @json_urls - The section of the JSON containing URLS */

        for (var i = 0; i < json_urls.length; i++)
            if(json_urls[i]["type"] === "wiki")
                return json_urls[i]["url"]

        return null;
}

function make_list(json_items, empty_placeholder) {
    /* Build an HTML list from JSON items
     @ json_items - A list of items from the JSON
     @ empty_placeholder - The message to insert if no items */

    var list = document.createElement('ul');

    /* If no elements to insert */
    if(json_items.length === 0)
    {
        /* Create a list element */
        var item = document.createElement('li');

        /* Insert text */
        item.appendChild(document.createTextNode(empty_placeholder));

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
    /* Insert content into modal
     @ char_json - A chunk of the search result JSON containing only information about the clicked character */

    /* Insert the full sized image in the modal */
    var att = document.createAttribute("src");
    att.value = char_json.thumbnail.path + '.' + char_json.thumbnail.extension;
    document.getElementById("char-image").setAttributeNode(att);

    /* Insert the character name */
    var name = document.createElement('p');
    name.innerHTML = char_json.name;
    document.getElementById("char-name").replaceChild(name, document.getElementById("char-name").childNodes[0]);

    /* var wiki = get_wiki(char_json["urls"]);
    if(wiki) {
        var a = create_link(char_json.name, wiki);
    }
    else {
        var a = document.createElement('p');
        a.innerHTML = char_json.name;
    } */ //TODO - Remove bc of irrelevant/incorrect wiki links

    /* Insert the character description */
    if (char_json.description.trim().length === 0 )
        document.getElementById("char-desc").innerHTML = "No Description.";
    else
        document.getElementById("char-desc").innerHTML = char_json.description; //TODO - replace unicode

    /* Insert a list of comics */
    var comic_list = make_list(char_json["comics"]["items"], "No comic appearances."); //TODO - Cap at 11 and allow for pagination
    var dom_comic_list = document.getElementById("char-comics");
    dom_comic_list.replaceChild(comic_list, dom_comic_list.childNodes[0]);

    /* Insert a list of series */
    var series_list = make_list(char_json["series"]["items"], "No series appearances."); //TODO - Cap at 11 and allow for pagination
    var dom_series_list = document.getElementById("char-series");
    dom_series_list.replaceChild(series_list, dom_series_list.childNodes[0]);

    /* Insert a list of stories */
    var stories_list = make_list(char_json["stories"]["items"], "No story appearances."); //TODO - Cap at 11 and allow for pagination
    var dom_stories_list = document.getElementById("char-stories");
    dom_stories_list.replaceChild(stories_list, dom_stories_list.childNodes[0]);
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

