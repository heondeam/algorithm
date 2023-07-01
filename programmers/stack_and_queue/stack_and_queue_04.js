let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

let queue = input[0].split(" ").map((item, index) => [Number(item), index]);
let n = Number(input[1]);
let x = 0;


while (queue.length > 0) {
    let now_process = queue.shift();
    let is_exist = false;

    for (let i = 0; i < queue.length; i++) {
        if(queue[i][0] > now_process[0]) {
            is_exist = true;
            break;
        }
    }


    if(is_exist) {
        queue.push(now_process);
    }else {
        x++;
        
        if(now_process[1] == n) {
            console.log(x);
            break;
        }
    }
}


console.log(Array.prototype.sort);