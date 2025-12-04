let zIndexCounter = 100;

function toggleStart() {
    const menu = document.getElementById("start-menu");
    menu.style.display = (menu.style.display === "block") ? "none" : "block";
}

function openApp(url) {
    toggleStart();

    let win = document.createElement("div");
    win.className = "window";
    win.style.top = "120px";
    win.style.left = "160px";
    win.style.zIndex = ++zIndexCounter;

    win.innerHTML = `
        <div class="window-header" onmousedown="dragWindow(event, this.parentElement)">
            Windows 13 App — 128-bit Mode
            <span style="float:right;cursor:pointer;" onclick="this.parentElement.parentElement.remove()">✖</span>
        </div>
        <div class="window-content">
            <iframe src="${url}" width="100%" height="100%" frameborder="0"></iframe>
        </div>
    `;

    document.body.appendChild(win);
}

let dragData = null;

function dragWindow(e, win) {
    dragData = {
        offsetX: e.clientX - win.offsetLeft,
        offsetY: e.clientY - win.offsetTop,
        win: win
    };

    document.onmousemove = dragMove;
    document.onmouseup = () => document.onmousemove = null;
}

function dragMove(e) {
    if (!dragData) return;
    dragData.win.style.left = (e.clientX - dragData.offsetX) + "px";
    dragData.win.style.top = (e.clientY - dragData.offsetY) + "px";
}
