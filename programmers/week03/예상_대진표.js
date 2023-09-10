function solution(n) {
	// 첫번째 라운드는 무조건 진행된다.
	let answer = 1;

	// 선수 목록
  const fighters = Array(n).fill(0).map((item,idx) => idx + 1);
	// 현재 라운드의 대진표
  let newFight = [];
  
	// 처음 대진표 생성
  for (let i = 0; i < n / 2; i ++) {
      const nowFighter = fighters.slice(i * 2, (i + 1) * 2);
      newFight.push(nowFighter);
  }
  
	// 다음으로 계산할 대진의 수
  n = n / 2;
  
  while(n > 1) {
    let nextFight = [];
    let newNextFight = [];
    
    for (const nf of newFight) {
      // 둘이 만났으면? answer 리턴
      if (nf.includes(a) && nf.includes(b)) {
        return answer;
      } else if (nf.includes(a) && !nf.includes(b)) {
        nextFight.push(a);
      } else if (nf.includes(b) && !nf.includes(a)) {
        nextFight.push(b);
      } else {
        nextFight.push(nf[0]);
      }
    }
    
    for (let i = 0; i < n / 2; i ++) {
        const nowFighter = nextFight.slice(i * 2, (i + 1) * 2);
        newNextFight.push(nowFighter);
    }
    
    newFight = newNextFight;
     
    n = n / 2;
    answer += 1;
  }
  
  return answer;
}

solution(8, 4, 7);