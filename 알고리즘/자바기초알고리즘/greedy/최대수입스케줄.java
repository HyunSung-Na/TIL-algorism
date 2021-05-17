package com.baekjun.demo.인프런.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

class Lecture implements Comparable<Lecture> {

    public int money;
    public int time;

    Lecture(int money, int time) {
        this.money = money;
        this.time = time;
    }

    @Override
    public int compareTo(Lecture o) {
        return o.time - this.time;
    }
}

public class 최대수입스케줄 {

    static int n, max = Integer.MIN_VALUE;

    static int solution(ArrayList<Lecture> arrayList) {
        int answer = 0;
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        int j = 0;
        for (int i = max; i >= 1; i--) {
            for (; j < n; j++) {
                if (arrayList.get(j).time < i) break;
                priorityQueue.add(arrayList.get(j).money);
            }

            if (!priorityQueue.isEmpty()) answer += priorityQueue.poll();
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        ArrayList<Lecture> arrayList = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            arrayList.add(new Lecture(inputs[0], inputs[1]));
            max = Math.max(inputs[1], max);
        }

        Collections.sort(arrayList);

        int answer = solution(arrayList);
        System.out.println(answer);
    }
}
