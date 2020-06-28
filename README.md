# TIL

하루하루 배운 코드를 기록하는 곳입니다.





### 알고리즘 

python으로 준비하였습니다

# JAVA

## Collection Framework

### - Collection Framework란?

\- 배열의 단점을 보완한 데이터 군을 저장하는 클래스들을 표준화한 설계이다.
\- 다수의 데이터를 쉽게 처리할 수 있는 방법을 제공하는 클래스들로 구성된다.
\- 컬렉션(collection) : 다수의 데이터, 데이터 그룹을 의미한다.
\- 프레임워크(framework) : 표준화, 정형화된 체게적인 프로그래밍 방식이다.
\- 컬렉션 클래스(collection class) : 다수의 데이터를 저장할 수 있는 클래스이다.



![Collection Framework 계층도](https://3.bp.blogspot.com/-YatAN_wi-Kw/VsZujw_7XuI/AAAAAAAAAIk/5tZPcgA8T7w/s1600/%25EC%25BB%25AC%25EB%25A0%2589%25EC%2585%25981.jpg)

**인터페이스의 특징**

- **List**
  1. 순서가 있는 데이터의 집합, 데이터의 중복을 허용한다.
  2. 데이터를 add를 하면 앞에서 부터 순차적으로 데이터가 들어간다.(Stack)
  3. 각각의 저장되어 있는 공간들은 고유한 index를 갖는다
  4. 구현클래스 : ArrayList, LinkedList, Stack, Vector 등
- **Set**
  1. 순서를 유지하지 않는 데이터의 집합(순서가 없음), 데이터의 중복을 허용하지 않는다.
  2. 집합과 같은 구조(데이터를 추가할 때 순서와 상관없이 add한다. )
  3. 구현클래스 : HashSet, TreeSet
- **Map**
  1. key , value 값의 쌍으로 이뤄진 데이터의 집합
  2. 순서는 유지되지 않는다.
  3. key는 중복이 허용되지 않으나 value는 중복허용
  4. 구현클래스 : HashMap, TreeMap, Hashtable, Properties등

------

### ArrayList

- **Array**
  1. PHP  : Array가 Size를 가지지 않고 데이터가 추가될 때 마다 자동으로 Size가 늘어남
  2. Java  : Array에 Size를 정해줘야함 - > Java Library - > ArrayList (데이터 추가하면 배열이 자동으로 추가 )

- **ArrayList**

- 특징

  - 배열기반의 데이터구조
   - 저장 순서가 유지되고 중복을 허용

    1. 장점 : 배열은 구조가 간단하고 데이터를 읽는 시간이 짧다
    2. 단점 : 크기를 변경할 수 없다.
       - 크기를 변경해야되는 경우 새로운 배열을 생성 후 데이터를 복사해야 함
       - 크기 변경을 피하기 위해 충분히 큰 배열을 생성하면 메모리의 낭비
    3. 비 순차적인 데이터의 추가, 삭제 시간이 많이 걸린다.
       - 데이터를 추가하거나 삭제하기 위해 다른 데이터를 옮겨야 함.
            - 순차적인 데이터추가는 빠르다 (데이터의 끝에서 추가, 끝부터 삭제)

- Doubling

  - 생성한 ArrayList가 가득 차고 새로운 데이터를 넣어야 할때 Doubling 이 일어난다.
  - Doubling 이란 기존 ArrayList를 복사해서 ArrayList 두배의 크기로 생성하고 복사한 ArrayList를 붙여넣어 생성하는 것이다. 
  - 수정) 자바 컬렉션프레임워크 도입되기 전 Vector 클래스에서는 2배의 크기로 증가시켰으나 현재 ArrayList는 사이즈 증가시 50%증가
    - ArrayList grow(minCapacity : int)  - > int newCapacity = oldCapacity + (oldCapacity >> 1) 오른쪽 시프트연산
    - 오른쪽 시프트연산은 그 값을 /2 로 나눈 것과 같으므로 
    - 새로운용량 = 이전용량 + 이전용량 / 2  (전 용량보다 1.5배 증가)

  <img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbQ5ZNv%2FbtqFdt2FFoU%2FnNOQqEHT5cjQaySItSpekk%2Fimg.jpg" width = "400px" style = "height:300px" />

  

  **ArrayList 구현**

  ```java
  class ArrayList {
  	private Object[] data; // ArrayList는 객체만 사용할 수 있기 때문에 Object객체 생성
  	private int size;
  	private int index;
  	
  	public ArrayList(){
  		this.size = 1;
  		this.data = new Object[this.size]; // size 1로 배열 객체생성
  		this.index = 0; // index 0번째 부터 데이터 삽입
  	}
      
      public void add(Object obj){ //배열의 요소를 추가해주는 함수
          if(this.index == this.size-1){  // 배열이 꽉찬 경우 doubling을 실행
              doubling();
          }
          data[this.index] = obj; //현재 index에 object를 삽입
          this.index++; // 새로운 배열 추가를 위해 빈 배열 index로 이동
      }
      
      private void doubling(){ //배열의 크기를 늘려주는 함수
          this.size = this.size * 2;
          Object[] newData = new Object[this.size]; // 기존 배열의 2배 크기의 new배열 생성
          for(int i = 0; i < data.length; i++){
              newData[i] = data[i]; // 기존 배열의 값을 new배열로 복사
          }
          this.data = newData; //기존 배열의 참조변수를 현재 newData로 변경
      }
      
      public Object get(int i) throws Exception{ // index 번호로 ArrayList값에 접근하는함수
          if (i > this.index-1){ // index 값이 배열의 크기보다 크면 Exception을 발생시킨다
              throw new Exception("ArrayIndexOutOfBound");
          }else if(i < 0){ // index의 값이 0보다 작으면 Exception 발생
              throw new Exception("Negative Value");
          }
          return this.data[i];
      }
      
      public void remove(int i) throws Exception{
          if (i > this.index-1){
              throw new Exception("ArrayIndexOutOfBound");
          }else if(i < 0){
              throw new Exception("Negative Value");
          }
          for (int x = i; x < this.data.length -1; x++){
              data[x] = data[x + 1]; //삭제할 데이터를 기준으로 앞으로 덮어쓴다.
          }
          this.index--; // index를 하나 줄여준다
      }
  }
  
  public class Test{
  	public static void main(String[] args) throws Exception{
  		ArrayList al = new ArrayList();
          al.add("0");
          al.add("1");
          al.add("2");
          al.add("3");
          al.add("4");
          al.add("5");
          al.add("6");
          al.add("7");
          al.add("8");
          al.add("9");
          System.out.println(al.get(5));
          al.remove(5);
          System.out.println(al.get(5));
  	}
  }
  ```

  **(1) 객체 생성**

  ArrayList<Integer> numbers = new Arraylist<>();

  

  **(2) 데이터 추가시 add 메소드 사용**

  numbers.add(10)

  numbers.add(1,50) : index 1번에 50이라는 숫자 넣기

  

  **(3)데이터 삭제시 remove 메소드 사용**

  numbers.remove(2) : index 2번째 값 삭제, 빈공간은 메움

  but 데이터의 끝부터 삭제시 덮어쓰지 않고 데이터만 삭제

  

  **(4) 데이터 가져올 때 get 메소드 사용**

  numbers.get(2) : index 2번째 값 가져오기

  

  **(5) 몇개 데이터 있는 지 확인 : size 메소드 사용**

  numbers.size(); 

  

  **(6) 반복(Iteration)**

  Iterator it = numbers.iterator(); (아래 참고 바람)

  iterator 메소드 호출하여 Iterator 데이터 타입에 넣음

  

  ------

  

  ### Linked List

  - Linked List 란
  - 연결리스트는 노드 하나에 하나의 데이터를 보관하고 노드 내의 링크에 의해 순서 정보(다음 노드의 위치 정보, 이전 노드의 위치 정보)를 기억하는 자료구조입니다.

  <img src = "http://ehpub.co.kr/wp-content/uploads/2016/12/%EA%B7%B8%EB%A6%BC-3.3-%EB%B0%B0%EC%97%B4%EA%B3%BC-%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8.png" />

