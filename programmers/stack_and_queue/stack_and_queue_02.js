let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

progresses = input[0].split(" ").map(Number);
speed = input[1].split(" ").map(Number);

queue = [...progresses];

answer = [];

while(queue.length > 0) {
    if (queue[0] >= 100) {
        queue.shift();
        speed.shift();

        let tmp = 0;

        for (let i = 0; i < queue.length; i++) {
            if(queue[i] >= 100) {
                tmp += 1;
            }else {
                break;
            }
        }

        for (let i = 0; i < tmp; i++) {
            queue.shift();
            speed.shift();
        }

        answer.push(tmp + 1);
    }

    for(let i = 0; i < queue.length; i ++) {
        queue[i] += speed[i];
    }
}

console.log(answer);
