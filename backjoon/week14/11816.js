let fs = require('fs');
let X = fs.readFileSync('./input.txt').toString();

/* 11816. 8진수, 10진수, 16진수 */

if(X.slice(0, 2) == "0x") {
    // 16진수
    console.log(parseInt(X, 16));
}else if(X.length >= 2 && X[0] == "0") {
    // 8진수
    console.log(parseInt(X, 8));
}else {
    console.log(X);
}