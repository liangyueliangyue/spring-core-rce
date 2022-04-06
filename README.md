# spring-core-rce
spring core rce 简单利用

war可以使用
https://github.com/fengguangbin/spring-rce-war
docker环境可以使用
https://github.com/lunasec-io/Spring4Shell-POC

指定url和type即可
type（默认为1）
  1  --> 测试漏洞是否存在
  2  --> 冰蝎马注入，密码rebeyond
  3  --> 哥斯拉马注入，密码pss
  
可选参数
  filename  --> 文件名(默认inject)
  directory  --> 写入路径(默认webapps/ROOT)
