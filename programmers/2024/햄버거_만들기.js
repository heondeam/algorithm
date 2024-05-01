// 햄버거 만들기
// 1 - 삥, 2 - 야채, 3 - 고기

function solution(ingredient) {
    let count = 0;
    const stack = [];
    
    const getFunc = (arr) => {
      let answer = [1, 2, 3, 1];
      let isTrue = true;
      
      arr.forEach((a, i) => {
        if (a !== answer[i]) {
          isTrue = false;
        };
      });
      
      return isTrue;
    }
    
    for (let i = 0; i < ingredient.length; i ++) {
      stack.push(ingredient[i]);
      
      while (true) {
        if (stack.length < 4) break;
        
        if (getFunc(stack.slice(stack.length - 4, stack.length))) {
          stack.splice(stack.length - 4, stack.length);
          count++;
          continue;
        }
        
        break;
      }
    }
    
    
    return count;
  }
  
  solution([2, 1, 1, 2, 3, 1, 2, 3, 1]);