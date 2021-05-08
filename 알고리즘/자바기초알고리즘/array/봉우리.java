package com.baekjun.demo.인프런.array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 봉우리 {

    static int[][] array;
    static int[] x = {0, 1, -1, 0};
    static int[] y = {1, 0, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int answer = 0;
        array = new int[N + 2][N + 2];

        for (int i = 1; i < N + 1; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            for (int j = 1; j < N + 1; j++) {
                array[i][j] = input[j - 1];
            }
        }

        for (int k = 1; k < N + 1; k++) {
            for (int p = 1; p < N + 1; p++) {
                boolean check = true;

                for (int w = 0; w < 4; w++) {
                    int nx = k + x[w];
                    int ny = p + y[w];

                    if (array[k][p] <= array[nx][ny]
                            && nx < N + 1 && ny < N + 1
                            && nx > 0 && ny > 0) {
                        check = false;
                        break;
                    }
                }

                if (check) {
                    answer += 1;
                }
            }
        }

        System.out.println(answer);
    }
}
