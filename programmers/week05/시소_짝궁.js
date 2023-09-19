function solution(weights) {
    let answer = 0;
    // 시소 중심축으로부터의 거리에 따른 무게 배열
    let weightDistance = Array(4001).fill(0);
    // 실제 무게 배열
    let realWeights = Array(1001).fill(0);
    
    for (const w of weights) {
      // 거리에 따른 무게
      const d2 = w * 2;
      const d3 = w * 3;
      const d4 = w * 4;
      
      // 이전에 지나갔던 사람 중 현재 무게와 일치하는 값이 있으면 시소짝궁으로 추가한다.
      answer += weightDistance[d2];
      answer += weightDistance[d3];
      answer += weightDistance[d4];
      
      // 실제 무게가 같은 사람들이 있으면 시소의 거리에 따른 무게가 3배가 됨.
      // 이를 제거하기 위해 실제 무게 배열의 2배만큼 빼줌
      if (realWeights[w] > 0) {
        answer -= realWeights[w] * 2;
      }
      
      realWeights[w] ++;
      weightDistance[d2] ++;
      weightDistance[d3] ++;
      weightDistance[d4] ++;
    }
    
    
    return answer;
  }