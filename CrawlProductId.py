#cao du lieu idproduct dien thoai tren tiki shop
#import thu vien
#thư viện requests hộ trợ cào data
import requests
#thư viện pandas để hỗ trợ định dạng dữ liệu
import pandas as pd  


#khai báo các biến cố định trên web, như cookies, headers, params
cookies = {
	'_trackity=4e372fff-ac84-f0c4-a18b-a109b4c8603c; _ga=GA1.1.2058824245.1717775787; amp_99d374=m99rAY1PcQy1qqX6GlDKiD...1hvpmkob3.1hvpmkpc0.3.7.a; _hjSessionUser_522327=eyJpZCI6ImU4YjFkYWI1LTJhMDEtNTE4YS1hMWUzLTNlZDAwMjc5MjY3OSIsImNyZWF0ZWQiOjE3MTc3NzU3OTEwNDUsImV4aXN0aW5nIjpmYWxzZX0=; __uidac=0166632db009b8d1cf54ac9040e9d7dd; dtdz=62d59c34-5842-5716-8116-5b57fc3cba02; __adm_upl=eyJ0aW1lIjoxNzE3Nzc1Nzk2LCJfdXBsIjpudWxsfQ==; __RC=5; __R=3; _ga_S9GLR1RQFJ=GS1.1.1717775787.1.0.1717775830.17.0.0; TOKENS={%22access_token%22:%22F2SwHGscTReUBNtOWi67QAgV4P9JnZEC%22}; tiki_client_id=2058824245.1717775787'
}

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
	'Accept': 'application/json, text/plain, */*',
	'Accept_Langague': 'en,vi;q=0.9,en-US;q=0.8,fr-FR;q=0.7,fr;q=0.6',
	'Referer': 'https://tiki.vn/dien-thoai-smartphone/c1795',
	'X-Guest-Token': 'F2SwHGscTReUBNtOWi67QAgV4P9JnZEC',
	'Connection': 'keep_alive',
	'TE': 'Trailers',
}

params = {
	'limit': '10',
	'sort': 'top_seller',
	'page': '1',
	'urlKey': 'dien-thoai-smartphone',
	"category": '1795',
}

#tạo list để lưu trữ product_id
product_id = []
#lặp từ trang 1 để trang 11
for i in range(1, 11):
	#gắn giá trị page trong params bằng giá trị i
	params['page'] = i
	#dùng hàm requests.get để lấy dữ liệu
	response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings', headers= headers, params = params)
	if response.status_code == 200:
		#trên trạng có status_code nếu nó bằng 200 thì vào vòng if
		print('requests success')
		for record in response.json().get('data'):
			product_id.append({'id': record.get('id')})
		#lấy các dòng trong response 
		#lấy dòng bắt đầu bằng 'id' rồi thêm vào list product_id
df = pd.DataFrame(product_id)
#dùng thư viện pandas để tạo thành file csv
df.to_csv('product_id.csv', index= False)




# {
#   "name": "Điện thoại iPhone 16 Pro Max 256GB",
#   "newPrice": 34990000,
#   "oldPrice": 40000000,
#   "image": [
#     "http://res.cloudinary.com/annnn/image/upload/v1728750500/zgfalsuxqbev571dddro.jpg",
#     "http://res.cloudinary.com/annnn/image/upload/v1728750500/kwlacegobwns4kery4pp.jpg",
#     "http://res.cloudinary.com/annnn/image/upload/v1728750500/qwegyt3jk1mmulm6v4lp.jpg",
#     "http://res.cloudinary.com/annnn/image/upload/v1728750500/lkgt5ehg19ejnpyuji9u.jpg",
#     "http://res.cloudinary.com/annnn/image/upload/v1728750501/dqiq217opsxkgoyhllu6.jpg",
#     "http://res.cloudinary.com/annnn/image/upload/v1728750501/jthe610ies8at64cd7yf.jpg",
#     "http://res.cloudinary.com/annnn/image/upload/v1728750500/elfjsilzemhxhsl7dk7o.jpg",
#     "http://res.cloudinary.com/annnn/image/upload/v1728750500/h2eofg6jf9ll0zg6i04n.jpg",
#     "http://res.cloudinary.com/annnn/image/upload/v1728750500/becivzowoz2xwge7j8g6.jpg"
#   ],
#   "thumnail": "http://res.cloudinary.com/annnn/image/upload/v1728750503/arkhs52vbtuv0kwwvthk.jpg",
#   "colors": [
#     "Titan Trắng",
#     "Titan Sa Mạc ",
#     "Titan tự nhiên",
#     "Titan đen"
#   ],
#   "memorys": [
#     "256",
#     "512",
#     "1TB"
#   ],
#   "category": "Phone",
#   "createdAt": "2024-10-12T16:28:24.105Z",
#   "updatedAt": "2024-10-12T16:30:23.265Z",
#   "__v": 0
# }
