function solution(cacheSize, cities) {
    const caches = {};
   let answer = 0;
   
   for (let i = 0; i < cities.length; i++) {
     const nc = cities[i].toLowerCase();
     
     // 히트 여부
     if (caches[nc] !== undefined) {
       answer += 1;
       caches[nc] = i;
       continue;
     } else {
       answer += 5;
     }
     
     // 현재 캐시 테이블 크기
     const size = Object.keys(caches).length;
     
     if (size < cacheSize) {
       // 캐시 테이블 적재
       caches[nc] = i;
     } else if (cacheSize > 0) {
       // LRU 알고리즘에 따른 교체 (해시 테이블 내의 가장 작은 값)
       const oldNum = Object.keys(caches).map((k) => ([caches[k], k])).sort((a, b) => a[0] - b[0])[0];
       
       delete caches[oldNum[1]];
       caches[nc] = i;
     }
   }
   
   return answer;
 }