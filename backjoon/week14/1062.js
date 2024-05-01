let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const sentense = input.slice(1, input.length);

if(K < 5) {
    console.log(0);
}else if (K === 5) {
    if (sentense.filter(item => item === "antatica").length > 0) {
        console.log(1);
    }
}else {


}

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





