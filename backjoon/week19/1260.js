let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().split("\n");


const [nodes, edges, v] = input.shift().split(" ").map(Number);

const graph = [];

let dfsAnswer = "";
let bfsAnswer = "";

let visited = Array(nodes+1).fill(0);

for (let i = 0; i < nodes + 1; i ++) {
    graph.push([]);
}

for (let i = 0; i < input.length; i++) {
    const [a, b] = input[i].split(" ").map(Number);

    graph[a].push(b);
    graph[b].push(a);

    graph[a].sort((a, b) => a - b);
    graph[b].sort((a, b) => a - b);
}

/**
 * 
 * @param {*} v 탐색을 시작할 노드
 */
function dfs(n) {
    visited[n] = 1;

    dfsAnswer += `${n} `;
    for (const s of graph[n]) {
        if(!visited[s]) {
            dfs(s);
        }
    }
}

/**
 * 
 * @param {*} n 탐색을 시작할 노드
 */
function bfs(n) {
    const queue = [];
    queue.push(n);
    visited[n] = 1;

    while(queue.length) {
        const nv = queue.shift();
        bfsAnswer += `${nv} `;
        for (const ns of graph[nv]) {
            if (!visited[ns]) {
                visited[ns] = 1;
                queue.push(ns);
            }
        }
    }

}

dfs(v);

visited = Array(nodes+1).fill(0);

bfs(v);

console.log(dfsAnswer.trim());
console.log(bfsAnswer.trim());