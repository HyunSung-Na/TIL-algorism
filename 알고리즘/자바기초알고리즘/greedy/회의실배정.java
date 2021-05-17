package com.baekjun.demo.인프런.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class 회의실배정 {

    static class CountTime implements Comparable<CountTime>{
        int start;
        int end;

        public CountTime(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public int getStart() {
            return start;
        }

        public int getEnd() {
            return end;
        }


        @Override
        public int compareTo(CountTime o) {
            if (this.end == o.end) {
                return this.start - o.start;
            }

            return this.end - o.end;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<CountTime> arrayList = new ArrayList<>();
        final int[] nextTime = {0};
        int[] answer = {0};

        for (int i = 0; i < N; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            arrayList.add(new CountTime(inputs[0], inputs[1]));
        }

        Collections.sort(arrayList);

        arrayList.forEach((it) -> {
            if (nextTime[0] <= it.start) {
                nextTime[0] = it.end;
                answer[0] += 1;
            }
        });

        System.out.println(answer[0]);
    }
}
