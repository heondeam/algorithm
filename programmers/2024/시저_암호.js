function solution(s, n) {
    const arr = [
      "a",
      "b",
      "c",
      "d",
      "e",
      "f",
      "g",
      "h",
      "i",
      "j",
      "k",
      "l",
      "m",
      "n",
      "o",
      "p",
      "q",
      "r",
      "s",
      "t",
      "u",
      "v",
      "w",
      "x",
      "y",
      "z",
    ];
    let answer = "";
    const splited = s.split("");
    
    for (let i = 0; i < splited.length; i++) {
      if (splited[i] === " ") {
        answer += " ";
        continue;
      }
      
      const isUpper = splited[i] === splited[i].toUpperCase();
  
      
      if (isUpper) {
        const idx = arr.indexOf(splited[i].toLowerCase());
        const ns = idx + n > 25 ? (idx + n) % 26 : idx + n;
        
        answer += arr[ns].toUpperCase();
      }else {
        const idx = arr.indexOf(splited[i]);
        const ns = idx + n > 25 ? (idx + n) % 26 : idx + n;
        
        answer += arr[ns];
      }
    }
    
    return answer;
  }