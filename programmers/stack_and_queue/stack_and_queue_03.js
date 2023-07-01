let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("");


let stack = [];

for (let i = 0; i < stack.length; i ++) {
    let now = input[i];

    if(stack.length > 0) {
        if(stack[stack.length - 1] == "(") {
            stack.pop();
        }else {
            stack.push(now);
        }

    }else {
        stack.push(now);
    }
}


if(stack.length > 0) {
    console.log(false);
}else {
    console.log(true);
}