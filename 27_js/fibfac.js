//Team In the Works :: Shafiul H, Kosta D
//SoftDev pd2
//K27 -- Basic functions in JavaScript
//2023-04-03t

// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

// fact
function fact(n) {
    if (n < 2){
        return 1
    } else{
        return n * fact(n - 1)
    }
}

console.log(fact(1))
console.log(fact(2))
console.log(fact(3))
console.log(fact(4))
console.log(fact(5))

function fib(n) {
    if (n < 2){
        return 1
    } else{
        return fib(n - 1) + fib(n - 2)
    }
}

console.log(fib(1))
console.log(fib(2))
console.log(fib(3))
console.log(fib(4))
console.log(fib(5))
