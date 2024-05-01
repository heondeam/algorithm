let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

const [n, k] = input.shift().split(" ").map(Number);

const dp = Array(k + 1).fill(0);
dp[0] = 1;

for (let i = 0; i < input.length; i++) {
    for (let j = Number(input[i]); j <= k; j++) {
      dp[j] += dp[j - Number(input[i])];
    }
}
console.log(dp[k]);