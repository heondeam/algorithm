function solution(storey) {
    let answer = 0;
    const storeyArr = storey.toString().split("").map(Number);
    
    for (let i = storeyArr.length - 1; i >= 1; i --) {
      
      if (storeyArr[i] === 5) {
        answer += 5;     
        
        if (storeyArr[i - 1] >= 5) {
          storeyArr[i - 1] += 1;
        }
        
      }else if (storeyArr[i] === 10) {
        storeyArr[i - 1] += 1;
        storeyArr[i] = 0;
      }else if (storeyArr[i] > 5) {
        answer += (10 - storeyArr[i]);
        storeyArr[i - 1] += 1;
      }else {
        // storeyArr[i] < 5
        answer += storeyArr[i];
      }
      
      
  
    }
    
    return answer + Math.min(storeyArr[0], 11 - storeyArr[0]);
  }