package com.baekjun.demo.인프런.dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 동전교환 {

    static int n, m;
    static int[] dy;

    static int solution(int[] coin) {
        Arrays.fill(dy, Integer.MAX_VALUE);
        dy[0] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = coin[i]; j <= m; j++) {
                dy[j] = Math.min(dy[j], dy[j - coin[i]] + 1);
            }
        }

        return dy[m];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();

        m = Integer.parseInt(br.readLine());
        dy = new int[m + 1];

        System.out.println(solution(arr));
    }
}
