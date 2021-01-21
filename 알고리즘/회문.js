const convert = s => {
    let answer = "YES";
    let len = s.length;
    s = s.toLowerCase();

    for(let i = 0; i < Math.floor(len/2); i++) {
        if (s[i] !== s[len-i-1]) {
            return "NO";
        }
    }

    return answer;
}

s = "gooG";
console.log(convert(s));