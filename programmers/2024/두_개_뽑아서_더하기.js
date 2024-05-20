function solution(numbers) {
    const s = new Set([])  
    
    
    // 모든 경우의 수 찾기
    
    for (let i = 0; i < numbers.length; i ++) {
      for (let j = i + 1; j < numbers.length; j ++) {
        s.add(numbers[i] + numbers[j]);
      }
    }
    
    return Array.from(s).sort((a, b) => a - b)
  }
  
  solution([5, 0, 2, 7]);
  
  
  