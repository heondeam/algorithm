function solution(N, stages) {
    // 스테이지에 도달한 사람
    const arr = Array(N + 2).fill(0);
    
    // 실패율 
    const answer = Array(N).fill(0);
    
    for (let i = 0; i < stages.length; i++) {
      for (let j = 1; j <= stages[i]; j++) {
        arr[j]++
      }
    }
  
    for (let i = 1; i < arr.length - 1; i++) {
      const starter = stages.filter(a => a === i).length;
      
      
      answer[i - 1] = [starter / arr[i], i];
    }
    
  return answer.sort((a,b) => b[0] - a[0]).map(v => (v[1]))
  }
  
  solution(5, [2,1,2,6,2,4,3,3]);