function solution(s){
    let answer = true;
    let cnt = 0;
    
    for (const r of s.split("")){
      if (cnt < 0) return false;
      
      if (r === "(") cnt ++;
      if (r === ")") cnt --;
    }
    
    return cnt === 0 ? answer : false;
  }
  
  solution("(()(");