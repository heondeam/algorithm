function solution(k ,tangerine) {
    let answer = 0;
    let i = 0;
    const fruits = {};
    
    // 한 상자에 담으려는 귤의 개수 k개를 고를 때 크기의 종류를 최소화 하자.
    for (const f of tangerine) {  
      if (fruits[f]) {
        fruits[f] += 1;
      }else {
        fruits[f] = 1;
      }
    }
    
    // 귤의 개수가 많은 순대로 크기를 내림차순 정렬
    const newTangerine = [...Object.keys(fruits).sort((a, b) => fruits[b] -fruits[a] )];
    
    // 상자에 모든 귤을 담을 때까지 반복
    while(k) {
      const nowSize = newTangerine[i];
      
      if (fruits[nowSize] - k >= 0) {
        answer += 1;
        k = 0;
        break;
      } else {
        answer += 1;
        k -= fruits[nowSize];
        i += 1;
      }
    }
    
    return answer;
  }
  
  
  solution(4, [1, 3, 2, 5, 4, 5, 2, 3]);