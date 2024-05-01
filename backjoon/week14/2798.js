let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const cards = input[1].split(" ").map(Number);


function getCombibnations(arr, target) {
    const result = [];
    if(target === 1) return arr.map(el => [el]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombibnations(rest, target - 1);
        const attached = combinations.map(el => [fixed, ...el]);
        result.push(...attached);
    });

    return result;
}

let ans = getCombibnations(cards, 3);
let cur = 0;

ans.forEach(item => {
    let sum = 0;

    item.forEach(item2 => {
        sum += item2;
    });

    if (sum <= M) {
        cur = Math.max(cur, sum);
    }
});

console.log(cur);