// 성격 유형 검사하기


function solution(survey, choices) {
    let answer = "";
    const results = {
      1: {R : 0, T: 0},
      2: {C: 0, F: 0},
      3: {J: 0, M: 0},
      4: {A: 0, N: 0}
    }
    const getScores = (a, b, score) => {
      const scoreMap = {
        1: [a, 3],
        2: [a, 2],
        3: [a, 1],
        4: [null, null],
        5: [b, 1],
        6: [b, 2],
        7: [b, 3],
      };
      
      const typeMap = {
        "R": 1,
        "T": 1,
        "C": 2,
        "F": 2,
        "J": 3,
        "M": 3,
        "A": 4,
        "N": 4,
      }
      
      return [...scoreMap[score], typeMap[scoreMap[score][0]]];
    };
    
    for (const [idx, c] of choices.entries()) {
      const [a, b] = survey[idx].split("");
      const score = getScores(a, b, c);
      
      if (score[0]) {
        results[score[2]][score[0]] += score[1];
      }    
    }
    
    for (const i in results) {
      const s = results[i];
      const v = Object.keys(results[i]).map((k) => ([k, s[k]]));
      
      if (v[0][1] > v[1][1]) {
        answer+=v[0][0];
      }else if (v[0][1] < v[1][1]) {
        answer+=v[1][0];
      }else {
        answer+=v[0][0];
      }
    }
    
    return answer;
  }
  
  solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])