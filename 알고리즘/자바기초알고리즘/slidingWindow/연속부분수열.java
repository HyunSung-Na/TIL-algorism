package com.baekjun.demo.인프런.slidingWindow;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 연속부분수열 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] array = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int answer = sliding(input, array);

        System.out.println(answer);
    }

    private static int sliding(int[] input, int[] array) {
        int answer = 0;

        int N = input[0];
        int M = input[1];

        int lt = 0;
        int sum = 0;

        for (int rt = 0; rt < N; rt++) {
            sum += array[rt];

            if (sum == M) {
                answer++;
            }

            while (sum >= M) {
                sum -= array[lt];
                lt++;
                if (sum == M) {
                    answer++;
                }
            }
        }

        return answer;
    }

}
