function solution(m, v) {
    let answer = 1;
    let result = [v.shift()];

    for (const iter of v) {
        for (let i = 0; i < result.length; i++) {
            if (result[i] < m && result[i] + iter <= m) {
                result[i] += iter;
                break;
            } else {
                result.push(iter);
                answer += 1;
                break;
            }
        }
    }

    return answer;
}

const m = 4;
const v = [3,2,3,1];

console.log(solution(m, v));