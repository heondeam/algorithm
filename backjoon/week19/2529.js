let fs = require('fs');
let input = fs.readFileSync('./input.txt').toString().trim().split("\n"); 

// 부등호의 개수
const k = Number(input.shift());
// 부등호 배열 
const A = input[0].split(" "); 
// 각 부등호의 앞 뒤에 들어갈 수 있는 숫자 (중복 안됨.)
const pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

// const getPermutations = function (arr, selectNumber) {
//     const results = [];
//     if (selectNumber === 1) return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소 return
  
//     arr.forEach((fixed, index, origin) => {
//       const rest = [...origin.slice(0, index), ...origin.slice(index + 1)]; // 해당하는 fixed를 제외한 나머지 배열
//       const permutations = getPermutations(rest, selectNumber - 1); // 나머지에 대해 순열을 구한다.
//       const attached = permutations.map((permutation) => [fixed, ...permutation]); // 돌아온 순열에 대해 떼 놓은(fixed) 값 붙이기
//       results.push(...attached); // 배열 spread syntax 로 모두다 push
//     });
  
//     return results; // 결과 담긴 results return
//   };

//   const answer = [];


// getPermutations(pos, k + 1).forEach(item => {
//     for (let i = 0; i < item.length; i++) {
//         let flag = true;
    
//         for (let j = 0; j < A.length; j ++) {
//             if(A[j] === ">") {
//                 if(!(item[j] > item[j+1])) {
//                     flag = false;
//                 }
//             }else {
//                 if(!(item[j] < item[j+1])) {
//                     flag = false;
//                 }
//             }
//         }
    
//         if(flag) {
//             answer.push(item.join(""));
//         };
//     }
// });

// console.log(answer.pop()+'\n'+answer.shift())

const answer = [];

function DFS(str,cnt){
  if(cnt==k){
    answer.push(str);
    return;
  }else{
    const last = str[cnt];
    if(A[cnt]=='>'){
      for(let i = 0; i<10; i++){
        if(!str.includes(`${i}`) && last>i){
           check(str+`${i}`,cnt+1)
        }
      }
    }else{
      for(let i = 0; i<10; i++){
        if(!str.includes(`${i}`) && last<i){
           check(str+`${i}`,cnt+1)
        }
      }
    }
  }
}


for(let i = 0; i<10; i++){
  check(`${i}`,0);
}

console.log(answer.pop()+'\n'+answer.shift())
