# 시작하기 전에
access token 은 BAND OPEN API 호출에 필수적인 파라메터입니다. access token을 획득하는 가장 쉬운 방법은 본인의 BAND OPEN API 애플리케이션을 하나 만들고 등록하면서 밴드 서비스에서 access token을 생성하도록 하는 것입니다. 아래는 developers.band.us 사이트에서 open api 애플리케이션을 만드는 방법을 설명합니다.

# 나의 첫 번째 BAND OPEN API 애플리케이션

먼저 웹 브라우저를 열고 https://band.us 에 로그인을 합니다. (가입 전이라면 가입부터 해야겠지요.)
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/03ca360c-bd61-4949-8fd9-bab068bea1e0)
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/bd821574-ceae-4158-81a2-7e26d4e4d2f0)

로그인을 완료한 후 https://developers.band.us 의 내 서비스 메뉴로 들어갑니다.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/2d0a11cf-f7f2-4f48-a006-f8e7875dde8f)

내 서비스 등록 메뉴를 통해 open api 애플리케이션을 생성합니다.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/1ba41571-7537-4143-98fe-1d6a30213113)

서비스 명은 BAND OPEN API by Perl로 하고 서비스 유형은 원하는 것을 선택합니다.

Redirect URL은 제 3자가 우리가 만든 앱을 사용하여 밴드 서비스를 이용할 때 해당 사용자의 access token을 밴드 OPEN API 서버로 부터 전달받을 웹 리소스 위치를 의미합니다. 따라서 지금은 임의의 값을 넣고 지나갑시다.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/6a590e66-457e-4549-88a7-f528f85ea434)

약관까지 동의하고 확인합니다.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/8a427561-05dd-4122-a111-786cdf614761)
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/49f016c8-12a1-4666-b32d-a0147ceb90ee)

방금 생성된 BAND OPEN API by Perl 애플리케이션은 다음과 같습니다.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/0b3bad31-0126-457a-afca-e9c888822008)

Access Token 항목에 밴드 계정 연동 을 클릭하면 해당 애플리케이션을 위한 access token 을 얻을 수 있습니다.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/10f32800-1db9-4e13-965a-cf9336b011bf)

우리가 가진 모든 밴드에 접근 권한을 가진 access token 을 만들기 위해 아래와 같이 가입한 모든 밴드에 권한을 허용합니다.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/beaa35d8-cc98-41e7-b880-f3bed9566c33)

이후 동의하면 access token 이 생성됩니다.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/8027facf-0a42-4271-a77f-205cb460b0cd)

ZQ 로 시작하고 _xjqf 로 끝나는 당신의 모든 밴드에 접근 권한을 가진 access token 생성에 성공하였습니다.
이제 info.txt.default 파일을 info.txt 로 변경한 후 info.txt 의 access_token 필드의 값을 방금 생성한 access token 값으로 대체하세요.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/de5802f1-765e-4980-9937-e96eea7fc2bb)

이제 콘솔 창을 열어 bandopenapi 디렉터리로 이동한 후 아래 명령으로 환경검사를 시행합시다.
```
perl 0.환경검사.pl
```
축하합니다. 이제 다양한 예제 프로그램을 시도하여 보십시오.
```
perl 숫자.BAND_OPENAPI_기능.pl
```

# 오류 대응
## perl 프로그램이 설치되지 않았습니다.
대부분의 *nix 환경에서 Perl은 기본 설치되어 있습니다. Windows의 경우 딸기 펄(https://strawberryperl.com/) 을 설치하거나 윈도우즈 위에 리눅스 시스템을 설치할 수 있는 WSL 환경을 구축하세요. (https://learn.microsoft.com/ko-KR/windows/wsl/install)
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/26bb4e4f-7c2c-4890-86a6-f2ba28835ab6)
## 짧은 간격의 호출은 거부됩니다.
10초 정도 시간 간격을 유지하세요.
![image](https://github.com/heetakchoi/bandopenapi/assets/3896162/b6e3206d-1941-4621-a4a6-3e1af1827251)





