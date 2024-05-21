function solution(record) {
    const chat = {};
    
    const ans = [];
    
    for (let i = 0; i < record.length; i ++) {
      const [behavior, id, name] = record[i].split(" ");
      
      if (behavior !== "Leave") {
        chat[id] = name;
      }
    }
    
    console.log(chat)
    
    for (let i = 0; i < record.length; i ++) {
      const [behavior, id, name] = record[i].split(" ");
  
      if (behavior === "Enter") {
        ans.push(`${chat[id]}님이 들어왔습니다.`);
      }
      
      if (behavior === "Leave") {
        ans.push(`${chat[id]}님이 나갔습니다.`);
      }
    }
    
    return ans;
  }
  
  solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]);