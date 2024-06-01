function solution(want, number, discount) {
    const want_map = {}
      const sum = number.reduce((acc, a) => acc +a);
      let answer = 0;
      
      for (const [idx, w] of want.entries()) {
        want_map[w] = number[idx];
      }
      
      for (let i = 0; i < discount.length; i ++) {
        const day = discount.slice(i, i + 10);
        
        if (day.length >= sum) {
          let flag = true;
          
          for (let j = 0; j < want.length; j ++) {
            const nw = want[j];
            
            if (day.filter(a => a === nw).length !== want_map[nw]) {
              flag = false;
            }
          }
          
          if (flag) {
            answer ++;
          }
        }
      }
      
      return answer;
    }