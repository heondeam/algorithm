function solution(t, p) {
    // 문자열 t의 부분 문자열 중 P가 나타내는 수보다 작거나 같은 것이 나오는 횟수 리턴.
    let answer = 0;
    
    // t의 길이에 따라 반복의 횟수 달라질 것.
    // p 의 길이 <= t의 길이 <= 10,000
    // O(N ^ 2) 의 알고리즘의 경우 10 ^ 8 시간 소요
    
    
    for (let i = 0; i < t.length; i ++) {
      for (let j = i; j < t.length; j ++) {
        const nowSubStr = t.slice(i, j + 1);
        
        if (nowSubStr.length === p.length) {
          if (Number(nowSubStr) <= Number(p)) {
            answer += 1;
          }
        }
      }
    }
    
    
    return answer;
  }