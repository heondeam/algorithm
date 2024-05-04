// 소수 찾기

// 종이조각 중복 순열 구하기



const sieveOfEratosthenes = (n) => {
    // 2부터 n까지의 모든 수에 대한 후보 리스트 생성
    let primes = new Array(n + 1).fill(true);
    primes[0] = primes[1] = false; // 0과 1은 소수가 아님
  
    // 에라토스테네스의 체 알고리즘 수행
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (primes[i]) {
            for (let j = i * i; j <= n; j += i) {
                primes[j] = false;
            }
        }
    }
  
    return primes;
  }
  
  function solution(numbers) {
      const primes = sieveOfEratosthenes(100000);
      const splited_numbers = numbers.split("");
      const answer = new Set();
  
      const dfs = (idx, currentNum, visited) => {
          if (visited[idx]) return; // 이미 방문한 숫자인 경우 건너뜁니다.
  
          visited[idx] = true; // 현재 숫자를 방문했다고 표시합니다.
          currentNum += splited_numbers[idx]; // 현재 숫자를 조합에 추가합니다.
  
          if (primes[+currentNum]) {
              answer.add(+currentNum); // 소수인 경우 정답에 추가합니다.
          }
  
          for (let i = 0; i < splited_numbers.length; i++) {
              dfs(i, currentNum, [...visited]); // 재귀 호출 시 방문 여부를 복사하여 전달합니다.
          }
      }
  
      for (let i = 0; i < splited_numbers.length; i++) {
          dfs(i, "", new Array(splited_numbers.length).fill(false)); // 방문 여부 배열을 false로 초기화합니다.
      }
  
      return answer.size;
  }
  
  solution("011");