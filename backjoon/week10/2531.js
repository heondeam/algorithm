let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

/* 2531. 회전 초밥 */

// N = 회전 초밥 벨트에 놓인 접시 수
// d = 초밥의 가짓수
// k = 연속해서 먹는 접시의 수
// c = 쿠폰 번호

const [N, d, k, c] = input[0].split(" ").map(Number);
const belts = [];


for (let i = 1; i < N + 1; i++) {
    if (i === N) {
        belts.push({i : Number(input[i]), next: Number(input[1])});
    }else {
        belts.push({i : Number(input[i]), next: Number(input[i + 1])});
    }
}

let index = 0;
let cnt = 4;

while(1) {
    if (index === N) {
        index = 0;
    }else {
        // process.stdout.write(`${belts[index].i} `);
        console.log(belts[index].i);
        index += 1;
    }
}