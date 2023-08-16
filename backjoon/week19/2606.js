let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

const N = Number(input[0]) // 컴퓨터의 수
const C = Number(input[1]) // 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
const edges = input.slice(2, input.length);

const graph = [];

for (let i = 0; i < N + 1; i++) {
    graph.push([]);
}

for (const edge of edges) {
    const splitedEdge = edge.split(" ").map(Number);
    const node1 = splitedEdge[0];
    const node2 = splitedEdge[1];
    
    graph[node1].push(node2);
    graph[node2].push(node1);
}

const virus = [];

/**
 * 
 * @param {*} x 탐색 시작 노드 
 */
function DFS(x) {
    virus.push(x);

    if (graph[x].length === 0) {
        return;
    }

    graph[x].forEach(item => {
        if(!virus.some(v => v === item)) {
            DFS(item);
        }
    });
}

DFS(1);

console.log(virus.length - 1);