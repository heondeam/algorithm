function solution (picks , minerals) {
    var answer = 0;
    let len = Math.ceil(minerals.length / 5);
    let maxLen = picks.reduce((a, b) => a + b);
    let arr = [];
    if (maxLen === 0) return 0;
    minerals = minerals.splice(0, maxLen * 5);

    for (let a = 0; a < len; a++) {
      let obj = { d: 0, i: 0, s: 0 };
      // minerals의 0번째부터 5번째까지 자른후 배열을 순회하면서
      // 자른 배열의 해당 요소를 obj에 카운터
      minerals.splice(0, 5).map((v) => obj[v[0]]++);
      // 각 곡괭이로 5개의 광석을 캤을때 사용되는 피로도를 arr에 추가
      // 순서대로 [ dia, iron, stone ]
      // a ~ a + 4 구간에 각 곡괭이의 피로도를 저장 
      arr.push([
        obj.d + obj.i + obj.s,
        obj.d * 5 + obj.i + obj.s,
        obj.d * 25 + obj.i * 5 + obj.s,
      ]);
    }
    // stone 곡괭이로 캤을 때 가장 큰값이 앞에 오도록 내림차순으로 정렬 후
    // 배열을 순회 하면서 stone 곡괭이로 캤을 때 가장 큰값은 다이아가 많다는 뜻이므로
    // 다이아 곡괭이(picks[0])를 먼저 사용
    // 다이아 곡괭이가 없다면 철 곡괭이(picks[1])를 사용
    // 철 곡괭이도 없다면 돌 곡괭이 사용
    arr
      .sort((a, b) => b[2] - a[2])
      .map((v) => {
        if (picks[0] > 0) return picks[0]--, (answer += v[0]);
        if (picks[1] > 0) return picks[1]--, (answer += v[1]);
        if (picks[2] > 0) return picks[2]--, (answer += v[2]);
      });

    return answer;
}

solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]);