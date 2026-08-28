import csv
import os
import random
from datetime import date, timedelta

# 以脚本所在目录（第五章）为基准，定位 data 文件夹
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)  # data 文件夹不存在则自动创建
file_path = os.path.join(data_dir, 'sales.csv')

# 产品类别 -> 产品名称，保证类别和产品名称匹配
products = {
    '家居用品': ['枕头', '毯子', '保温杯', '收纳盒', '台灯'],
    '食品': ['海苔', '饼干', '坚果', '牛奶', '巧克力'],
    '电子产品': ['智能音箱', '蓝牙耳机', '充电宝', '电动牙刷', '鼠标'],
    '图书': ['小说', '漫画', '教材', '绘本', '杂志'],
    '服装': ['T恤', '牛仔裤', '运动鞋', '帽子', '外套'],
}

cities = ['合肥', '天津', '福州', '北京', '广州', '郑州', '武汉',
          '青岛', '重庆', '深圳', '南京', '昆明', '上海', '杭州', '成都']

payments = ['支付宝', '微信支付', '银行卡', '现金']

# 生成 1000 个不重复的 10 位订单号
order_ids = set()
while len(order_ids) < 1000:
    order_ids.add(random.randint(1000000000, 9999999999))

# 订单日期范围：2025-06-01 ~ 2025-06-30
start_date = date(2025, 6, 1)

rows = []
for order_id in order_ids:
    category = random.choice(list(products.keys()))
    name = random.choice(products[category])
    quantity = random.randint(1, 10)
    price = random.randint(1, 399)
    city = random.choice(cities)
    payment = random.choice(payments)
    order_date = start_date + timedelta(days=random.randint(0, 29))
    rows.append([order_id, category, name, quantity, price,
                 city, payment, order_date.strftime('%Y-%m-%d')])

with open(file_path, mode='w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['订单号', '产品类别', '产品名称', '销售数量', '单价', '客户所在城市', '支付方式', '订单日期'])
    writer.writerows(rows)

print(f'已生成 {len(rows)} 条销售数据：{file_path}')
