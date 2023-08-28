function solution (sequence, k) {
    let answer= [];
    let sum = 0; 
    const sumArr = [0];
    
    for (const s of sequence) {
      sum += s;
      sumArr.push(sum);
    }
    
    let maxLen = Infinity;
    let lt = 0;
    let rt = 0;
    
    while(lt <= rt) {
      let sum = sumArr[rt] - sumArr[lt];
      
      if (sum === k) {
        // 수열의 길이 체크
        let nowLen = rt - 1 - lt;
        
        if(maxLen > nowLen) {
          answer = [lt, rt - 1];
          maxLen = nowLen;
        }
      }
      
      if (sum < k) {
        rt ++;
      }else {
        lt ++;
      }
    }
    
    return answer;
  }
  
  solution([1, 2, 3, 4, 5], 6);