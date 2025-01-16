import json

def process_color_data(input_json_path):
    # 读取 JSON 文件
    with open(input_json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
        # 检查 JSON 文件的结构
        if 'colors' not in data:
            print("Error: JSON format is incorrect. 'colors' key is missing.")
            return
        
        output_xml_file = 'colors.xml'

        # 打开输出文本文件
        with open(output_xml_file, 'w', encoding='utf-8') as txt_file:
            # 写入固定的头部内容
            txt_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
            txt_file.write('<resources>\n')
            txt_file.write('\t<color name="colorPrimary">#7183BB</color>\n')
            txt_file.write('\t<color name="colorPrimaryDark">#7183BB</color>\n')
            txt_file.write('\t<color name="colorAccent">#7183BB</color>\n')
            txt_file.write('\t<color name="xm_background">#FFFFFF</color>\n')
            txt_file.write('\t<color name="xm_button_color_normal">@color/colorPrimary</color>\n')
            txt_file.write('\t<color name="xm_button_color_pressed">@color/colorPrimary</color>\n')
            txt_file.write('\t<color name="xm_button_color_disable">@color/colorPrimary</color>\n')
            txt_file.write('\t<color name="black">#FF000000</color>\n')
            txt_file.write('\t<color name="white">#FFFFFFFF</color>\n')
            txt_file.write('\t<color name="transparent">#00FFFFFF</color>\n')
            txt_file.write('\t<color name="white_text">#FFF</color>\n')
            txt_file.write('\t<color name="black_text">#333333</color>\n')

            # 遍历每个颜色条目并按要求写入文件
            for color in data['colors']:
                name = color.get('name', 'Unknown')
                value = color.get('value', '#000000')  # 默认值为黑色
                comment = color.get('comment', '')
                # 判断 value 字段是否以 # 开头，如果是，替换为 0x
                if value.startswith('0x'):
                    value = '#' + value[2:].upper()  # 去掉 #，并转换为 0x 前缀

                # 使用 - 连接字段
                color_line = f"\t<!--  {comment}  -->\n\t<color name=\"{name}\">{value}</color>\n\n"
                
                # 写入到文件
                txt_file.write(color_line)
                # print(f"Written: {color_line.strip()}")  # 打印正在写入的内容
            # 写入文件尾部的结束标记
            txt_file.write('</resources>\n')
            print(f"Android written to {output_xml_file} successfully")

    

# 输入和输出文件路径
input_json_file = 'androidColors.json'  # 你的输入 JSON 文件路径

# 调用函数
process_color_data(input_json_file)
