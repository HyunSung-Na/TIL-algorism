package com.baekjun.demo.인프런.slidingWindow;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 연속된자연수의합 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int m = N / 2 + 1;

        int[] arr = new int[m];

        int answer = 0;
        int sum = 0;
        int lt = 0;

        for (int i = 0; i < m; i++) {
            arr[i] = i + 1;
        }

        for (int rt = 0; rt < m; rt++) {
            sum += arr[rt];
            if (sum == N) answer++;
            while (sum >= N) {
                sum -= arr[lt++];
                if (sum == N) answer++;
            }
        }

        System.out.println(answer);
    }
}
