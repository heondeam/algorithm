let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n");

const T = Number(input.shift());




for (let i = 0; i < T; i++) {
    const N = Number(input.shift());
    const numbers = input.shift().split(" ").map(Number);
    const visited = Array(N+1).fill(0);
    let cnt = 0;
    const graph = [];


    const dfs = (v, graph, visit) => {
        if(visit[v] === 1) {
            return;
        }

        visit[v] = 1;

        if(graph[v].length) {
            dfs(graph[v][0], graph, visit);
        }
    }

    for (let j = 0; j < N + 1; j++) {
        graph.push([]);
    }

    for (const [i, num] of numbers.entries()) {
        if (i + 1 !== num) {
            graph[i + 1].push(num);
        }
    }

    for (const num of numbers) {
        if(!visited[num]) {
            cnt +=1;
            dfs(num, graph, visited);
        }
    }

    console.log(cnt);
}