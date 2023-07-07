let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");

// 강의의 수 n, 블루레이의 수 m
const [n , m] = input[0].split(" ").map(Number);

// 비디오의 수 (각 강의의 길이는 10000분을 넘지 않음)
const videos = input[1].split(" ").map(Number);

function sum(arr) {
    let result = 0;
    
    arr.forEach(item => result += item);

    return result;
}

function getMax(arr) {
    let result = arr[0];

    arr.forEach(item => {
        result = Math.max(result, item);
    });

    return result;
}

let lt = getMax(videos);
let rt = sum(videos);

let answer = rt;

while (lt <= rt) {
    // 블루레이의 크기
    mid = Math.round((lt + rt) / 2);

    // 하나의 블루레이 크기를 mid로 잡았을 때 필요한 블루레이의 수 
    let size = 0;
    let num = 1;

    for (let i = 0; i < videos.length; i++) {
        if ((size + videos[i]) <= mid) {
            size += videos[i];
        } else {
            num += 1;
            size = videos[i];
        }
    }

    if (num <= m) {
        answer = mid;
        rt = mid - 1;
    }else {
        lt = mid + 1;
    }
}

console.log(answer);