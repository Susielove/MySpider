import requests

url = "http://www.renren.com/PLogin.do"
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Cookie": "anonymid=jpf70le8-9ae8tv; depovince=JS; jebecookies=44141ed3-133c-4e43-bee6-c06ad192477d|||||; _r01_=1; JSESSIONID=abcl3nDsnXPdQ7k7R6mEw; ick_login=4c1aad9e-79e6-4959-90cd-02b3011f795a; _de=4CF6CB302AA2195C2C7FD618744BFAA5; p=1c1aae36295ac84d281a8cb74f27a9e50; first_login_flag=1; ln_uact=13862332046; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=e91b5da895f7429daba967856be7a78e0; societyguester=e91b5da895f7429daba967856be7a78e0; id=969029780; xnsid=7312785c; ver=7.0; loginfrom=null; jebe_key=09519390-cd6a-4a60-9423-0e0cd42bc289%7C035f4dae732f625f4302ef7a8a179598%7C1544257637927%7C1%7C1544257636376; wp_fold=0"}

response = requests.get(url, headers=headers)
print(response.status_code)
file_path = "{}.html".format("人人网带cookie")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(response.content.decode())
