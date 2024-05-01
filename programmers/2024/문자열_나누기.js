// 문자열 나누기

// 첫 글자를 읽는다. = x
// x를 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 센다.

// 처음으로 두 횟수가 같아지는 순간 멈추고 읽은 문자열 분리

function solution(s) {
    const str = s.split("");
    let x = str[0];
    let [sc, dc] = [[], []];
    let cnt = 0;
    let answer = 0;
    
    while (str.length) {
      const nx = str[cnt];
      
      if (nx === x) {
        sc.push(nx);
      }else {
        dc.push(nx);
      }
      
      if (sc.length === dc.length) {
        str.splice(0, cnt + 1);
        cnt = 0;
        sc = [];
        dc = [];
        x = str[0];
        answer++
        
        continue;
      }
      
      cnt++;
    }
    
    return answer;
  }
  
  
  solution("aaabbaccccabba");