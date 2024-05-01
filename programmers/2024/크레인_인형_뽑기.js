// 크레인 인형 뽑기

function solution(board, moves) {
    let result = 0;
    const cart = [];
    
    for (let i = 0; i < moves.length; i ++) {
      // 크레인 위치 = 열
      const m = moves[i] - 1;
      
      // 인형 꺼내기    
      for (let j = 0; j < board.length; j ++) {
        if (board[j][m] > 0) {
          cart.push(board[j][m]);
          board[j][m] = 0;
          break;
        }
      }
      
      // 인형 터뜨리기
      while (true) {
        if (!cart.length) break;
        
        if (cart.at(-1) === cart.at(-2)) {
          cart.pop();
          cart.pop();
          result += 2;
        }else {
          break;
        }
      }
      
    }
    
    return result;
  }
  
  solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]);