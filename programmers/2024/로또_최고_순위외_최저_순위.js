// 로또 최고 순위와 최저 순위

function solution(lottos, win_nums) {
    const score = Array(7).fill(0).map((v,i) => 7-i);
    // 맞은 번호 수 (0 맞을 때, 0 틀릴 때)
    let answer = [0, 0];
    
    
    for (const n of lottos) {
      if (win_nums.indexOf(n) > -1) {
        answer[0] ++;
        answer[1] ++;
      }
      
      if (n === 0) {
        answer[0] ++;
      }
    }
   
    return [score[answer[0]] > 5 ? 6 : score[answer[0]] , score[answer[1]] > 5 ? 6 : score[answer[1]]];
  }
  
  solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]);