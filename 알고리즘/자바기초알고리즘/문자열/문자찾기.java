package com.baekjun.demo.인프런.문자열;

import java.util.*;

public class 문자찾기 {

    static int matchChar(String target, char s) {
        int matchCount = 0;

        String toUpperCase = target.toUpperCase();
        char c = Character.toUpperCase(s);

        for (int i = 0; i < toUpperCase.length(); i++) {
            if (toUpperCase.charAt(i) == c) {
                matchCount += 1;
            }
        }

        return matchCount;
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        String target = in.next();
        char s = in.next().charAt(0);

        System.out.println(matchChar(target, s));
        return ;
    }
}