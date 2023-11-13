#!/usr/bin/node
function factorial(a){
if (a < 0){
    return -1;	
} else if (a === 1 || isNaN(a)){
	return 1;
}
else{
	return (a * factorial(a-1));
}
}
const x = Number(process.argv[2]);
console.log(factorial(x));



