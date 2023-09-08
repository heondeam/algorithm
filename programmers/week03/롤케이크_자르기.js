function solution(topping) {
    let answer = 0;
    let leftHash = {};
    let rightHash = {};
    let leftSort = 0;
    let rightSort = 0;
    
    for (const tp of topping) {
      if (rightHash[tp]) {
        rightHash[tp] += 1;
      }else {
        rightHash[tp] = 1;
        rightSort += 1;
      }
    }
    
    for (let i = 0; i < topping.length; i ++) {
      
      if (leftHash[topping[i]]) {
        leftHash[topping[i]] += 1;
      }else {
        leftHash[topping[i]] = 1;
        leftSort += 1;
      }
      
      if(rightHash[topping[i]] - 1) {
        rightHash[topping[i]] -= 1;
      }else {
        delete rightHash[topping[i]];
        rightSort -= 1;
      }
    
        
      if (leftSort === rightSort) {
        answer += 1;
      }
    }
    
    return answer;
  }
  
  solution([1, 2, 1, 3, 1, 4, 1, 2]);