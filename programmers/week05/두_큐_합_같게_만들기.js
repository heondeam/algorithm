function solution(queue1, queue2) {
    const bfs = (q1, q2, l = 0) => {
      const queue = [[q1, q2, l]];
      const visited = new Set(); // 이미 방문한 큐 상태를 저장할 집합
  
      while (queue.length) {
        const [nq1, nq2, nl] = queue.shift();
        const sumQ1 = nq1.reduce((ac, cu) => ac + cu, 0);
        const sumQ2 = nq2.reduce((ac, cu) => ac + cu, 0);
  
        if (sumQ1 === sumQ2) {
          return nl;
        } else {
          if (nq1.length > 0 && nq2.length > 0) {
            const newState1 = [nq1.slice(1), [...nq2, nq1[0]]];
            const newState2 = [[...nq1, nq2[0]], nq2.slice(1)];
  
            // 새로운 상태를 방문하지 않았을 경우에만 큐에 추가
            if (!visited.has(JSON.stringify(newState1))) {
              queue.push([newState1[0], newState1[1], nl + 1]);
              visited.add(JSON.stringify(newState1));
            }
            if (!visited.has(JSON.stringify(newState2))) {
              queue.push([newState2[0], newState2[1], nl + 1]);
              visited.add(JSON.stringify(newState2));
            }
          }
        }
      }
      return -1; // 무한 루프를 방지하기 위한 추가 종료 조건
    }
  
    return bfs(queue1, queue2);
  }
  
  solution([1, 2, 1, 2], [1, 10, 1, 2]);