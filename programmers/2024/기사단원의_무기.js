// 기사단원의 무기

// number 만큼 반복문을 돌면서 해당 숫자의 약수 개수를 리턴, 약수가 limit보다 크다면 limit-1을 합계

const find = (x) => {
    if (x === 0 || x === 1 || x === 2) return x;
    
    let result = new Set()
    
    for (let i = 1; i <= Math.sqrt(x); i ++) {
      if (x % i === 0) {
        result.add(x / i);
        result.add(i)
      }
    }
    
    
    return result.size;
  }
  
  
  function solution(number, limit, power) {
    let result = 0;
    
    for (let i = 1; i <= number; i ++) {
      const nowNum = find(i);
      
      if (nowNum > limit) {
        result += power;
      }else {
        result += nowNum;
      }
    }
    
    return result;
  }
  
  solution(10,3,2);