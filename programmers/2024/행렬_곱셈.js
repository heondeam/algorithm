function solution(arr1, arr2) {
    const [m, n] = [arr1.length, arr2[0].length];
    const answer = Array.from({length: m}, () => Array.from({length: n}).fill(0));
    
    for (let i = 0; i < m; i++) {
      for (let j = 0; j < n; j++) {
        let sum = 0;
        
        for (let k = 0; k < arr1[0].length; k ++) {
          sum += arr1[i][k] * arr2[k][j];
        }
        
        answer[i][j] = sum;
      }
    }
    
    return answer;
  }