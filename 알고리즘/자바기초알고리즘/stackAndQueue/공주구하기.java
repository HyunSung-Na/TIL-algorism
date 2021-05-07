package com.baekjun.demo.인프런.stackAndQueue;

import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 공주구하기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int N = inputs[0];
        int M = inputs[1];

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 1; i < N + 1; i++) {
            queue.add(i);
        }

        int turn = 1;

        while (queue.size() != 1) {
            int temp = queue.poll();

            if (turn != M) {
                queue.add(temp);
            } else {
                turn = 0;
            }

            turn++;
        }

        System.out.println(queue.poll());
    }
}
