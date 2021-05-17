package com.baekjun.demo.인프런.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class 결혼식 {

    static class Time implements Comparable<Time> {
        public int time;
        public char state;

        public Time(int time, char state) {
            this.time = time;
            this.state = state;
        }

        @Override
        public int compareTo(Time o) {
            if (this.time == o.time) {
                return this.state - o.state;
            }

            return this.time - o.time;
        }

        public char getState() {
            return state;
        }

        public int getTime() {
            return time;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<Time> arrayList = new ArrayList<>();
        int[] answer = {0};
        int[] cnt = {0};

        for (int i = 0; i < N; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            arrayList.add(new Time(inputs[0], 's'));
            arrayList.add(new Time(inputs[1], 'e'));
        }

        Collections.sort(arrayList);

        arrayList.forEach((it) -> {
            if (it.state == 's') {
                cnt[0] += 1;
            } else if (it.state == 'e') {
                cnt[0] -= 1;
            }

            answer[0] = Math.max(answer[0], cnt[0]);
        });

        System.out.println(answer[0]);
    }
}
