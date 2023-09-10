function solution(n, words) {
    // 현재 턴 
    let turn = 1;
    // 이전에 나온 단어
    let preWords = [];
    
    for (let i = 0; i < words.length; i ++) {
      const nowWord = words[i];
      const nowPerson = (i + 1) % n === 0 ? n : (i + 1) % n;
      
      if (nowWord.length === 1) {
        // 한글자 단어 탈락
        return [nowPerson, turn];
      }
      
      if (i > 0) {
        const preword = preWords.at(-1);
  
        if (preWords.includes(nowWord)) {
          // 이전에 등장했던 단어라면 탈락
          return [nowPerson, turn];
        }
  
        if (i > 0 && preword[preword.length - 1] !== nowWord[0]) {
          // 끝말잇기가 아니면 탈락
          return [nowPerson, turn];
        }
      }
      
      // 통과 시 단어 추가
      preWords.push(nowWord);
      // 현재 사람이 마지막 사람이면 turn ++;
      if (nowPerson === n) {
        turn += 1;
      }
    }
    
      // 탈락자 없다면?
    return [0, 0];
  }
  
  solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]);