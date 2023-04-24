var c = document.getElementById('slate');

var ctx = c.getContext("2d");

var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circle";
    } 
    else {
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    ctx.rect(mouseX, mouseY, 100, 300);
    ctx.fill();
    console.log("mouseclick registered at (" + mouseX + ", " + mouseY + ")");
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
    ctx.fill();
    console.log("mouseclick registered at (" + mouseX + ", " + mouseY + ")");
}

var draw = function(e) {
    if (mode == "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

var wipeCanvas = function() {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var bClear = document.getElementById("buttonClear");
bClear.addEventListener("click", wipeCanvas);