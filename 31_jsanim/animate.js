var c = document.getElementById("playground");
var dotButton = document.getElementById("dotButton");
var stopButton = document.getElementById("stopButton");

var ctx = c.getContext("2d");

ctx.fillStyle = "black";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    clear(e);
    ctx.beginPath();
    ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 * Math.PI);
    ctx.fill();
    ctx.stroke();
    if (radius >= 300){
        growing = false;
    } else if (radius == 1){
        growing = true;
    }
    if (growing){
        radius += 2;
    } else {
        radius -= 2;
    }
    requestID = window.requestAnimationFrame(drawDot);

};

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log( requestID );
    requestID = window.canceltAnimationFrame(requestID);

}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click",  stopIt);