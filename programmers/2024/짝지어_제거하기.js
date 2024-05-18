function solution(s)
{
const str = s.split("");
const stack = [];
const len = str.length;

for (let i = 0; i < len; i++) {
  const ns = str[i];

  if (stack.length > 0 && stack[stack.length - 1] === ns) {
    // Remove the top element if it's the same as the current character
    stack.pop();
  } else {
    // Otherwise, push the current character onto the stack
    stack.push(ns);
  }
}

// If the stack is empty, return 1, otherwise return 0
return stack.length === 0 ? 1 : 0;
}

solution("cdcd");