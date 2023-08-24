// Written by Nater0214

// Variables
var httpsState = true;

// Functions
export function setup() {
    let element;
    element = document.getElementById("httpsCheck");
    element.addEventListener("change", toggleHttps);

    element = document.getElementById("createButton");
    element.addEventListener("click", create);
}

function getUrl() {
    let element = document.getElementById("urlInput");

    return element.value;
}

function toggleHttps() {
    let element = document.getElementById("httpsText");
    
    if (httpsState) {
        element.style.color = "#5F5F5F";
    } else {
        element.style.color = "#FFFFFF";
    }
    httpsState =!httpsState;
}

function create() {
    let outUrl;
    if (httpsState) {
        outUrl = "//" + getUrl();
    } else {
        outUrl = getUrl();
    }
    window.open(outUrl, "_blank", "location:yes, height:500, width: 700");
}