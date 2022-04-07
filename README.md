# spring-core-rce  
spring core rce 简单利用  

war可以使用  
https://github.com/fengguangbin/spring-rce-war  
docker环境可以使用  
https://github.com/lunasec-io/Spring4Shell-POC  

也可以使用vulfocus的在线环境  
http://vulfocus.io/  
或者vulhub的靶场  
https://github.com/vulhub/vulhub/tree/master/spring/CVE-2022-22965  

vulfocus环境冰蝎马能够写入但无法连接，新增了哥斯拉shell进行测试  

指定url和type即可  
type（默认为1）  
  1  --> 测试漏洞是否存在  
  2  --> 冰蝎马注入，密码rebeyond  
  3  --> 哥斯拉马注入，密码pass  
可选参数  
  filename  --> 文件名(默认inject)  
  directory  --> 写入路径(默认webapps/ROOT)  
