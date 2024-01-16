

import os


# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

# Call Django's setup to configure the settings
import django
django.setup()

# from works.models import WeeklyReport
from publications.models import Patent


data = {
	"table": "publications_patent",
	"rows":
	[
		{
			"status": 2,
			"writer": "관리자",
			"subject": "[2021.09.17.] Mobile Electronic wallet system based on Block chain technology",
			"content": "발명자: 김동성,사비어,이재민\r\n\r\n출원번호: 10-2021-0124951(PCT/KR2021/015676)\r\n출원일: 2021.09.17.\r\n\r\n발명의명칭: Mobile Electronic wallet system based on Block chain technology(블록체인 기반의 모바일 전자지갑 시스템)",
			"tcp_ip": "202.31.137.123",
			"write_date": "2021-12-20 11:51:19",
			"update_date": None,
			"visit": 402,
			"ref": "202112200001"
		},
		{
			"status": 2,
			"writer": "관리자",
			"subject": "[2021.10.01.] Fast Successive Approximation ADC With series Time-Interleaved Architecture",
			"content": "발명자: 김동성,유슈ㅂ 모알림,이재민\r\n\r\n출원일자: 2021.10.01.\r\n출원번호: 10-2021-0130498(PCT/KR2021/015714)\r\n\r\n발명의 명칭: Fast Successive Approximation ADC With series Time-Interleaved Architecture(직렬 시간 인터리브 구조기반의 고성능 아날로그 디지털 컨버터)",
			"tcp_ip": "202.31.137.123",
			"write_date": "2021-12-20 11:52:16",
			"update_date": None,
			"visit": 391,
			"ref": "202112200002"
		},
		{
			"status": 4,
			"writer": "관리자",
			"subject": "[2008.02.19] Method for real-time transmission of wireless fieldbus(무선 필드버스를 이용한 실시간 전송 방법)",
			"content": "Method for real-time transmission of wireless fieldbus(무선 필드버스를 이용한 실시간 전송 방법)\r\n(https://doi.org/10.8080/1020070015005)\r\n\r\nIPC : H04W 74/00 H04W 72/00\r\n\r\n출원번호/일자 : 1020070015005 (2007.02.13)\r\n\r\n출원인 : 금오공과대학교 산학협력단\r\n\r\n등록번호/일자 : 1008075290000 (2008.02.19)\r\n\r\n발명자 : 김동성, 이정일, 정지원, 최동혁",
			"tcp_ip": "202.31.137.123",
			"write_date": "2021-12-20 18:17:23",
			"update_date": None,
			"visit": 379,
			"ref": "202112200003"
		},
		{
			"status": 4,
			"writer": "관리자",
			"subject": "[2008.10.31] System and method for wireless management for pet dog in home environment(무선 센서 네트워크를 이용한 애완견 관리 시스템 및 그방법)",
			"content": "System and method for wireless management for pet dog in home environment\r\n(무선 센서 네트워크를 이용한 애완견 관리 시스템 및 그방법)\r\n(https://doi.org/10.8080/1020070007607)\r\n\r\nIPC : G06Q 50/00D0 H04W 84/18\r\n\r\n출원번호/일자 : 1020070007607 (2007.01.24)\r\n\r\n출원인 : 금오공과대학교 산학협력단\r\n\r\n등록번호/일자 : 1008675540000 (2008.10.31)\r\n\r\n발명자 : 김동성, 정지원, 이정일",
			"tcp_ip": "202.31.137.123",
			"write_date": "2021-12-20 18:17:45",
			"update_date": None,
			"visit": 425,
			"ref": "202112200004"
		},
		{
			"status": 4,
			"writer": "관리자",
			"subject": "[2010.06.29]DYNAMIC GTS ALLOCATION METHOD FOR WIRELESS CONTROL NETWORK USING IEEE 802.15.4(ＩＥＥＥ 802.15.4 기반의 무선 제어 네트워크를 위한 동적ＧＴＳ할당 방법)",
			"content": "DYNAMIC GTS ALLOCATION METHOD FOR WIRELESS CONTROL NETWORK USING IEEE 802.15.4\r\n(ＩＥＥＥ 802.15.4 기반의 무선 제어 네트워크를 위한 동적ＧＴＳ할당 방법)\r\n(https://doi.org/10.8080/1020080038743)\r\n\r\n출원번호/일자 : 1020080038743 (2008.04.25)\r\n\r\n출원인 : 금오공과대학교 산학협력단\r\n\r\n등록번호/일자 : 1009683460000 (2010.06.29)\r\n\r\n발명자 : 김동성, 이정일, 정지원, 김윤섭, 김준우",
			"tcp_ip": "",
			"write_date": "2021-12-20 18:18:09",
			"update_date": "2022-03-03 01:24:53",
			"visit": 375,
			"ref": "202112200005"
		}
	]
}
def populate():
    for row in data['rows']:
        Patent.objects.create(**row)

if __name__ == '__main__':
    populate()
    print("working again")