let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");



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

for (let i = 0; i < input.length - 1; i ++) {
    const splitedInput = input[i].split(" ").map(Number);   
    const k = splitedInput.shift();


    const answer = getCombibnations(splitedInput, 6);

    for (const a of answer) {
        console.log(...a);
    }
    console.log();
}