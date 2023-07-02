let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

const [len_a, len_b] = input[0].split(" ").map(Number);
const a = new Set(input[1].split(" ").map(Number));
const b = new Set(input[2].split(" ").map(Number));

Set.prototype.difference = function (set) {
    const result = new Set(this);

    for (const value of set) {
        result.delete(value);
    }

    return result;
}

const answer = [...a.difference(b), ...b.difference(a)];