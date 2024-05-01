// 과일장수 

// 사과는 상태에 따라 1 ~ k점
// 한 상자에 사과를 m개씩 담아 포장한다. 
// 상자에 담긴 사과 중 가장 낮은 점수가 p일 때, 사과 한 상자의 가격은 P * M 이다.

// 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 리턴하자.

function solution(k, m, score) {
    let answer = 0;
    const cnt = Math.floor(score.length / m);
    const boxs = [];
    score.sort((a, b) => b - a);
    
    for (let i = 0; i < cnt; i++) {
      boxs.push(score.slice(i * m, (i * m) + m));
    }
    
    for (const box of boxs) {
      const price = box.at(-1) * m;
      answer += price;
    }
    
    return answer;
  }
  
  solution(4, 3,	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]);