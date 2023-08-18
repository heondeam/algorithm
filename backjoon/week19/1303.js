let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

// 아군 - 흰색옷(W) , 적군 - 파란색옷(B)
// 병사 N 명이 뭉쳐있을 때 N^2 의 위력 낼 수 있음. (대각선으로만 인접한 경우는 뭉쳐있는 것 아님.)

const [N, M] = input[0].split(" ").map(Number);
const info = input.slice(1, input.length);
const map = [];
const visited = [];
let [white, blue] = [0, 0];

// 탐색 방향 - 상 하 좌 우
const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];

for (let i = 0; i < M; i ++) {
    visited.push([]);

    for (let j = 0; j < N; j ++) {
        visited[i].push(0);
    }
}

for (const [i ,row] of info.entries()) {
    const item = row.split("");
    map.push([]);
    for (const s of item) {
        map[i].push(s);
    }
}

// 내 병사의 위력의 합 적국 병사의 위력의 합을 출력.
function BFS(x, y) {

    const queue = [];
    queue.push([x, y]);
    visited[x][y] = 1;
    let nt = map[x][y];
    let answer = 0;

    while (queue.length > 0) {
        const [cx, cy] = queue.shift();
        answer += 1;

        for (let i = 0; i< 4; i ++) {
            const nx = cx + dx[i];
            const ny = cy + dy[i];

            if(nx >= 0 && ny >= 0 && nx < M && ny < N) {
                if(visited[nx][ny] === 0 && map[nx][ny] === nt) {
                    visited[nx][ny] = 1;
                    queue.push([nx, ny]);
                }
            }
        }
    }

    nt === "W" ? (white += answer ** 2) : (blue += answer ** 2);
}

for (let i = 0; i < M; i ++) {
    for (let j = 0; j < N; j ++) {
        if (!visited[i][j]) BFS(i, j);
    }
}

console.log(white, blue);