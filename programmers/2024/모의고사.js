// 모의고사

function solution(answers) {
    const answer = Array(3).fill(0);
    const supoza = [
      [0,1,2,3,4,5],
      [0,2,1,2,3,2,4,2,5],
      [0,3,3,1,1,2,2,4,4,5,5],
    ]
    
    for (let i = 1; i <= answers.length; i++) {
      const nowAnswer = answers[i - 1];
      const [s1,s2,s3] = supoza;
      
      // s1
      if (i >= s1.length) {
        if (s1[i % 5 === 0 ? 5 : i % 5] === nowAnswer) answer[0]++
      }else {
        if (s1[i] === nowAnswer) answer[0]++;
      }
      
      if (i >= s2.length) {
        if (s2[i % 8 === 0 ? 8 : i % 8] === nowAnswer) answer[1]++;
      }else {
        if (s2[i] === nowAnswer) answer[1]++;
      }
      
      if (i >= s3.length) {
        if (s3[i % 10 === 0 ? 10 : i % 10] === nowAnswer) answer[2]++;
      }else {
        if (s3[i] === nowAnswer) answer[2]++;
      }
    }
    
    const result = [];
    const maxAnswer = Math.max(...answer);
    
    answer.forEach((a, idx) => {
      if (a === maxAnswer) result.push(idx + 1);
    });
    
    return result.sort();
  }
  
  solution([3, 2, 2, 3]);