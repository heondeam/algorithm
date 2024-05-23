function solution(n, words) {
    let cnt = 0;
    
    for (let i = 1; i < words.length; i++) {
      const exWord = words[i - 1].split("");
      const nowWord = words[i].split("");
        
      if (exWord[exWord.length - 1] !== nowWord[0]) {
        cnt = i + 1;
        break;
      }
      
      if (words.slice(0, i).find(a => a === words[i])) {
        cnt = i + 1;
        break;
      }
      
    }
    
    if (cnt === 0) {
      return [0, 0]
    }else {
        return [cnt % n === 0 ? n : cnt % n, Math.ceil(cnt /n)]
    }
  }
  
  solution(3, ["tank", "kick", "know", "kick"]);