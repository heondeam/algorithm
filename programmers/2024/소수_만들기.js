// 소수 만들기

const getCombinations = (arr, selectNumber) => {
    const results = []
    if (selectNumber === 1) return arr.map((value) => [value])
    
    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1)
      const combinations = getCombinations(rest, selectNumber - 1)
      const attached = combinations.map((combination) => [fixed, ...combination])
      results.push(...attached)
    });
  
    return results
  }
  
  function solution(nums) {
    let answer = 0;
    const cases = getCombinations(nums, 3);
    
    for (const ca of cases) {
      const sum = ca.reduce((acc, v) => acc + v)
      let flag = true;
      
      for (let i = 2; i < sum; i ++) {
        if (sum % i === 0) {
          flag = false;
          break;
        }
      }
      
      if(flag) answer++;
    }
    
    return answer;
  }
  
  solution([1,2,3,4]);