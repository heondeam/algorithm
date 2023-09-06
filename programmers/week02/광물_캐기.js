function solution (picks , minerals) {
  let answer = 0;
  // 누적된 피로도
  let maxLen = Math.min((picks[0] * 5) + (picks[1] * 5) + (picks[2] * 5), minerals.length);
  let nowLen = 0;
  
  // 곡괭이 수에 맞춰 캘 수 있는 광물.
  let splitedMinerals = [];
  
  // O(N) - minerals.length <= 50
  while (maxLen > nowLen) {
    let cnt = maxLen - nowLen;
    
    if (cnt > 0 && cnt <= 5) {
      const nm = minerals.splice(0, cnt);
      splitedMinerals.push(nm);
      nowLen += nm.length;
    }else if(cnt > 5) {
      const nm = minerals.splice(0, 5);
      splitedMinerals.push(nm);
      nowLen += 5;
    }else {
      break;
    }
  }
  
  splitedMinerals.sort((a, b) => {
    let sumA = 0;
    let sumB = 0;
    
    a.forEach(item => item === "diamond" ? sumA += 25 : item === "iron" ? sumA += 5 : sumA += 1);
    b.forEach(item => item === "diamond" ? sumB += 25 : item === "iron" ? sumB += 5 : sumB += 1);

    // sumA와 sumB를 비교하여 내림차순으로 정렬
    if (sumA > sumB) {
      return -1; // sumA가 크면 b를 앞으로
    } else if (sumA < sumB) {
      return 1;  // sumB가 크면 a를 앞으로
    } else {
      return 0;  // sumA와 sumB가 같으면 순서 변경 없음
    }
  });
  
  while (splitedMinerals.length) {
    const nowMinerals = splitedMinerals.shift();
    
    let nowPick;
    
    if (picks[0] > 0) {
      nowPick = "diamond";
      picks[0] -= 1;
    }else if (picks[1] > 0) {
      nowPick = "iron";
      picks[1] -= 1;
    }else if (picks[2] > 0) {
      nowPick = "stone";
      picks[2] -= 1;
    }
    
    if (nowPick === "diamond") {
      nowMinerals.forEach(item => answer += 1);
    }
    
    if (nowPick === "iron") {
      nowMinerals.forEach(item => item === "diamond" ? answer += 5 : item === "iron" ? answer += 1 : answer += 1);
    }
    
    if (nowPick === "stone") {
      nowMinerals.forEach(item => item === "diamond" ? answer += 25 : item === "iron" ? answer += 5 : answer += 1);
    }
  }
  
  return answer;
}

solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]);