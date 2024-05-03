// 다트 게임

function solution(dartResult) {
    const dart_arr = dartResult.split("");
    const scores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    const games = [];
    
  
    while(dart_arr.length) {
      const nowStr = dart_arr.shift();
      
      const isNumber = scores.indexOf(Number(nowStr)) > -1 ? true : false;
      
      console.log(games, "\n")
      
      if (isNumber) {
        // 숫자일 경우
        if (Number(nowStr) === 1) {
          // 10 일 경우
          if (dart_arr[0] === "0") {
            games.push([10]);
            dart_arr.shift();
            continue;
          }
        }
          games.push([Number(nowStr)]);
          continue;
      }
      
      if (nowStr === "S") {
        games[games.length - 1][0] = games[games.length - 1][0] ** 1;
      }
      
      if (nowStr === "D") {
        games[games.length - 1][0] = games[games.length - 1][0] ** 2;
      }
      
      if (nowStr === "T") {
        games[games.length - 1][0] = games[games.length - 1][0] ** 3;
      }
      
      if (nowStr === "*") {
        games[games.length - 1][0] *= 2;
        
        if (games.length > 1) {
          games[games.length - 2][0] *= 2;
        }
      }
      
      if (nowStr === "#") {
        games[games.length - 1][0] *= -1;
      }
    }
    
    return games.reduce((acc, v, idx) => Number(acc) + v[0]);
  }
  
  solution("1D2S0T");