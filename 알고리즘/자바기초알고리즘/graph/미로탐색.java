package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 미로탐색 {

    static int LENGTH = 8;
    static int[][] board;
    static int answer = 0;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        board = new int[LENGTH][LENGTH];

        for (int i = 1; i < LENGTH; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            for (int j = 1; j <= 7; j++) {
                board[i][j] = inputs[j - 1];
            }
        }
        board[1][1] = 1;
        dfs(1, 1);
        System.out.println(answer);
    }

    private static void dfs(int x, int y) {
        if (x == LENGTH - 1 && y == LENGTH - 1) {
            answer++;
        } else {

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + x;
                int ny = dy[i] + y;

                if (checkLength(nx, ny) && board[nx][ny] == 0) {
                    board[nx][ny] = 1;
                    dfs(nx, ny);
                    board[nx][ny] = 0;
                }
            }
        }
    }

    private static boolean checkLength(int nx, int ny) {
        return nx >= 1 && nx <= 7 && ny >= 1 && ny <= 7;
    }
}
