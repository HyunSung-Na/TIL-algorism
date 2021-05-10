package com.baekjun.demo.인프런.sorting;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 중복확인 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String answer = "U";
        int[] array = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .sorted()
                .toArray();

        for (int i = 1; i < N; i++) {
            int pre = array[i - 1];

            if (pre == array[i]) {
                answer = "D";
                break;
            }
        }

        System.out.println(answer);
    }
}
