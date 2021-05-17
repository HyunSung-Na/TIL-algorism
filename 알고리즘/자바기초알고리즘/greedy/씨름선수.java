package com.baekjun.demo.인프런.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 씨름선수 {

    static class Actor implements Comparable<Actor>{
        int ki;
        int weight;

        public Actor(int ki, int weight) {
            this.ki = ki;
            this.weight = weight;
        }

        public int getKi() {
            return ki;
        }

        public int getWeight() {
            return weight;
        }

        @Override
        public int compareTo(Actor o) {
            return o.getKi() - this.ki;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<Actor> arrayList = new ArrayList<>();
        final int[] max = {Integer.MIN_VALUE};
        final int[] answer = {0};

        for (int i = 0; i < N; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            arrayList.add(new Actor(inputs[0], inputs[1]));
        }

        Collections.sort(arrayList);

        arrayList.forEach(
                (it) -> {
                    if (it.weight > max[0]) {
                        max[0] = it.weight;
                        answer[0]++;
                    }
                });

        System.out.println(answer[0]);
    }
}
