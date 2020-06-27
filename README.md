Spring
=============

## JPA

**> 왜 JPA를 학습해야 하는가**
1. 도메인 주도 개발 가능
* 애플리케이션의 코드가 SQL 데이터베이스 관련 코드에 잠식 당하는 것을
방지하고 도메인 기반의 프로그래밍으로 비즈니스 로직을 구현하는데 집중할
수 있습니다.

2. 그리고 개발 생산성에 좋으며, 데이터베이스에 독립적인 프로그래밍이 가능하고, 타입
세이프한 쿼리 작성 그리고 Persistent Context가 제공하는 캐시 기능으로 성능
최적화까지 가능합니다.

**> JDBC란?**
* 데이터베이스에 접속 할때 데이터베이스서버와 클라이언트서버를 이어주는 연결고리
1. JDBC를 사용할 때 쓰는 것
* DataSource / DriverManager 데이터베이스의 드라이버에 접근하기 위한 DriverManager
* Connection 으로 데이터베이스 정보와 연결
* PreparedStatement로 미리 쿼리문을 작성함으로써 코드를 간결하게 유지
* **EX)코드
```
@Bean(destroyMethod = "close")
	public DataSource dataSource() {
		DataSource ds = new DataSource();
		ds.setDriverClassName("com.mysql.jdbc.Driver");
		ds.setUrl("jdbc:mysql://localhost/spring-Test?characterEncoding=utf8");
		ds.setUsername("spring5");
		ds.setPassword("spring5");
		ds.setInitialSize(2);
		ds.setMaxActive(10);
		ds.setTestWhileIdle(true);
		ds.setMinEvictableIdleTimeMillis(60000 * 3);
		ds.setTimeBetweenEvictionRunsMillis(10 * 1000);
		
		return ds;
	}
  ```
**> JDBC의 단점**
1. SQL을 실행하는 비용이 비싸다.
2. SQL이 데이터베이스 마다 다르다.
3. 스키마를 바꿨더니 코드가 너무 많이 바뀌네...
4. 반복적인 코드가 너무 많아.
5. 당장은 필요가 없는데 언제 쓸 줄 모르니까 미리 다 읽어와야 하나...

**> JPA를 사용하는 이유(도메인 모델)**
1. 객체 지향 프로그래밍의 장점을 활용하기 좋으니까.
2. 각종 디자인 패턴
3. 코드 재사용
4. 비즈니스 로직 구현 및 테스트 편함.

