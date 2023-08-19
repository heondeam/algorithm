let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

const T = Number(input.shift());
const pairs = input.map(item => item.split(" "));
const visited = {};
const demicals = {};
const [dx, dy] = [[1,-1,0,0], [0,0,-1,0]];

const isDemical = (num) => {
    if(num === 1) return false;
    if(num === 2) return true;

    for (let i = 2; i < num; i ++) {
        if(num % i === 0) {
            return false;
        }
    }

    return true;
}

const BFS = (start, end) => {
    const queue = [[start, 0]];

    visited[start] = true;

    while (queue) {
        let nowElem = queue.shift();
        let nowStr = nowElem[0];

        if(nowStr === end) return nowElem[1];

        for (let i = 0; i < 4; i ++) {
            for (let j = 0; j < 10; j ++) {
                let temp = nowStr.slice(0, i) + j + nowStr.slice(i+1, nowStr.length);
                
                if(!visited[temp] && demicals[temp] && temp >= 1000) {
                    visited[temp] = true;
                    queue.push([temp, nowElem[1] + 1]);
                }
            }
        }
    }
}

pairs.forEach(item => {
    const [start, end] = item;

    for (let i = 1000; i <= 10000; i ++) {
        visited[i] = false;
        
        if(isDemical(i)) {
            demicals[i] = true;
        }
    }   

    let result = BFS(start, end);

    return result >= 0 ? console.log(result) : console.log("Impossible");
});

