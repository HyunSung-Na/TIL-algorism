package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 멘토링 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ints = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int N = ints[0];
        int M = ints[1];

        int[][] array = new int[M][N];

        for (int i = 0; i < M; i++) {
            int[] exam = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            for (int j = 0; j < N; j++) {
                array[i][j] = exam[j];
            }
        }

        int result = 0;

        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                int cnt = 0;
                int person1 = i;
                int person2 = j;
                for (int k = 0; k < M; k++) {
                    for (int p = 0; p < N; p++) {
                        if (array[k][p] == i) {
                            person1 = p;
                        }

                        if (array[k][p] == j) {
                            person2 = p;
                        }
                    }

                    if (person1 < person2) {
                        cnt++;
                    }
                }

                if (cnt == M) {
                    result++;
                }
            }
        }

        System.out.println(result);
    }
}
