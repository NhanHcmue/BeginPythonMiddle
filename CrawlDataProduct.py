#import các thư viện cần để cào dữ liệu
#thư viện requests để lấy dữ liệu trên web
import requests
#thư viện pandas để định dạng dữ liệu
import pandas as pd  
#thư viện tqdm để quan sát xem vòng lặp đã chạy đến đâu rồi 
from tqdm import tqdm

#thêm các biến mặc định của web như cookies, headers, params
cookies = {
	'_trackity': '4e372fff-ac84-f0c4-a18b-a109b4c8603c', 
    '_ga': 'GA1.1.2058824245.1717775787', 
    'amp_99d374': 'm99rAY1PcQy1qqX6GlDKiD...1hvpmkob3.1hvpmkpc0.3.7.a',
    '_hjSessionUser_522327': 'eyJpZCI6ImU4YjFkYWI1LTJhMDEtNTE4YS1hMWUzLTNlZDAwMjc5MjY3OSIsImNyZWF0ZWQiOjE3MTc3NzU3OTEwNDUsImV4aXN0aW5nIjpmYWxzZX0=',
    '__uidac': '0166632db009b8d1cf54ac9040e9d7dd', 
    'dtdz': '62d59c34-5842-5716-8116-5b57fc3cba02', 
    '__adm_upl': 'eyJ0aW1lIjoxNzE3Nzc1Nzk2LCJfdXBsIjpudWxsfQ==',
    '__RC': '5', 
    '__R': '3', 
    '_ga_S9GLR1RQFJ': 'GS1.1.1717775787.1.0.1717775830.17.0.0', 
    'TOKENS': '{"access_token":"F2SwHGscTReUBNtOWi67QAgV4P9JnZEC"}', 
    'tiki_client_id': '2058824245.1717775787'
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

params = (
		('platform', 'web'),
		('spid', '273259162')
	)

#hàm lấy dữ liệu được định trước(lấy những dữ liệu cần thiết)
def parser_product(json):
    d = dict()
    # Lấy ID của mặt hàng
    d['id'] = json.get('id', None)  # Giá trị mặc định là None nếu không có ID
    
    # Lấy tên mặt hàng
    d['name'] = json.get('name', "Unknown Product")  # Giá trị mặc định là "Unknown Product"
    
    # Lấy giá mặt hàng
    d['newPrice'] = json.get('price', 0)  # Giá trị mặc định là 0 nếu không có giá
    
    # Lấy giá gốc để tính giảm giá
    d['oldPrice'] = json.get('original_price', 0)  # Giá trị mặc định là 0
    
    # Lấy các ảnh của mặt hàng
    d['image'] = [
        img.get("base_url", "") for img in json.get("images", []) if img.get("base_url")
    ]  # Lọc các ảnh không hợp lệ
    
    # Lấy ảnh thumbnail
    d['thumbnail'] = json.get('thumbnail_url', "")  # Giá trị mặc định là chuỗi rỗng
    
    # Tạo danh sách colors và memorys để lưu các màu sắc và dung lượng của mặt hàng
    d['colors'] = []
    d['memorys'] = []
    
    # Lấy các tùy chọn cấu hình (nếu có)
    options = json.get('configurable_options', [])
    for option in options:
        if option.get('code') == "option1":
            d['colors'] = [
                value.get('label', "Unknown Color") for value in option.get('values', [])
            ]  # Giá trị mặc định là "Unknown Color"
        elif option.get('code') == "option2":
            d['memorys'] = [
                value.get('label', "Unknown Memory") for value in option.get('values', [])
            ]  # Giá trị mặc định là "Unknown Memory"
    
    # Gắn loại hàng hóa là 'phone'
    d['category'] = 'phone'
    
    return d
#đọc dư liệu trong file product_id.csv để lấy được product_id trên tiki
df_id = pd.read_csv('product_id.csv')
#lưu nó ở dạng list trong biến p_ids
p_ids = df_id.id.to_list()
#in ra xem đã lấy được chưa
print(p_ids)
#tạo list result để lưu kết quả
result = []
#vòng lặp hết tất cả id trong biến p_ids
for pid in tqdm(p_ids, total=len(p_ids)):
    #dùng hàm requests.get để lấy dữ liệu trong link
    response = requests.get(f'https://tiki.vn/api/v2/products/{pid}', headers=headers, params=params, cookies=cookies)
    #nếu status_code ==200 thì tiếp tục
    if response.status_code == 200:
        #hiển thị đã cào dữ liệu thành công cho id 
        print(f'Crawl data {pid} success !!')
        #thêm dữ liệu đã cào, dùng hàm parser_product để định dạng dữ liệu và lấy nhưng dữ liệu cần thiết rồi thêm vào list result
        result.append(parser_product(response.json()))
    #nếu không thì hiển thị lỗi status_code
    else:
        print(f'Error fetching data for {pid}: {response.status_code}')
#dùng thư viện pandas để định dạng dữ liệu
df_product = pd.DataFrame(result)
#chuyển thành file cst có định dạng ngôn ngư
df_product.to_csv('productData.csv', index=False, encoding='utf-8')
df_product_read = pd.read_csv('productData.csv',  encoding='utf-8')
print(df_product_read.head())
