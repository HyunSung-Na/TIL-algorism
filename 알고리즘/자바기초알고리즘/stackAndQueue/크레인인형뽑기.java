package com.baekjun.demo.인프런.stackAndQueue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

public class 크레인인형뽑기 {

    static int[][] array;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        array = new int[N][N];
        Stack<Integer> stack = new Stack<>();
        int answer = 0;

        for (int i = 0; i < N; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            for (int j = 0; j < N; j++) {
                array[i][j] = inputs[j];
            }
        }

        int M = Integer.parseInt(br.readLine());
        int[] move = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for (int k = 0; k < M; k++) {
            int x = move[k] - 1;

            for (int y = 0; y < N; y++) {
                if (array[y][x] != 0) {
                    if (stack.isEmpty()) {
                        stack.push(array[y][x]);
                    }
                    else if (stack.peek() == array[y][x]) {
                        answer += 2;
                        stack.pop();

                    } else {
                        stack.push(array[y][x]);
                    }

                    array[y][x] = 0;
                    break;
                }
            }
        }

        System.out.println(answer);
    }
}
