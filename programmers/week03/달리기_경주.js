function solution(players, callings) {
	// 원본 배열을 복사한다.
  const answer = [...players];
  const nowHash = Object.fromEntries(players.map((item, idx) => [item, idx]));
  

  for (let i = 0; i < callings.length; i ++) {
    const nowIndex = nowHash[callings[i]];
     
		// 앞에 있는 선수
    let temp = answer[nowIndex - 1];
    
		// 추월
    answer[nowIndex - 1] = answer[nowIndex];
    answer[nowIndex] = temp;
    

		// 해시테이블 업데이트
    nowHash[callings[i]] = nowIndex - 1;
    nowHash[answer[nowIndex]] = nowIndex;
    
  }
  
  // 복사한 배열을 리턴한다.
  return answer;
}