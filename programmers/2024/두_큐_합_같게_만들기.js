function solution(queue1, queue2) {
    let answer = 10000000;
    
    // d: 타입, t: 작업 횟수
    const dfs = (q1, q2,  t) => {
      // 기저 조건
      if (t > (queue1.length + queue2.length)) return -1;
      
      if (q1.length === 0 || q2.length === 0) {
        return;
      }
      
      const sumA = q1.reduce((acc, a) => acc + a);
      const sumB = q2.reduce((acc, b) => acc + b);
      
      if (sumA === sumB) {
        answer = Math.min(answer, t);
        return;
      }
      
      if (sumA > sumB) {
        dfs([...q1.slice(1, q1.length)], [...q2, ...q1.slice(0, 1)], t + 1);
      }else {
        dfs([...q1, ...q2.slice(0, 1)], [...q2.slice(1, q2.length)], t + 1);
      }
    }  
    
    dfs([...queue1], [...queue2], 0);
    
    return answer === 10000000 ? -1 : answer;
  }
  solution([1, 1], [1, 5]);