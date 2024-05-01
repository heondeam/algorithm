



const graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [4, 5],
    [7],
    [2, 6, 8],
    [1, 7]
];

const visited = Array(9).fill(0);

/**
 * 
 * @param {*} v 탐색을 시작할 노드 
 */
const dfs = (v) => {

    visited[v] = 1;
    

    console.log(v);

    for (const s of graph[v]) {
        if(!visited[s]) {
            dfs(s);
        }
    }
}

dfs(1);