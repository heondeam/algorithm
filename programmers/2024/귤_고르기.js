function solution(k, tangerine) {
    const t = Array.from({length: Math.max(...tangerine) + 1}, () => 0);
    let answer = 0;
    
    for (let i = 0; i < tangerine.length; i++) {
      t[tangerine[i]] ++;
    };
    
    t.sort((a, b) => b - a);
    
    console.log(t);
    
    for (let i = 0; i < t.length; i++) {
      answer ++;
      k -= t[i];
      
      if (k <= 0) {
        break;
      }
    }
    
    return answer;
  }
  
  solution(4, [1,3,2,5,4,5,2,3]);