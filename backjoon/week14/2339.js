let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

const N = Number(input[0]);
const map = [];

for (let i = 1; i < input.length; i++) {
    map.push(input[i].split(" ").map(Number));
}


for (let i = 0; i < map.length; i++) {

    for (let j=0; j < map[i].length; j++) {
        print(map[i][j]);
    }

    console.log("");
}