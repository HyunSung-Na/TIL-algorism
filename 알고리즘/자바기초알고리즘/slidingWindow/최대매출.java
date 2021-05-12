package com.baekjun.demo.인프런.slidingWindow;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 최대매출 {

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
        int sum = 0;

        int N = input[0];
        int M = input[1];
        int lt = 0;
        int rt = M - 1;

        for (int j = 0; j < M; j++) {
            sum += array[j];
        }

        int prev = sum;

        for (int i = 0; i < N; i++) {
            if (rt < N - 1) {
                int temp = prev;
                temp -= array[lt];
                lt++;
                rt++;
                temp += array[rt];
                prev = temp;
                sum = Math.max(sum, temp);
            }
        }

        return sum;
    }
}
