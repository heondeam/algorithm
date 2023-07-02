let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

const A = input[1].split(" ").map(Number);
const B = input[2].split(" ").map(Number);
const C = A.concat(B).sort((a, b) => a - b);

let answer = "";

C.forEach((item, i) => {
    if(i === C.length) {
        answer += item;
    }else {
        answer += item + " ";
    }
});

console.log(answer);