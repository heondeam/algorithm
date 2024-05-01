// 타겟 넘버

function solution(numbers, target) {
    let cnt = 0;
    
    const dfs = (i, x, sum = 0) => {
      if (i === numbers.length) {
        console.log(sum);
        
        if (sum === target) cnt++;
        return;
      }
      
      if (x === "+") sum += numbers[i];
      if (x === "-") sum -= numbers[i];
      
      dfs(i + 1, "+", sum);
      dfs(i + 1, "-", sum);
    }
    
    dfs(0, "+");
    // dfs(0, "-");
    
    return cnt;
  }
  
  
  solution([4,1,2,1], 2);