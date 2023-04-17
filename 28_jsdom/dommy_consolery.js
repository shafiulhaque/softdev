/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN
   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team In the Works :: Shafiul H, Kosta D
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17m
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); // "AYO" is printed into the console

var i = "hello";
var j = 20;
// string and number is stored in the respective variable


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x; // 30 is added to x
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        }; //the variable is like a dictionary


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem); // item is added to the end of a list
}; // var is functioning like a dictionary


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
}; // item is removed from a list


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
      items[i].classList.add('red'); //adds red
    } else {
      items[i].classList.add('blue'); //adds blue
    }
  }
};

//insert your implementations here for...
// FIB
function fib(n) {
  if (n < 2){
      return 1
  } else{
      return fib(n - 1) + fib(n - 2)
  }
}

// FAC
function fact(n) {
  if (n < 2){
      return 1
  } else{
      return n * fact(n - 1)
  }
}

// GCD
function gcd(a, b) {
  if (b == 0) {
    return a;
  } else {
    while (b != 0) {
      var x = b;
      b = a%b;
      a = x;
    }
    return a;
  }
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};