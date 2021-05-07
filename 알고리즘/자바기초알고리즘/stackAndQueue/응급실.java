package com.baekjun.demo.인프런.stackAndQueue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class PerSon{
    int id;
    int priority;

    public PerSon(int id, int priority) {
        this.id = id;
        this.priority = priority;
    }
}

public class 응급실 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] array = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        Queue<PerSon> queue = new LinkedList<>();
        int N = inputs[0];
        int M = inputs[1];
        int answer = 1;

        for (int i = 0; i < array.length; i++) {
            queue.offer(new PerSon(i, array[i]));
        }

        while (!queue.isEmpty()) {
            PerSon temp = queue.poll();

            for (PerSon x : queue) {
                if (x.priority > temp.priority) {
                    queue.add(temp);
                    temp = null;
                    break;
                }
            }

            if (temp != null) {
                if (temp.id == M) {
                    System.out.println(answer);
                    System.exit(0);
                } else {
                    answer++;
                }
            }
        }
    }
}
