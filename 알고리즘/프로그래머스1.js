function solution(n, record) {
    let answer = [];
    let result = [];
    let servers = [[]];

    while (record.length > 0) {
        let temp = record.shift().split(' ');
        result.push(temp);
    }

    for (let i = 1; i < n + 1; i++) {
        servers.push([]);
    }

    while (result.length > 0) {
        let temp = result.shift();
        let server = temp[0];
        let name = temp[1];


        while (servers[server].length >= 5) {
            servers[server].shift();
        }
        
        if (!servers[server].includes(name)) {
                servers[server].push(name);
        }
        
    }

    for (const iter of servers) {
        if (iter.length > 0) {
            answer.push(...iter.slice(0, 5));
        }
    }

    return answer;
}

const n = 1;
let record = ["1 fracta", "1 sina","1 hana","1 robel","1 abc", "1 sina", "1 lynn"];
console.log(solution(n, record));

const n1 = 4;
let record1 = ["1 a","1 b","1 abc","3 b","3 a","1 abcd","1 abc","1 aaa","1 a","1 z","1 q", "3 k", "3 q", "3 z", "3 m", "3 b"];
console.log(solution(n1, record1))