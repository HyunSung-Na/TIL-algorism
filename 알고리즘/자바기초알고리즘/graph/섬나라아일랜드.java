package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 섬나라아일랜드 {

    static int N;
    static int[][] board;
    static int answer;
    static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        board = new int[N][N];

        for (int i = 0; i < N; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            for (int j = 0; j < inputs.length; j++) {
                board[i][j] = inputs[j];
            }
        }

        for (int p = 0; p < N; p++) {
            for (int m = 0; m < N; m++) {
                if (board[p][m] == 1) {
                    board[p][m] = 0;
                    dfsIsLand(p, m);
                    answer++;
                }
            }
        }

        System.out.println(answer);
    }

    private static void dfsIsLand(int x, int y) {

        for (int i = 0; i < 8; i++) {
            int nx = dx[i] + x;
            int ny = dy[i] + y;

            if (nx >= 0 && nx < N && ny >= 0 && ny < N
                    && board[nx][ny] == 1) {
                board[nx][ny] = 0;
                dfsIsLand(nx, ny);
            }
        }
    }
}
