let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

/* 11720. 숫자의 합 */

let N = Number(input[0]);
let arr = input[1].split("").map(Number);

function sum(arr) {
    let sum = 0;

    arr.forEach(item => {
        sum += item;
    });

    return sum;
}

console.log(sum(arr));