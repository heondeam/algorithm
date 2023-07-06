let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

const str = [...input[0]];
const bomb = [...input[1]];
const stack = [];

for(let i = 0;  i < str.length; i ++) {

    // 일단 스택에 문자열 push
    stack.push(str[i]);

    // 만약 현재 Push한 문자가 폭발하는 문자열의 마지막 문자일 경우
    if(str[i] === bomb[bomb.length - 1]) {
        const start = (stack.length - 1) - (bomb.length - 1);
        const end = stack.length;

        if (stack.slice(start, end).join("") === input[1]) {
            for (let j = end - 1; j >= start; j--) {
                stack.pop();
            }
        }
    }
}

const answer = stack.join("");

if (answer) {
    console.log(answer);
}else {
    console.log("FRULA");
}