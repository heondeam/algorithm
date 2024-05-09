// 비밀지도

function makeBinary (x, n) {
    if (x.length >= n) return x;
    
    const newArr = [...x]
    
    while (newArr.length < n) {
      newArr.unshift('0')
    }
    
    return newArr;
  }
  
  function solution(n, arr1, arr2) {
    const answer = [];
    const map = Array.from({length: n}, () => Array.from({length: n}, () => ""));
    
    for(let i = 0; i < n; i ++) {
      const one = makeBinary(arr1[i].toString(2).split(""), n);
      const two = makeBinary(arr2[i].toString(2).split(""), n);
      
      one.forEach((o, idx) => {
        if (!map[i][idx] && o === "1") {
          map[i][idx] = "#";        
        }
      })
      
      two.forEach((t, idx) => {
        if (!map[i][idx] && t === "1") map[i][idx] = "#"
      })
      
      answer.push(map[i].map(a => a === "#" ? "#" : " " ).join(""))
    }
    
    return answer;
  }
  
  solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])