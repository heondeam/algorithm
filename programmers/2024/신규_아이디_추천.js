// 신규 아이디 추천


function solution(new_id: string) {
    const regex = /^(?!.*\.{2})[a-z0-9._-]{3,15}$/;
    
    if (regex.test(new_id) && new_id.indexOf(".") !== 0) return new_id;
    
    const str = new_id.split("").map(v => v.toLocaleLowerCase());
    const str2 = []
    
    for (const s of str) {
      if (!/[^a-z0-9._-]/.test(s)) {
        str2.push(s);
      }
    }
    
    let str3 = [];
    
    for (const s of str2) {
      if (str3.length === 0) {
        str3.push(s);
        continue;
      }
      
      if (s === "." && str3.at(-1) === s) {
        continue;
      }
      
      str3.push(s);
    }
    
    if (str3[0] === ".") {
      str3.shift();
    }
    
    if (str3.at(-1) === ".") {
      str3.pop();
    }
    
    if (str3.length === 0) {
      str3.push("a");
    }
    
    if (str3.length >= 16) {
      str3 = str3.splice(0, 15);
      
      if (str3[0] === ".") {
        str3.shift();
      }
      
      if (str3.at(-1) === ".") {
        str3.pop();
      }
    }else if (str3.length <= 2) {
      const last = str3.at(-1);
      
      while (str3.length < 3) {
        str3.push(last);
      }
    }
    
    return str3.join("");
  }
  
  solution(".1.");