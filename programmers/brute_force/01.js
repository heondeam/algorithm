let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");


const sizes = input.map(item => item.split(" ").map(Number));

let maxWidth = 0;
let maxHeight = 0;

for (let i = 0; i < sizes.length; i++) {
    const [w, h] = sizes[i];

    maxWidth = Math.max(w, maxWidth);
    maxHeight = Math.max(h, maxHeight);
}

let sum = maxWidth * maxHeight;


for (let i = 0; i < sizes.length; i++) {
    let newSizes = [...sizes];

    for (let j = i; j < sizes.length; j ++) {
        let tmp = [];
        tmp[0] = newSizes[j][1];
        tmp[1] = newSizes[j][0];

        newSizes[j] = tmp;
    }

    let tmpMaxWidth = 0;
    let tmpMaxHeight = 0;

    for (let j = 0; j < sizes.length; j ++) {
        const [w, h] = newSizes[j];

        tmpMaxWidth = Math.max(w, tmpMaxWidth);
        tmpMaxHeight = Math.max(h, tmpMaxHeight);
    }

    console.log(tmpMaxWidth, tmpMaxHeight);
    
    sum = Math.min(sum, (tmpMaxWidth * tmpMaxHeight));
}
