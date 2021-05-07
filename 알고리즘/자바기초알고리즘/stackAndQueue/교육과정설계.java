package com.baekjun.demo.인프런.stackAndQueue;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class 교육과정설계 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] rules = br.readLine().toCharArray();
        char[] inputs = br.readLine().toCharArray();
        Queue<Character> queue = new LinkedList<>();
        String answer = "YES";

        for (int i = 0; i < rules.length; i++) {
            queue.offer(rules[i]);
        }

        for (int j = 0; j < inputs.length; j++) {
            if (queue.contains(inputs[j])) {
                if (queue.poll() != inputs[j]) {
                    System.out.println("NO");
                    System.exit(0);
                }
            }
        }

        if (!queue.isEmpty()) {
            System.out.println("NO");
            System.exit(0);
        }
        System.out.println(answer);
    }
}
