// 푸드 파이트 대회

function solution(food) {
    const answer = [0];
    
    
    for (let i = food.length -1; i >= 0; i -- ) {
      const nowFood = Math.floor(food[i] / 2);
      
      for (let j = 0; j < nowFood; j ++) {
        answer.push(i);
        answer.unshift(i);
      }
    }
  
    return answer.join("")
  }
  
  solution([1,3,4,6])