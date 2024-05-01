let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");


const n = Number(input.shift());


const triangle = [];

for (const [i, n] of input.entries()) {
    const nowNum = n.split(" ").map(Number);
    triangle.push([...nowNum]);
}

for (let i = n-2; i >= 0; i --) {
    for (let j = 0; j < triangle[i].length; j ++) {
        triangle[i][j] += Math.max(triangle[i+1][j], triangle[i+1][j+1]);
    }
}


console.log(triangle[0][0]);

