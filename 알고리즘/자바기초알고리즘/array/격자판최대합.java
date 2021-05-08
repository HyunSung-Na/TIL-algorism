package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 격자판최대합 {

    static int[][] array;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        array = new int[N][N];

        for (int i = 0; i < N; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            for (int j = 0; j < N; j++) {
                array[i][j] = inputs[j];
            }
        }

        int maxNum = 0;

        for (int i = 0; i < N; i++) {
            int sumNum = 0;

            for (int j = 0; j < N; j++) {
                sumNum += array[i][j];
            }

            maxNum = Math.max(maxNum, sumNum);
            sumNum = 0;

            for (int k = 0; k < N; k++) {
                sumNum += array[k][i];
            }

            maxNum = Math.max(maxNum, sumNum);
        }

        int crossSum = 0;

        for (int m = 0; m < N; m++) {
            crossSum += array[m][m];
        }

        maxNum = Math.max(maxNum, crossSum);

        crossSum = 0;

        for (int k = N - 1; k < 0; k--) {
            int p = 0;
            crossSum += array[p][k];
            p++;
        }

        maxNum = Math.max(maxNum, crossSum);

        System.out.println(maxNum);
    }
}
