

function solution(maps) {
  const trueMap = [];
  const visited = [];
  const answer = [];
  let [w, h] = [0, 0];
  
  for(let i = 0; i < maps.length; i ++) {
    trueMap.push([]);
    visited.push([])
    const splitedStr = maps[i].split("");
    
    for (let j = 0; j < splitedStr.length; j ++){
      trueMap[i].push(splitedStr[j]);
      visited[i].push(0);
    }
  }
  
  h = trueMap.length;
  w = trueMap[0].length;
  
  // 탐색 방향
  const dx = [-1, 0, 1, 0]
  const dy = [0, 1, 0, -1];
  // 방문여부 판별 배열
  
  // bfs를 이용해서 풀어보자.
  const bfs = (x, y) => {
    // x , y 탐색을 시작할 좌표
    const queue = [[x, y]];
    let sum = Number(trueMap[x][y]);
    visited[x][y] = 1;
    
    while (queue.length) {
      const [nx, ny] = queue.shift();
      
      for(let i = 0; i < 4; i ++) {
        const [sx, sy] = [nx + dx[i], ny + dy[i]];
        
        if ((sx >= 0 && sx < h) && (sy >= 0 && sy < w)) {
          if (visited[sx][sy] === 0 && trueMap[sx][sy] !== "X") {
            queue.push([sx, sy]);
            visited[sx][sy] = 1;
            sum += Number(trueMap[sx][sy]);
          }
        }
      }
    }    

    return sum;
  }
  
  for(let i = 0; i < trueMap.length; i ++) {
    for (let j = 0; j <  trueMap[i].length; j ++){
      if (trueMap[i][j] !== "X" && visited[i][j] === 0) {
         let sum = bfs(i, j);
          answer.push(sum);
      }
    }
  }
  
  answer.sort((a,b) => a - b);
  return answer.length > 0 ? answer : [-1];
}


solution(["XXX","XXX","XXX"]);