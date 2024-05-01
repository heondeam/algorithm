let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

const N = Number(input.shift());

// 종말의 수? 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수.
// 666 -> 1666 -> 2666 -> 3666 ...
// N번째 영화 제목 출력.


const answer = [];

for (let i = 1; i < Math.ceil(N / 19) * 10000; i ++) {
    if(i.toString().includes("666")){
        answer.push(i);
    }
}

console.log(answer[N-1]);

