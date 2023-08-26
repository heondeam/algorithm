

// 명함의 크기 가로, 세로
const sizes = [[20, 10], [12, 18]];
// 만들 수 있는 명함의 크기 가로, 세로

const longer = [];
const shoter = [];


for (let i = 0; i < sizes.length; i ++) {
    const [nowX, nowY] = sizes[i];

    if(nowX > nowY) {
        longer.push(nowX);
        shoter.push(nowY);
    }else {
        longer.push(nowY);
        shoter.push(nowX);
    }
}


console.log(longer, shoter)
console.log(Math.max(...longer) * Math.max(...shoter));