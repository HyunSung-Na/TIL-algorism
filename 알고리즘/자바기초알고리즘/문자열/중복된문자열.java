package com.baekjun.demo.인프런.문자열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class 중복된문자열 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        ArrayList<Character> arrayList = new ArrayList<>();

        char[] chars = s.toCharArray();

        for (char c : chars) {
            if (arrayList.contains(c)) {
                continue;
            }

            arrayList.add(c);
        }

        System.out.println(arrayList.stream()
                .map(String::valueOf)
                .collect(Collectors.joining("")));
    }
}
