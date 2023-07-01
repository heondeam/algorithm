let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

/* 8595. 히든 넘버 */

let n = Number(input[0]);
let str = input[1];

let ans = [];

for (let i=0; i<n; i++) {
    let now_str = str[i];

    if(Number(str[i-1]) || Number(str[i-1]) === 0) {
        continue;
    }else {
        if(Number(str[i]) || Number(str[i]) === 0) {
            for (let j = i + 1; j<n; j++) {
                if(Number(str[j]) || Number(str[j]) === 0) {
                    now_str += str[j];
                }else{ 
                    break;
                }
            }
    
            ans.push(now_str);
        }
    }
}

let sum = 0;

ans.forEach(item => {
    sum += Number(item);
});

console.log(sum);