function solution(s){
    const splited = s.split("");
    const cnt = [0 , 0];
    
    
    for (const str of splited) {
        if (str === "p" || str === "P") cnt[0]++;
        if (str === "y" || str === "Y") cnt[1]++;
    }
    
    
    
    if (cnt[0] === 0 && cnt[1] === 0) return true;
    
    return cnt[0] === cnt[1]
}