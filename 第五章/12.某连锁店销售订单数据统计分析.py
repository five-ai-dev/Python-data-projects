"""
某连锁店销售订单数据统计分析
参考 11.某连锁店销售订单统计分析.ipynb，完成以下四个统计需求：
    需求1：统计每天销售额的变化（折线图）
    需求2：统计对比不同城市的累计销售数量（柱状图）
    需求3：统计不同产品类别对应的订单比例（饼状图）
    需求4：统计不同支付方式对应的订单比例（饼状图）
"""
from matplotlib.axes import Axes
import pandas as pd
import matplotlib.pyplot as plt


def init_chinese_font():
    """设置matplotlib支持中文显示"""
    plt.rcParams['font.sans-serif'] = ['SimHei']


def load_data(file_path: str = 'data/sales.csv') -> pd.DataFrame:
    """读取销售订单数据

    :param file_path: csv数据文件路径
    :return: 原始订单数据
    """
    return pd.read_csv(file_path)


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """数据清洗：缺失值处理、异常值处理、日期格式统一、计算销售额

    :param data: 原始订单数据
    :return: 清洗后的订单数据
    """
    # 1.缺失值处理
    print('各列缺失值数量：\n', data.isnull().sum())  # 统计缺失值，为0表示没有缺失值
    data['客户所在城市'] = data['客户所在城市'].ffill()  # 填充缺失值,用前一个值填充

    # 2.异常值处理
    print('单价为负的异常订单数量：', (data['单价'] < 0).sum())
    data['单价'] = data['单价'].abs()  # 用绝对值修复负单价

    # 3.数据格式处理：统一日期格式(数据中混有 2025/06/07 这类写法)
    data['订单日期'] = data['订单日期'].str.replace('/', '-')
    data['订单日期'] = pd.to_datetime(data['订单日期'])

    # 4.计算销售额(必须在修复负单价之后)
    data['销售额'] = data['销售数量'] * data['单价']
    return data


def plot_daily_sales(ax: Axes, data: pd.DataFrame):
    """需求1：统计每天销售额的变化（折线图）

    :param ax: 绘图区域
    :param data: 清洗后的订单数据
    """
    # 1.1 分组统计：按天求销售额合计
    day_sales = data.groupby('订单日期')['销售额'].sum()

    # 1.2 组装数据
    min_day = day_sales.index.min()
    max_day = day_sales.index.max()
    # x轴数据：补全中间缺失的日期, freq='D'表示每天，freq='W'表示每周，freq='M'表示每月
    x = pd.date_range(min_day, max_day, freq='D')
    # y轴数据：用reindex对齐,缺失日期补0
    y = day_sales.reindex(x, fill_value=0)

    # 1.3 绘制折线图
    ax.plot(x, y)  # 绘制折线图
    ax.set_title('每天销售额变化', fontsize=16)  # 添加子图标题
    ax.set_xlabel('订单日期', fontsize=12)  # 设置x轴标签
    ax.set_ylabel('销售额', fontsize=12)  # 设置y轴标签
    ax.set_xticks(x)  # 设置x轴刻度
    ax.tick_params(axis='x', rotation=45)  # 30个日期标签旋转45度避免重叠
    ax.grid(linestyle='--', alpha=0.5)  # 添加网格


def plot_city_sales(ax: Axes, data: pd.DataFrame):
    """需求2：统计对比不同城市的累计销售数量（柱状图）

    :param ax: 绘图区域
    :param data: 清洗后的订单数据
    """
    # 2.1 数据处理：按城市汇总销售数量并降序排列
    city_sum = data.groupby('客户所在城市')['销售数量'].sum().sort_values(ascending=False)
    x_city = city_sum.index.tolist()  # x轴数据：城市列表
    y_city_sales_sum = city_sum.values.tolist()  # y轴数据：累计销售数量列表

    # 2.2 绘制柱状图
    ax.bar(x_city, y_city_sales_sum, color='skyblue', width=0.7)  # 绘制柱状图
    ax.set_title('不同城市累计销售数量对比', fontsize=16)  # 添加子图标题
    ax.set_xlabel('城市', fontsize=12)  # 设置x轴标签
    ax.set_ylabel('累计销售数量', fontsize=12)  # 设置y轴标签
    ax.grid(linestyle='--', alpha=0.5)  # 添加网格


def plot_category_pie(ax: Axes, data: pd.DataFrame):
    """需求3：统计不同产品类别对应的订单比例（饼状图）

    :param ax: 绘图区域
    :param data: 清洗后的订单数据
    """
    # 3.1 数据处理：按产品类别统计订单数量
    type_count = data.groupby('产品类别')['产品类别'].count()
    x_type = type_count.index.tolist()  # 产品类别列表
    y_type_count = type_count.values.tolist()  # 对应的订单数量列表

    # 3.2 绘制饼状图
    # autopct='%1.1f%%' : 显示百分比; startangle : 起始角度; radius : 半径
    ax.pie(y_type_count, labels=x_type, autopct='%1.1f%%', startangle=140, radius=1.2)
    ax.set_title('不同产品类别对应的订单比例', fontsize=16, y=1.05)  # 添加子图标题
    ax.legend(loc='lower center', ncol=3, bbox_to_anchor=(0.5, -0.3))  # 添加图例
    ax.axis('equal')  # 确保饼状图是圆的


def plot_payment_pie(ax: Axes, data: pd.DataFrame):
    """需求4：统计不同支付方式对应的订单比例（饼状图）

    :param ax: 绘图区域
    :param data: 清洗后的订单数据
    """
    # 4.1 数据处理：按支付方式统计订单数量
    pay_count = data.groupby('支付方式')['支付方式'].count()
    x_pay = pay_count.index.tolist()  # 支付方式列表
    y_pay_count = pay_count.values.tolist()  # 对应的订单数量列表

    # 4.2 绘制饼状图
    ax.pie(y_pay_count, labels=x_pay, autopct='%1.1f%%', startangle=140, radius=1.2)
    ax.set_title('不同支付方式对应的订单比例', fontsize=16, y=1.05)  # 添加子图标题
    ax.legend(loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.3))  # 添加图例
    ax.axis('equal')  # 确保饼状图是圆的


def main():
    """主函数：完成整体画布搭建、数据清洗与四个统计需求的图表绘制"""
    # 显示中文
    init_chinese_font()

    # 创建子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle('某连锁店销售订单统计分析', fontsize=24, x=0.5, y=0.98)  # 主标题, x=0.5:x轴位置, y=0.98:y轴位置
    fig.subplots_adjust(hspace=0.6, wspace=0.3)  # 调整子图之间的间距, hspace:垂直方向, wspace:水平方向

    # 获取子图
    axes1: Axes = axes[0][0]
    axes2: Axes = axes[0][1]
    axes3: Axes = axes[1][0]
    axes4: Axes = axes[1][1]

    # 读取并清洗数据
    data = clean_data(load_data())

    # 分别完成四个统计需求
    plot_daily_sales(axes1, data)  # 需求1：每天销售额变化（折线图）
    plot_city_sales(axes2, data)  # 需求2：不同城市累计销售数量（柱状图）
    plot_category_pie(axes3, data)  # 需求3：不同产品类别订单比例（饼状图）
    plot_payment_pie(axes4, data)  # 需求4：不同支付方式订单比例（饼状图）

    # 保存图片并显示画布
    plt.savefig('data/某连锁店销售订单统计分析结果图.png')
    plt.show()


if __name__ == '__main__':
    main()
