let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

let bridge_length = Number(input[0]);
let weight = Number(input[1]);
let truck_weight = input[2].split(" ").map((item, index) => {
    return [Number(item), 0];
});


let bridge = [truck_weight.shift()];
bridge[0][1] += 1;

let spended_time = 1;

// while문 한 바퀴에 1시간이라고 생각
while (bridge.length > 0) {
    // 다리를 지나고 있는 트럭들 이동 +1
    for(let i = 0; i < bridge.length; i++) {
        bridge[i][1] += 1;
    }

    if(bridge[0][1] === bridge_length + 1) {
        bridge.shift();
    }

    let bridge_sum = bridge.reduce((acc, curr) => acc + curr[0], 0);


    if(bridge_sum < weight) {
        // 다리에 트럭이 진입할 수 있는 상황
        if(truck_weight.length > 0 && (truck_weight[0][0] + bridge_sum) <= weight) {
            let next_truck = truck_weight.shift();
            next_truck[1] += 1;
            
            bridge.push(next_truck);
        }
    }

    spended_time += 1;
}

console.log(spended_time);