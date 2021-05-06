package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class 문장속단어 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] strings = br.readLine().split(" ");
        ArrayList<String> answer = new ArrayList();

        int maxInt = Arrays.stream(strings)
                .mapToInt(it -> it.length())
                .max()
                .getAsInt();

        for (String s : strings) {
            if (s.length() == maxInt) {
                answer.add(s);
            }
        }

        System.out.println(answer.get(0));
    }
}
