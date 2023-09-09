function solution(n) {
    // N만큼 떨어진 거리를 최소한의 건전지를 사용해서 가야한다.
   let answer = 0;
   while(n !== 0){
      if (n % 2 === 0){
          n /= 2;
      } else {
          n--;
          answer++;
      }
   }
    
   return answer;
  }
  
  solution(5);