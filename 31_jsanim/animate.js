var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#ff0000";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    clear();
    ctx.beginPath();
    ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    if (radius == c.width/2){
        growing = false;
    } else if (radius == 0){
        growing = true;
    }
    if (growing){
        radius += 2;
    } else {
        radius -= 2;
    }
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);

};

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log( requestID );
    requestID = window.cancelAnimationFrame(requestID);

}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click",  stopIt);