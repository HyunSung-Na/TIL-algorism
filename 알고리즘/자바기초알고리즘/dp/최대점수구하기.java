package com.baekjun.demo.인프런.dp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 최대점수구하기 {

    static int n, m;
    static int[] dy;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] input = Arrays.stream(br.readLine().split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();

        n = input[0];
        m = input[1];
        dy = new int[m + 1];

        for (int i = 0; i < n; i++) {
            int[] array = Arrays.stream(br.readLine().split(" "))
                                .mapToInt(Integer::parseInt)
                                .toArray();

            int ps = array[0];
            int pt = array[1];

            for (int j = m; j >= pt; j--) {
                dy[j] = Math.max(dy[j], dy[j - pt] + ps);
            }
        }

        System.out.println(dy[m]);
    }
}
