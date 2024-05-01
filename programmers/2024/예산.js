// 예산

// 최대한 많은 부서의 물품을 구매해주었을 때, 부서의 수

function solution(d, budget) {
    d.sort((a, b) => a-b);
    let answer = 0;
    
    for (const r of d) {
      if (budget - r >= 0) {
        budget-=r;
        answer++;
        
        continue;
      }
      
      break;
    }
    
    return answer;
  }
  
  solution([2,2,1,3,15], 15);