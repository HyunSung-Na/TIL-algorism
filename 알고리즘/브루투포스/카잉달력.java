package com.baekjun.demo.브루트포스;

import java.io.*;

public class 카잉달력 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int testNum = Integer.parseInt(br.readLine());

        for (int i = 0; i < testNum; i++) {
            String[] input = br.readLine().split("\\s");
            int M = Integer.parseInt(input[0]);
            int N = Integer.parseInt(input[1]);
            int x = Integer.parseInt(input[2]) - 1;
            int y = Integer.parseInt(input[3]) - 1;

            int result = 0;
            boolean check = false;

            for (int j = x; j < (M * N); j += M) {
                if (j % N == y) {
                    result = j + 1;
                    check = true;
                    break;
                }
            }

            if (!check)
                result = -1;

            bw.write(String.valueOf(result));
            bw.flush();
        }

    }

}

