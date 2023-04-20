// Team Dragonite :: Jeffrey Z, Shafiul H
// SoftDev pd2
// K29 -- DOMfoolery++
// 2023-04-20t

//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
function fib(n){

  if (n <= 1){
	  return n
  }
  return fib(n-1)+fib(n-2);
}
// FAC
function fact(n) {
	if (n < 2) 
        return 1;
      else {
          return (n * fact(n - 1));
      }
}
// GCD
function gcd(a, b) {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}
// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

document.getElementById("fib").innerHTML = fib(5);
document.getElementById("fact").innerHTML = fact(5);
document.getElementById("gcd").innerHTML = gcd(5,7);

function helper1(){
  console.log(fib(20))
  document.getElementById("one").innerHTML = fib(20)
}

function helper2(){
  console.log(fib(20))
  document.getElementById("two").innerHTML = fact(20)
}

function helper3(){
  console.log(fib(20))
  document.getElementById("three").innerHTML = gcd(20,7)
}

function fibb(){
  var dasbut = document.getElementById("a"); 
  console.log('ok')
  dasbut.addEventListener('click', helper1());
}

function facc(){
  var dasbut = document.getElementById("b"); 
  console.log('ok')
  dasbut.addEventListener('click', helper2());
}

function gcdd(){
  var dasbut = document.getElementById("c"); 
  console.log('ok')
  dasbut.addEventListener('click', helper3());
}
// {
//   console.log(fib(20))
//   document.getElementById("a").innerHTML = fib(20);
//   console.log('ok')
// }