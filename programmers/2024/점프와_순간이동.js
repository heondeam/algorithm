function solution(n) {
    let ans = 1;
    
    while (n !== 1) {
      if (Number.isInteger(n / 2)) {
        n /= 2;
      }else {
        n -= 1;
        ans++;
      }
    }
    
    return ans;
  }
  
  solution(6);