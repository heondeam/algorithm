function solution(maps) {
    let answer = [];
    let sum = 0;
    const maxX = maps.length;
    const maxY = maps[0].length;
    const newMaps = [];
    const [dX, dY] = [[-1, 0, 1, 0], [0, 1, 0, -1]];
    
    let exitPos;
    let startPos;
    let leverPos;
    
    for (let i = 0; i < maps.length; i ++) {
      newMaps.push([]);
      
      for (let j = 0; j < maps[i].length; j ++) {
        newMaps[i].push(maps[i][j]);
        
        if (maps[i][j] === "S") {
          startPos = [i, j];
        }
        
        if (maps[i][j] === "L") {
          leverPos = [i, j];
        }
        
        if (maps[i][j] === "E") {
          exitPos = [i, j];       
        }
      }
    }
    
    function BFS(x, y, o) {
  
      const queue = [[x, y, 0]];
      const visited = [];
      
      for (let i = 0; i < maxX; i ++) {
        visited.push([]);
        for (let j = 0; j < maxY; j ++) {
          visited[i].push(0);
        }
      }
      
      visited[x][y] = 1;
      
      while(queue.length) {
        const [nX, nY, nT] = queue.shift();
        
        for (let i = 0; i < 4; i ++) {
          const [sX, sY] = [nX + dX[i], nY + dY[i]];
          
          if ((sX >= 0 && sX < maxX) && (sY >= 0 && sY < maxY)) {
            if (maps[sX][sY] !== "X" && visited[sX][sY] === 0) {            
              // 갈 수 있음.
              if (maps[sX][sY] === o) {
                answer.push(nT + 1);
                sum += nT + 1;
                return;
              }else {
                queue.push([sX, sY, nT + 1]);
                visited[sX][sY] = 1
              }
            }            
          }
        }
      }
    } 
    
    BFS(startPos[0],startPos[1], "L");
    BFS(leverPos[0],leverPos[1], "E");
    
    
    return answer.length > 1 ? sum : -1;
  }