let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

let today = new Date(input[0]);
let terms = input.slice(1, 4).map(item => item.split(" "));
let privacies = input.slice(4, input.length).map(item => item.split(" ")).map((item, index) => {
    return [new Date(item[0]), item[1], index + 1];
});

let result = [];

// 월 단위로 계산.
for (let i = 0; i < privacies.length; i++) {
    let now_date = privacies[i][0];
    let now_term = terms.find(item => item[0] === privacies[i][1]);

    now_date.setMonth(now_date.getMonth() + Number(now_term[1]));

    if(now_date <= today) {
        result.push(privacies[i][2]);
    }
}

privacies.sort((a, b) => a[0] - b[0]);

console.log(result);