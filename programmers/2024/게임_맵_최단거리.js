function solution(maps) {
    const [dx, dy] = [[-1, 0, 1, 0], [0, 1, 0, -1]];
    const [h, w] = [maps.length, maps[0].length];
    
    const bfs = (x, y) => {
      const queue = [[x, y]];
      const v = Array.from({length: h}, () => Array.from({length: w}, () => 0));
      v[x][y] = 1;
      
      while(queue.length > 0) {
        const [sx, sy] = queue.shift();
        
        for (let i = 0; i < 4; i ++) {
          const [nx, ny] = [sx + dx[i], sy + dy[i]];
          
          if (nx >= 0 && ny >= 0 && nx < h && ny < w) {
            if (v[nx][ny] === 0 && maps[nx][ny] === 1) {
              queue.push([nx, ny]);
              v[nx][ny] = v[sx][sy] + 1
            }
          }
        }
      }
      
      
      return v[h - 1][w- 1] === 0 ? -1 : v[h - 1][w- 1];
    }
    
    return bfs(0, 0);
  }
  
  solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]);