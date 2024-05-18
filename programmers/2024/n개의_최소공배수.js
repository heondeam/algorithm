function solution(arr) {
    arr.sort((a, b) => a - b);
    
    const minValue = arr.at(-1)
    const maxValue = arr.reduce((acc, a) => acc * a);
  
    
    let answer = 0;
  
    for (let i = minValue; i <= maxValue; i ++) {
      let flag = true;
      
      for (let j = 0; j < arr.length; j ++) {
        if (i % arr[j] !== 0) {
          flag = false;
          break;
        }
      }
      
      
      if (flag) {
        answer = i;
        break;
      }
      
    }
    
    return answer;
  }
  
  solution([1, 2, 3]);