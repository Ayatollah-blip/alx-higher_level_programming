#!/usr/bin/node
if(isNaN(process.argv[2]) || process.argv[2] === undefined)
{
console.log('Missing size');
}   else{
const x = Number(process.argv[2]);
let i = 0;
for (i; i < x; i++){
	console.log('X'.repeat(x));

}
}

