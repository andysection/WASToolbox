import json

def process_color_data(input_json_path):
    # 读取 JSON 文件
    with open(input_json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
        # 检查 JSON 文件的结构
        if 'colors' not in data:
            print("Error: JSON format is incorrect. 'colors' key is missing.")
            return
        
        output_m_file = 'MMAppTheme+Color.m'
        output_h_file = 'MMAppTheme+Color.h'

        # 写入第一个文件，开头包含：#import <Foundation/Foundation.h>
        with open(output_h_file, 'w', encoding='utf-8') as txt_file_1:
            # 写入固定的头部内容
            txt_file_1.write('#import <Foundation/Foundation.h>\n\n')
            txt_file_1.write('@interface MMAppTheme (Color)\n\n')
            txt_file_1.write('#pragma mark - 字体配置\n\n')
            
            # 遍历每个颜色条目并按要求写入文件
            for color in data['colors']:
                name = color.get('name', 'Unknown')
                value = color.get('value', '#000000')  # 默认值为黑色
                comment = color.get('comment', '')
                
                # 判断 value 字段是否以 # 开头，如果是，替换为 0x
                if value.startswith('#'):
                    value = '0x' + value[1:].upper()  # 去掉 #，并转换为 0x 前缀
                
                # 使用 - 连接字段并用 {} 包裹
                color_line = f"///{comment} + {value}\n+ (UIColor *){name};\n\n"
                
                # 写入到文件
                txt_file_1.write(color_line)
                # print(f"Written to file 1: {color_line.strip()}")  # 打印正在写入的内容

            # 写入文件尾部的结束标记
            txt_file_1.write('@end\n')
            print(f"written to {output_h_file} successfully")
        
        # 打开输出文本文件
        with open(output_m_file, 'w', encoding='utf-8') as txt_file:
            # 写入固定的头部内容
            txt_file.write('#import "MMAppTheme+Color.h"\n\n')
            txt_file.write('@implementation MMAppTheme\n\n')
            txt_file.write('#pragma mark + 颜色配置\n\n')

            # 遍历每个颜色条目并按要求写入文件
            for color in data['colors']:
                name = color.get('name', 'Unknown')
                value = color.get('value', '#000000')  # 默认值为黑色
                comment = color.get('comment', '')
                # 判断 value 字段是否以 # 开头，如果是，替换为 0x
                if value.startswith('#'):
                    value = '0x' + value[1:].upper()  # 去掉 #，并转换为 0x 前缀

                # 使用 - 连接字段
                color_line = f"///{comment}\n+ (UIColor *){name} {{\n \treturn HexColor({value});\n}}\n"
                
                # 写入到文件
                txt_file.write(color_line)
                # print(f"Written: {color_line.strip()}")  # 打印正在写入的内容
            # 写入文件尾部的结束标记
            txt_file.write('@end\n')
            print(f"written to {output_m_file} successfully")

    

# 输入和输出文件路径
input_json_file = 'iOSColors.json'  # 你的输入 JSON 文件路径

# 调用函数
process_color_data(input_json_file)
