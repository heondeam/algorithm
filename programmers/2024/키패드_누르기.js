// 키패드 누르기

function solution(numbers, hand) {
    const map = [
      [1,2,3],
      [4,5,6],
      [7,8,9],
      ["*",0,"#"]
    ];
    let [lt, rt] = [[3, 0], [3, 2]];
    const answer = [];
    
    const getPosition = (v) => {
        for (let i =0; i < map.length; i ++) {
          for (let j = 0; j <map[i].length; j++) {
            if (map[i][j] === v) return [i, j];
          }
        }
    }
    
    const getDistance = (a, b) => {
     return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
    
    while (numbers.length) {
      const num = numbers.shift();
      
      if ([1, 4, 7].includes(num)) {
        answer.push("L");
        lt = getPosition(num);
  
      }else if ([3, 6, 9].includes(num)) {
        answer.push("R");
        rt = getPosition(num);
      }else {
        // 거리 계산 눌러야 할 키패드 좌표 - 현재 손가락 좌표
        const rd = getDistance(rt, getPosition(num));
        const ld = getDistance(lt, getPosition(num));
        
        // 거리 비교
        if (rd > ld) {
          answer.push("L");
          lt = getPosition(num);
        }
        else if (rd < ld) {
          answer.push("R");
          rt = getPosition(num);
        }
        else {
          const n = hand === "right" ? "R" : "L";
          
          answer.push(n);
          if (n === "R") rt = getPosition(num);
          else lt = getPosition(num)
        }
      }
    }
    
    return answer.join("");
  }
  
  solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right");