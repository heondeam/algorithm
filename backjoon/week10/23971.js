let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

const [H, W, N, M] = input[0].split(" ").map(Number);


// 한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐 있을 때, 모든 참가자는 세로로 N칸 또는 가로로 M칸 이상 비우고 앉아야 한다.

let peoples = 0;

for (let i = 1; i < H + 1; i += N + 1) {
    for (let j = 1; j < W + 1; j += M + 1) {
        peoples += 1;
    };
}

console.log(peoples);