let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

let [n, x] = input[0].split(" ").map(Number);
visiters = input[1].split(" ").map(Number);

// x일 동안 가장 많이 들어온 방문자 수를 출력한다. 최대 방문자 수가 0이라면 sad를 출력.
let max = 0;
let total = 0;
let cnt = 1;


for (let i = 0; i < x; i++) total += visiters[i];
max = Math.max(total, max);
for (let i = 1; i <= n - x; i ++) {
    total -= visiters[i - 1];
    total += visiters[i + x - 1];
    if (total === max) cnt += 1;
    else {
      if (total > max) cnt = 1;
      max = Math.max(total, max);
    }
}

if (max === 0) {
    console.log("SAD");
}else {
    console.log(max, cnt);
}