function solution(wallpaper) {
    const board = wallpaper.map(paper => paper.split(""));
    
    const maxX = board.length;
    const maxY = board[0].length;
    const [dx, dy] = [[0, 1], [1, 0]];
    const answer = [];
    
    const visited = new Array(maxX).fill([]).map(a => new Array(maxY).fill(0));
    
    const BFS = (x, y) =>  {
      
      const queue = [[x, y]];
      visited[x][y] = 1;
        
      if (board[x][y] === "#") {
        answer.push([x, y]);
      }
      
      while(queue.length) {
        const [nx, ny] = queue.shift();
        
        for (let i = 0; i < 2; i ++) {
          const [sx, sy] = [nx + dx[i], ny + dy[i]];
          
          if (sx < maxX && sy < maxY) {
            if (visited[sx][sy] === 0) {
              queue.push([sx, sy]);
              visited[sx][sy] = 1;
              
              if (board[sx][sy] === "#") {
                answer.push([sx, sy]);
              }           
            }
          }
        }
      }
      
    }
    
    BFS(0, 0);
    
    
    const aArr = answer.map(a => a[0]);
    const bArr = answer.map(a => a[1]);
    
    
    return [Math.min(...aArr), Math.min(...bArr), Math.max(...aArr) + 1, Math.max(...bArr) + 1];
  
  }