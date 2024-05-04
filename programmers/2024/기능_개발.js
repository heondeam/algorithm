// 기능 개발

function solution(progresses, speeds) {
    const deployments = [];
    
    while (progresses.length) {
      for (let i = 0; i <progresses.length; i ++) {
        progresses[i] += speeds[i];
      }
      
      let num = 0;
      
      while (progresses[0] >= 100) {
        progresses.shift();
        speeds.shift();
        num ++;
      }
      
      if (num > 0) deployments.push(num);
    }
    
    return deployments;
  }
  
  solution([1, 95, 95, 95], [99, 1, 1, 1]);