let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

let N = Number(input[0]);
const loop = input[0].length;

// 256 (= 245 + 2 + 4 + 5) , 245는 256의 생성자.
const final = [];

for (let i = 1; i < N; i ++) {
    let nowNum = [...i.toString()];

    let ans = i;

    for (let j = 0 ; j < nowNum.length; j++) {
        ans += Number(nowNum[j]);
    }

    if(ans === N) {
        final.push(i);
    }
}


if(final.length > 0) {
    console.log(final[0]);
}else {
    console.log(0);
}