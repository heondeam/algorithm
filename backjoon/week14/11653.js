let fs = require('fs');
let N = Number(fs.readFileSync('./input.txt').toString());

/* 11653. 소인수분해 */

let ans = [];

function isPrime(x) {
    if (x == 1) {
        return false;
    }

    if (x == 2) {
        return false;
    }

    for (let i = 2; i < x; i++) {
        if(x % i == 0) {
            return false;
        }
    }

    return true;
}

while(!isPrime(N) && N > 2) {
    for (let i = 2; i < N; i ++) {
        if(N % i === 0) {
            N = N / i;

            ans.push(i);
            break;
        }
    }
}

if (N > 1) {
    ans.push(N);
}

ans.sort((a, b) => a - b);

let true_ans = "";

ans.forEach((item, i) => {
    if(i == ans.length -1) {
        true_ans += `${item}`;
    }else {
        true_ans += `${item}\n`;
    }
});

console.log(true_ans);