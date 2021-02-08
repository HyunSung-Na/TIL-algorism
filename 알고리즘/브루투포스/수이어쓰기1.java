package com.baekjun.demo.브루트포스;

import java.io.*;

public class 수이어쓰기1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int result = 0;
        int start = 1;
        int length = 1;

        while (start <= N) {
            int end = start * 10 - 1;
            if (end > N)
                end = N;
            result += (end - start + 1) * length;
            start *= 10;
            length += 1;
        }

        bw.write(String.valueOf(result));
        bw.flush();
    }
}
