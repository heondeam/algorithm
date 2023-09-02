function solution (board) {
    const maps = [];
    const visited = [];
    let [sx, sy] = [0, 0];
    let [end_x, end_y] = [0, 0];
    
    for (let i = 0; i < board.length; i ++) {
      maps.push([]);
      visited.push([]);
      
      const splitedStr = board[i].split("");
      
      for (let j = 0; j < splitedStr.length; j ++) {
        maps[i].push(splitedStr[j]);
        visited[i].push(10000);
        
        if(splitedStr[j] === "R") {
          sx = i;
          sy = j;
        }
        
        if(splitedStr[j] === "G") {
          end_x = i;
          end_y = j;
        }
      }
    }  
    
    const [w, h] = [board[0].length, board.length];
    const [dx, dy] = [[-1, 0, 1, 0], [0, 1, 0, -1]];
    
    const bfs = (x, y) => {
      const queue = [[x, y, 0]];
      
      while(queue.length) {
          if (visited[end_x][end_y] !== 10000) {
            return visited[end_x][end_y];
          }
        
        const [ex, ey, ec] = queue.shift();
        
        for (let i = 0; i < 4; i++) {
          // i에 따른 방향 0 : 상 , 1 : 우, 2 : 하, 3 : 좌
          let [nx, ny, nc] = [ex, ey, ec + 1];
          
          while ((ny + dy[i] < w && nx + dx[i] < h) && (ny + dy[i] >= 0 && nx + dx[i] >= 0) && maps[nx + dx[i]][ny + dy[i]] !== "D") {
            ny += dy[i];
            nx += dx[i];
          }
          
          if ((ny < w && nx < h) && (ny >= 0 && nx >= 0)) {
            if (nc < visited[nx][ny]) {
              visited[nx][ny] = nc;
              queue.push([nx,ny,nc]);
            }
          }
        }
      }
      
      return -1;
    }  
    
  
    return bfs(sx, sy);
  }
  
  solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]);