function solution(board) {
    // 상, 하, 좌, 우, 대각선
    const [dx, dy] = [[-1,0,1,0,-1,-1,1,1], [0,1,0,-1,-1,1,-1,1]]
    
    const [w, h] = [board[0].length, board.length]
    
    const bombs = (() => {
      const [bombX, bombY] = [[], []]
      
      for(let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
          if (board[i][j] === 1) {
            bombX.push(i);
            bombY.push(j);
          }
        }
      }
      
      return [bombX, bombY];
    })()
    
    for (let i = 0; i < bombs[0].length; i++) {
      const [bombX, bombY] = [bombs[0][i], bombs[1][i]];
      
      for (let j = 0; j < 8; j ++) {
        const [nx, ny] = [bombX + dx[j], bombY + dy[j]];
        
        if (nx >= 0 && nx < h && ny >= 0 && ny < w) {
          board[nx][ny] = 1;
        }
      }
    }
    
    let cnt = 0;
    
    for(let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        if (board[i][j] === 0) {
          cnt++
        }
      }
    }
    
    return cnt;
  }
  
  solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]])