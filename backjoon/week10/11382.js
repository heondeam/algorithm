let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split(" ");

const main = () => {
    let sum = 0;

    input.forEach(item => {
        sum += Number(item);
    }) ;

    console.log(sum);
}

main();