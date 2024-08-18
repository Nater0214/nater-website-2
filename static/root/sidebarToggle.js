// Written by Nater0214

var sidebarState = false;

document.getElementById("sidebarButton").addEventListener("click", () => {
    let button = document.getElementById("sidebarButton")
    let sidebar = document.getElementById("sidebar");
    if (!sidebarState) {
        sidebar.style.transform = "translateX(250px)";
        button.style.transform = "rotate(180deg)";
    } else {
        sidebar.style.transform = "translateX(0px)";
        button.style.transform = "rotate(0deg)";
    }
    sidebarState = !sidebarState;
});