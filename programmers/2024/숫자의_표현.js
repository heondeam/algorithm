function solution(n) {
    let result = 1;
  
    for (let i = 1; i <= n; i ++) {
      let total = 0;
      
      for (let j = i; j <= n; j ++) {
        
        if (total > n) {
          tatal = 0;
          break;
        }else if (total === n) {
          result ++;
          total = 0;
          break;
        }else {
          total += j;
        }
      }
    }
    
    return result;
  }
  
  solution(10);