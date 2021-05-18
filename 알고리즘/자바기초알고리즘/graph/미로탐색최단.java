package com.baekjun.demo.인프런.graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 미로탐색최단 {

    static int LENGTH = 8;
    static int[][] board;
    static int[][] dis;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        board = new int[LENGTH][LENGTH];
        dis = new int[LENGTH][LENGTH];

        for (int i = 1; i < LENGTH; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            for (int j = 1; j <= 7; j++) {
                board[i][j] = inputs[j - 1];
            }
        }
        bfs(1, 1);
        if (dis[LENGTH- 1][LENGTH - 1] == 0) System.out.println(-1);
        else {
            System.out.println(dis[LENGTH- 1][LENGTH - 1]);
        }
    }

    private static void bfs(int x, int y) {
        Queue<Point> queue = new LinkedList<>();
        queue.offer(new Point(x, y));
        board[1][1] = 1;

        while (!queue.isEmpty()) {
            Point temp = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = temp.x + dx[i];
                int ny = temp.y + dy[i];

                if (checkLength(nx, ny) && board[nx][ny] == 0) {
                    board[nx][ny] = 1;
                    queue.offer(new Point(nx, ny));
                    dis[nx][ny] = dis[temp.x][temp.y] + 1;
                }
            }
        }
    }

    private static boolean checkLength(int nx, int ny) {
        return nx >= 1 && nx <= 7 && ny >= 1 && ny <= 7;
    }
}

