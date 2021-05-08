package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 임시반장 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] array = new int[N + 1][6];
        int answer = 0;
        int maxValue = 0;

        for (int i = 1; i < N + 1; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            for (int j = 1; j < 6; j++) {
                array[i][j] = inputs[j - 1];
            }
        }

        for (int k = 1; k < N + 1; k++) {
            int cnt = 0;

            for (int v = 1; v < N + 1; v++) {
                for (int m = 1; m < 6; m++) {
                    if (array[k][m] == array[v][m]) {
                        cnt++;
                        break;
                    }
                }
            }

            if (cnt > maxValue) {
                maxValue = cnt;
                answer = k;
            }

        }

        System.out.println(answer);
    }
}
