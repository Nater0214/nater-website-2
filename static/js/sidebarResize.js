function getHeight() {
    let body = document.body;
    let html = document.documentElement;
    let sidebarElement = document.getElementById("sidebar");
    sidebarElement.style.height = "0px";
    let height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
    return height;
}

export function resizeSidebar() {
    let sidebarElement = document.getElementById("sidebar");
    sidebarElement.style.height = getHeight() - 75 + 'px';
}