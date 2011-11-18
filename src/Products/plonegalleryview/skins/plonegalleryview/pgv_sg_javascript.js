/*
 *  Javascript function collection
 *  ------------------------------
 *  Version  :   0.41
 *  Author   :   T.Hinze (HiDeVis)
 *  Date     :   16.05.2007    
 * 
 *  This scripts require the base_tools.js file >= 0.1 .
 *   
*/

var imgNum;

//#####################################
//---  image-zoom functions
//#####################################

/* ATMediaPage using LightBox JS for zoom-feature */


//#####################################
//---  generic functions
//#####################################

function antiLinkBorder(e) {
    /*  try to remove the border around active links (i.e. in mozilla-browsers)
    */
    var allLinksInPage = window.document.getElementsByTagName("a");
    for (var idx in allLinksInPage) {
        allLinksInPage[idx].onfocus = allLinksInPage[idx].blur;
    }
}
//---------------------------


//#####################################
//---  image autochange functions
//#####################################

function changeATMPImageSource(elemID, newURL, newTitle) {
    /*  try to reference the element with the id 'elemID'.
        If this element is an image object, then change the attribute
        'src' to the given newURL.
    */
    var ref = window.document.getElementById(elemID);
    //alert(elemID);
    var elemTitleID = "ATMP_ImageTitle";
    var refTitle    = window.document.getElementById(elemTitleID);
    var titleToken  = newTitle.split('|');
    var onlyTitle   = titleToken[0];
    var onlyDescr   = '';
    if (titleToken.length> 1)
        onlyDescr = titleToken[1];
            
    // change src of the image
    //alert(refTitle);
    if (ref && ref.tagName == "IMG") {
        ref.src = newURL;
        
        if (refTitle) {
            var textNode = document.createTextNode(onlyTitle);
            refTitle.replaceChild(textNode, refTitle.firstChild);
        }
        var parent  = ref.parentNode;
        if (parent.tagName == 'A') {
            // change the href of the link
            var token1      = newURL.split("/");
            var newID       = token1[token1.length - 2];
            var href        = parent.href;
            var token2      = href.split("/");
            var oldID       = token2[token2.length - 2];
            var href        = href.replace(oldID, newID).replace('/image_mini', '/image_large');
            parent.setAttribute('href', href);
            parent.setAttribute('title', newTitle);
        }
    }
}
//---------------------------

function autoChangeSideImage() {
    /*  This function will be called in a defined interval. At every call
        the 'src' attribute of the specified HTML-element (by id) will be
        changed with a value from the array 'allImages'.
        This array was created by the Python-script 'createAutoImagesJSCode_py.
    */
    var targetID    = "ATMP_AutochangeImage";
    var newURL      = "";
    if (allImages.length) {
        // only change if array is exists
        var allImagesLength = allImages.length;
        var newURL          = allImages[imgNum].src;
        var newTitle        = allImageTitle[imgNum];
        if (!useZoom) {
            linkURL = newURL.replace('/image_mini', '/image_view_large');
            var ref = window.document.getElementById(targetID);
            ref.parentNode.href = linkURL;
        }
        imgNum++;
        if (imgNum >= allImagesLength) {
            imgNum = 0;
        }
        changeATMPImageSource(targetID, newURL, newTitle);
    }    
}

//---------------------------

function initAutoChange() {
    /*  initialize the interval for automatic image change
        The variable 'autoChangeDelay ' have to setup in other scriptparts before.
    */
    imgNum = 0;
    window.setInterval("autoChangeSideImage()", autoChangeDelay);
}
//---------------------------
