function solution(a, b, n) { 
    // a : 콜라를 받기 위해 주어야 하는 병 수, b : 빈 병 a개를 가져다 줬을 때, 받을 수 있는 콜라 수, n : 현재 가지고 있는 빈병.
    let cnt = 0;
    
    while (n / a >= 1) {
      const num = Math.floor(n / a);
      cnt += (num * b);
      n = n - (a * num);
      n = n + (num * b);
    }
    
    return cnt
  }
  
  solution(5, 3, 21);