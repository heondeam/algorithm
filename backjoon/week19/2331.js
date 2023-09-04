let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

const [A, P] = input.shift().split(" ").map(Number);

let nowNumber = A;
let answer = [A];

while(true) {
    let splitedNumber = nowNumber.toString().split("");
    let g = 0;

    for (const s of splitedNumber) {
        g += s ** P;
    }

    nowNumber = g;
    const isExist = answer.some(item => item === g);

    if(isExist) {
        console.log(answer.slice(0, answer.findIndex(item => item === g)).length);
        break;
    }else {
        answer.push(g);
    }
}