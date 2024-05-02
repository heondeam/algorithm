// 숫자 짝꿍

function solution(X, Y) {
    let answer = "";
    const number_map = {
      "0": [0, 0],
      "1": [0, 0],
      "2": [0, 0],
      "3": [0, 0],
      "4": [0, 0],
      "5": [0, 0],
      "6": [0, 0],
      "7": [0, 0],
      "8": [0, 0],
      "9": [0, 0],
    }
   
    X.split("").forEach(x => number_map[x][0]++);
    Y.split("").forEach(y => number_map[y][1]++);
    
    Object.keys(number_map).reverse().forEach(k => {
        const [x, y] = number_map[k];
      
        if (x > 0 && y > 0) {
          while (number_map[k][0] > 0 && number_map[k][1] > 0) {
            
            number_map[k][0] -= 1;
            number_map[k][1] -= 1;
            
            if (answer === "0" && k === "0") {
              answer = "0";
              continue;
            };
            
            answer += k;
          }
        }
    });
    
    return answer.length ? answer : "-1";
  }
  
  solution("100", "203045");