let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split(" ").map(Number);

function solution(arr) {
    stack = [];

    
    for(let i =0; i < arr.length; i++) {

        if(stack) {
            if (stack[stack.length - 1] == arr[i]) {
                continue;
            }else {
                stack.push(arr[i]);
            }
        }else {
            stack.push(arr[i]);
        }

    }
}